import os
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from it610.items import ArticleItemLoader, ItSpiderItem


class It610SpiderSpider(CrawlSpider):
    name = 'it610_spider'
    allowed_domains = ['www.it610.com']
    start_urls = ['https://www.it610.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'https://www.it610.com/tags/[a-zA-Z0-9]/1.htm')), callback='parse_tags',
             follow=True),
    )

    def parse_tags(self, response):
        # print(response.body)
        linkExt = LinkExtractor(allow=r'https://www.it610.com/search/.*/1.htm')
        links = linkExt.extract_links(response)
        if links:
            for link in links:
                request = Request(str(link.url), callback=self.parse_search,
                                  headers={'Connection': 'close', 'refer': str(response.url)})
                yield request

    def parse_search(self, response):
        linkExt = LinkExtractor(allow=r'/article/.*.htm')
        links = linkExt.extract_links(response)
        if links:
            for link in links:
                request = Request(str(link.url), callback=self.parse_article,
                                  headers={'Connection': 'close', 'refer': str(response.url)})
                yield request

    def parse_article(self, response):
        article_itemLoader = ArticleItemLoader(item=ItSpiderItem(), response=response)
        public_title = response.xpath('//div/h1[@id="articleTitle"]/text()').get()
        if public_title:
            article_itemLoader.add_value("title", public_title)
        public_anthor = response.xpath(
            '//div[@class="article__authorright"]/div[@class="article__authormeta"]/a/strong/text()').get()
        article_itemLoader.add_value("author", public_anthor)
        public_time = response.xpath('//div[@class="article__authorright"]//span/text()').get()
        article_itemLoader.add_value("pub_time", public_time)
        article_itemLoader.add_value("origin_url", response.url)
        article_itemLoader.add_value("article_id", response.url)
        article_itemLoader.add_value("content",
                                     response.xpath('//div[@class="markdown_views"]/div[@id="article_content"]').get())
        public_subject = response.xpath('//ul[contains(@class,"taglist--inline")]/li/a[@class="tag"]/text()').get()
        if public_subject:
            article_itemLoader.add_value("subject", public_subject)
        else:
            article_itemLoader.add_value("subject", 0)
        item = article_itemLoader.load_item()
        yield item
