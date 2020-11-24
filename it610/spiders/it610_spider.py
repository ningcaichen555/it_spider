from faker import Faker
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from it610.image.ImageUp import ImageUp
from it610.items import ArticleItemLoader, ItSpiderItem
from scrapy_redis.spiders import RedisSpider


class It610SpiderSpider(RedisSpider):
    name = 'it610_spider'
    allowed_domains = ['www.it610.com', 'img.it610.com']
    start_urls = ['https://www.it610.com/']
    faker = Faker(locale='zh_CN')

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.imageUp = ImageUp()

    rules = (
        Rule(LinkExtractor(allow=(r'https://www.it610.com/tags/[a-zA-Z0-9]/1.htm')), callback='parse_tags',
             follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url=str("https://www.it610.com/"), callback=self.parse_tags, dont_filter=True, )

    def parse_tags(self, response):
        linkExt = LinkExtractor(allow=r'https://www.it610.com/tags/[a-zA-Z0-9]/1.htm')
        links = linkExt.extract_links(response)
        if links:
            for link in links:
                request = Request(str(link.url), callback=self.parse_search, dont_filter=True,
                                  headers={'Connection': 'close', 'refer': str(response.url)})
                yield request

    def parse_search(self, response):
        linkExt = LinkExtractor(allow=r'https://www.it610.com/search/.*/1.htm')
        links = linkExt.extract_links(response)
        if links:
            for link in links:
                request = Request(str(link.url), callback=self.parse_article, dont_filter=True,
                                  headers={'Connection': 'close', 'refer': str(response.url)})
                yield request
        next_page_str = response.xpath(
            '//div[contains(@class,"container") and contains(@class,"mt10")]/div[contains(@class,"page_mod") and contains(@class,"mt15")]/span[@class="page_next"]/a/@href').get()
        if next_page_str:
            next_page = "https://www.it610.com" + next_page_str
            Request(next_page, callback=self.parse_search,
                    headers={'Connection': 'close', 'refer': str(response.url)})

    def parse_article(self, response):
        linkExt = LinkExtractor(allow=r'/article/.*.htm')
        links = linkExt.extract_links(response)
        if links:
            for link in links:
                url = link.url.replace("https://www.it610.com", "")
                xpath_str = '//a[contains(@href,"%s")]/div[@class="article-excerpt"]' % url
                article_summary = response.xpath(xpath_str).getall()
                request = Request(str(link.url), callback=self.parse_article_detail,
                                  meta={"article_summary": "".join(article_summary)},
                                  headers={'Connection': 'close', 'refer': str(response.url)})
                yield request
        next_page_str = response.xpath(
            '//div[contains(@class,"container") and contains(@class,"mt10")]/div[contains(@class,"page_mod") and contains(@class,"mt15")]/span[@class="page_next"]/a/@href').get()
        if next_page_str:
            next_page = "https://www.it610.com" + next_page_str
            Request(next_page, callback=self.parse_article,
                    headers={'Connection': 'close', 'refer': str(response.url)})

    def parse_article_detail(self, response):
        article_itemLoader = ArticleItemLoader(item=ItSpiderItem(), response=response)
        article_summary = response.meta.get("article_summary")
        if article_summary:
            article_itemLoader.add_value("article_summary", article_summary)
        else:
            article_itemLoader.add_value("article_summary", 'article_summary')

        public_title = response.xpath('//div/h1[@id="articleTitle"]/text()').get()
        if public_title:
            article_itemLoader.add_value("title", public_title)

        public_anthor = response.xpath(
            '//div[@class="article__authorright"]/div[@class="article__authormeta"]/a/strong/text()').get()
        if public_anthor:
            article_itemLoader.add_value("author", public_anthor)
        else:
            randomName = self.faker.name()
            article_itemLoader.add_value("author", randomName)

        public_time = response.xpath('//div[@class="article__authorright"]//span/text()').get()
        if public_time:
            article_itemLoader.add_value("pub_time", public_time)
        else:
            article_itemLoader.add_value("pub_time", "")

        article_itemLoader.add_value("origin_url", response.url)
        article_itemLoader.add_value("article_id", response.url)

        public_content = response.xpath('//div[@class="markdown_views"]/div[@id="article_content"]').get()
        if public_content:
            article_itemLoader.add_value("content", public_content)

        public_subject = response.xpath('//ul[contains(@class,"taglist--inline")]/li/a[@class="tag"]/text()').get()
        if public_subject:
            article_itemLoader.add_value("subject", public_subject.strip())
        else:
            article_itemLoader.add_value("subject", 0)

        item = article_itemLoader.load_item()
        yield item
