from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ItaoDemandSpider(CrawlSpider):
    name = 'itao_spider_demand'
    allowed_domains = ['itaomiao.com']
    start_urls = ['http://www.itaomiao.com/purchases/purchaseList.itm']
    rules = (
        Rule(LinkExtractor(allow=('purchaseInfo\.itm')), callback='parse_item')
    )

    def parse_item(self):
        pass

    def parse(self, response):
        titles = response.xpath('')
