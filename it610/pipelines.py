# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi
from pymysql import cursors
from it610.image.ImageUp import ImageUp
from it610.items import ItSpiderItem, ImageItems, ImageItemLoader, md5_convert
from it610.settings import MY_SETTINGS

INSERT_SQL = """INSERT INTO article ( title, author, pub_time, origin_url, article_id, content,article_desc, word_count, view_count, comment_count, like_count, subjects ) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )"""


# 上传到mysql
class ItSpiderPipeline:
	# 创建初始化函数，当通过此类创建对象时首先被调用的方法
	def __init__(self, dbpool):
		self.dbpool = dbpool

	@classmethod
	def from_settings(cls, settings):
		settings = MY_SETTINGS
		settings['cursorclass'] = cursors.DictCursor
		dbpool = adbapi.ConnectionPool("pymysql", **settings)
		return cls(dbpool)

	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self.db_insert, item)
		query.addErrback(self.handle_error, item)
		return item

	def handle_error(self, failure, item):
		print('it_spider_handle_sql_error', failure, item)

	def db_insert(self, cursor, item):
		tt = cursor._connection._connection
		try:
			tt.ping()
		except Exception as e:
			print('it_spider_handle_sql_exception', e)
			self.dbpool.close()
			settings = MY_SETTINGS
			settings['cursorclass'] = cursors.DictCursor
			self.dbpool = adbapi.ConnectionPool("pymysql", **settings)
		try:
			cursor.execute(
				INSERT_SQL,
				(item['title'], item['author'], item['pub_time'], item['origin_url'], item['article_id'],
				 item['content'], item['article_summary'], 0, 0, 0,
				 0, item['subject']))
		except Exception as e:
			print("重複添加")
		print("=====title=====" + item['title'] + "=====origin_url=====" + item['origin_url'])
		return item


# 上传本地图片
class UploadImagePipeline:
	# 创建初始化函数，当通过此类创建对象时首先被调用的方法
	def __init__(self):
		self.imageUp = ImageUp()

	def process_item(self, item, spider):
		if item.get("imageItem"):
			imageItem = item["imageItem"]
			for url in imageItem["image_urls"]:
				key = os.path.basename(url)
				# 上传之后地址
				ret, info = self.imageUp.upload(key, "./images/" + url)
				if os.path.exists("./images/" + url):
					os.remove("./images/" + url)
				realImageUrl = "https://img.zhifoubj.com/" + key
				origin_url = imageItem["origin_image_map"][key]
				content = item.get("content")
				item["content"] = content.replace(origin_url, realImageUrl)
			return item
		else:
			return item

	def handle_error(self, failure, item):
		print('it_spider_handle_error', failure, item)
		return item


# 保存本地图片
class SaveImagePipeline(ImagesPipeline):
	default_headers = {
		'referer': '',
		'Connection': 'close',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
	}

	def get_media_requests(self, item, info):
		content = item['content']
		imageRes = re.findall(r'\"(https://img.it610.com/image.*?)\"', content)
		origin_image_map = {}
		for origin in imageRes:
			filePath = u'%s.jpg' % (md5_convert(origin))
			origin_image_map[filePath] = origin
		if imageRes:
			imageItemLoader = ImageItemLoader(item=ImageItems())
			imageItemLoader.add_value("image_urls", list(set(imageRes)))
			imageItemLoader.add_value("origin_image_map", origin_image_map)
			imageItemLoader.add_value("referer", item["origin_url"])
			imageItemLoader.add_value("article_id", item["article_id"])
			item["imageItem"] = imageItemLoader.load_item()
		else:
			return item
		image_item = item["imageItem"]
		# 下载图片，如果传过来的是集合需要循环下载
		# meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
		if isinstance(item, ItSpiderItem) and image_item.get('image_urls'):
			self.default_headers['referer'] = image_item["referer"]
			for url in image_item['image_urls']:
				yield scrapy.Request(url=url, headers=self.default_headers)

	def item_completed(self, results, item, info):
		'''所有图片处理完毕后（不管下载成功或失败），会调用item_completed进行处理
		   results是一个list 第一个为图片下载状态,
		   get_media_requests在图片下载完毕后，处理结果会以二元组的方式返回给item_completed()函数的
		   results，图片下载状态定义如下：
			   (success, image_info_or_failure)
			   success表示图片是否下载成功；image_info_or_failure是一个字典
		'''
		image_path = [x['path'] for ok, x in results if ok]
		# if not image_path:
		#     raise DropItem('Item contains no images')
		image_item = item.get("imageItem")
		if image_item:
			image_item['image_urls'] = image_path
		return item

	def file_path(self, request, response=None, info=None, item=None):
		filePath = u'%s.jpg' % (md5_convert(request.url))
		return filePath
