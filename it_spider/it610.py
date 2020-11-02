import scrapy


class It610Spider(scrapy.Spider):
    name = 'it610'
    allowed_domains = ['it610.com']
    start_urls = ['https://it610.com/']

    def parse(self, response):
        print(response)
        pass
