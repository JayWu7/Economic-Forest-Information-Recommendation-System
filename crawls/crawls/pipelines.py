# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from urllib.request import urlopen
import re
import os
from .settings import PIC_DIRECTORY

class CleanInfoPipeline():
    def process_item(self, item, spider):
        if spider.name == 'itao_supply' and item['info']:
            for index, field in enumerate(item['info']):
                if '\t' in field or '\r' in field or '\n' in field:
<<<<<<< HEAD
                    item['info'][index] = re.sub('[\t\n\r]','',field)
        #print(item['info'])
=======
                    item['info'][index] = re.sub('[\t\n\r]', '', field)
>>>>>>> origin
        return item


class DownloadPicsPipeline():
    def process_item(self, item, spider):
        if spider.name == 'itao_supply':
            self.download_pic(item['pictures'], item['barcode2D'])
        return item

    def download_pic(self, urls, code):
        dir = PIC_DIRECTORY + '/' + code
        os.mkdir(dir)
        for index, url in enumerate(urls):
            print('正在下载图片: {}'.format(code))
            pic_name = '{0}/pic_{1}.{2}'.format(dir, index, 'jpg')
            content = urlopen(url).read()
            with open(pic_name, 'wb') as f:
                f.write(content)


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
