from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import CrawelsDemandItem

class ItaoDemand(CrawlSpider):
    name = 'itaoDemand'
    allowed_domains = ['itaomiao.com']
    start_urls = ['http://www.itaomiao.com/purchases/purchaseList.itm']
    rules = (
        Rule(LinkExtractor(allow=('purchaseInfo\.itm')), callback='parse_item'),
    )

    def parse_item(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = CrawelsDemandItem()
        item['from_url'] = response.url
        item['company'] = response.xpath('//i/a/text()').get()
        item['start_time'] = response.xpath('//p[@class="pc_date"]/span/text()').re(r'\d\d\d\d-\d\d-\d\d')
        item['stop_time'] = response.xpath('//p[@class="pc_date"]/span/span/text()').get()
        item['place'] = response.xpath('//span[@class="pc_addr"]/i/text()').get()
        item['kinds'] = response.xpath('//div[@class="p_plantsList"]//a/text()').get()
        item['other_infor'] = response.xpath('//p[@class="moreRequire"]/text()').get()
        yield item


