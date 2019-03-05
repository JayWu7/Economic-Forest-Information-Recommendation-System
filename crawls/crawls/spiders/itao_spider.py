from scrapy.spiders import Spider
from scrapy import FormRequest, Request
from ..items import CrawelsDemandItem,CrawelsPlantsItem
import json


class PurchaseDemand(Spider):
    name = 'itao_purchase_demands'
    allowed_domains = ['itaomiao.com']

    def start_requests(self):
        url = 'http://www.itaomiao.com/purchases/getIndexPurchaseList.json'
        for page in range(1, 51):
            form_data = {'page': str(page), 'rows': '15'}
            yield FormRequest(url=url, formdata=form_data, callback=self.parse_json)

    def parse_json(self, response):
        json_str = json.loads(response.body.decode('utf-8'))
        for info in json_str['indexPurchaseList']:
            item = CrawelsDemandItem()
            item['purchase_id'] = info['id']
            item['name'] = info['purchaseName']
            item['from_url'] = 'http://www.itaomiao.com/purchases/purchaseInfo.itm?id={id}'.format(id=info['id'])
            item['company'] = info['companyName']
            item['start_time'] = info['createDate']
            item['stop_time'] = info['endDate']
            item['place'] = info['districtName']
            item['kinds'] = info['purchasePlants']
            item['other_infor'] = info['else2']
            item['buyer'] = info['buyer']
            item['buyer_tel'] = info['buyerTel']
            yield item


class SupplyCrawl(Spider):
    name = 'itao_supply'
    allowed_domains = ['itaomiao.com']

    def start_requests(self):
        url = 'http://www.itaomiao.com/supply/findSupplyList.json'
        for i in range(1, 2):
            form_data = {'pageNo': str(i), 'rows': '20'}
            yield FormRequest(url=url, formdata=form_data, callback=self.parse_page)

    def parse_page(self, response):
        supply_list = json.loads(response.text)
        if 'supplyList' in supply_list.keys():
            for plant in supply_list.get('supplyList'):
                if 'barcode2D' in plant.keys():
                    yield Request(
                        url='http://www.itaomiao.com/supply/supplyInfo.itm?code={code}'.format(code = plant.get('barcode2D')),
                        callback=self.parse_plant)

    def parse_plant(self, response):
        item = CrawelsPlantsItem()
        item['name'] = response.xpath('//input[@id="mainVariety"]/@value').get()
        print(item)

