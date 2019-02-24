from scrapy.spiders import Spider
from scrapy import FormRequest,Request
from ..items import CrawelsDemandItem
import json

class PurchaseDemand(Spider):
    name = 'itao_purchase_demands'
    allowed_domains = ['itaomiao.com']

    def start_requests(self):
        url = 'http://www.itaomiao.com/purchases/getIndexPurchaseList.json'
        for page in range(1,51):
            form_data = {'page':str(page),'rows':'15'}
            yield FormRequest(url=url,formdata=form_data,callback=self.parse_json)


    def parse_json(self,response):
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


