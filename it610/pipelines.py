# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from it610.image.ImageUp import ImageUp
from it610.items import ItSpiderItem, ImageItems, ImageItemLoader


class UploadImagePipeline:
    # 创建初始化函数，当通过此类创建对象时首先被调用的方法
    def __init__(self):
        self.imageUp = ImageUp()

    def process_item(self, item, spider):
        # print(item)
        # imagePath = item["image_urls"][index]
        # realImagePath = item["origin_image"][index]
        # realImagePath = realImagePath.replace("https:", "")
        # key = os.path.basename(imagePath)
        # ret, info = self.imageUp.upload(key, "../images/" + imagePath)
        # newImagePath = ret["key"]
        # content = content.replace(realImagePath, newImagePath)
        # item['content'] = content
        return item

    def handle_error(self, failure, item):
        print('============================', failure, item)
        return item


class SaveImagePipeline(ImagesPipeline):
    it_spider_item = None

    default_headers = {
        'referer': '',
        'Connection': 'close'
    }

    def get_media_requests(self, item, info):
        content = item['content']
        imageRes = re.findall(r'\"(https://img.it610.com/image.*?)\"', content)
        if imageRes:
            imageItemLoader = ImageItemLoader(item=ImageItems())
            imageItemLoader.add_value("image_urls", imageRes)
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
                print(url)
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
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_urls'] = image_path
        return item

    def file_path(self, request, response=None, info=None):
        filePath = u'%s/%s.jpg' % (request.meta['publish_date'], request)
        return filePath
