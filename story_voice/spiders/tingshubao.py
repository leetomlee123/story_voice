import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class TingshubaoSpider(CrawlSpider):
    name = 'tingshubao'
    allowed_domains = ['m.tingshubao.com']
    start_urls = ['http://m.tingshubao.com/']
    rules = [
    Rule(LinkExtractor(allow=r'book/\d+.html'), callback='parse_item')
    ]
    def parse_item(self,response):
        print(response.text)
