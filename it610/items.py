# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import datetime
import hashlib

import scrapy
from itemloaders import ItemLoader
from itemloaders.processors import MapCompose, Identity
from scrapy.loader.processors import TakeFirst


# 定义一个时间处理转换函数
# 将 '\r\n\r\n            2018/03/06 ·  ' 转换成 datetime.date(2018, 3, 14)
def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def md5_convert(value):
    try:
        md5_value = hashlib.md5(value.encode('utf-8')).hexdigest()
    except Exception as e:
        md5_value = 0
        print("md5_convert" + e)
    return md5_value


def title_convert(value):
    try:
        if len(value) >= 50:
            value = value[0:49]
    except Exception as e:
        print("title_convert" + e)
    return value


class It610Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ItSpiderItem(scrapy.Item):
    # 标题
    title = scrapy.Field(
        input_processor=MapCompose(title_convert)
    )
    # 作者ID
    author = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 文章地址
    origin_url = scrapy.Field()
    # 文章id
    article_id = scrapy.Field(
        input_processor=MapCompose(md5_convert)
    )
    # 文章内容
    content = scrapy.Field()
    # 文章字数
    word_count = scrapy.Field()
    # 浏览量
    view_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 喜欢数
    like_count = scrapy.Field()
    # 文章标签
    subject = scrapy.Field()


class ImageItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ImageItems(scrapy.Item):
    image_urls = scrapy.Field(
        output_processor=Identity()
    )
    origin_image = scrapy.Field(
        output_processor=Identity()
    )
    header = scrapy.Field()
    publish_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    image_id = scrapy.Field()
    # 文章内容
    content = scrapy.Field()
    # 文章id
    article_id = scrapy.Field()