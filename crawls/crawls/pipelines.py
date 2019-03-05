# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Request
from urllib.request import urlopen



class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.download_pic(item['pictures'],item['barcode2D'])
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


    def download_pic(self,urls,code):

        for index,url in enumerate(urls):
            print('正在下载图片: {}'.format(code))
            pic_name = '{0}/pic_{1}_{2}.{3}'.format('../pictures',code,index,'jpg')
            content = urlopen(url).read()
            with open(pic_name, 'wb') as f:
                f.write(content)
                f.close()


# class ImagesPipeline(ImagesPipeline):
#
#     def get_media_requests(self,item,info):
#         for image_url in item['pictures']:
#             yield Request(image_url)
#
#     def item_completed(self, results, item, info):
