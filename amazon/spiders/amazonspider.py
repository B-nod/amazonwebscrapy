import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    def parse(self, response):
        pass
