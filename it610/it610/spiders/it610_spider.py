import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class It610SpiderSpider(CrawlSpider):
    name = 'it610_spider'
    allowed_domains = ['www.it610.com']
    start_urls = ['https://www.it610.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'https://www.it610.com/search/.*/1.htm')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        print(response)
        return item
