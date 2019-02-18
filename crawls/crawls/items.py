# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawelsDemandItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    start_time = scrapy.Field()
    stop_time = scrapy.Field()
    place = scrapy.Field()
    kinds = scrapy.Field()
    from_url = scrapy.Field()
    other_infor = scrapy.Field()

class CrawelsPlantsItem(scrapy.Item):
    name = scrapy.Field()
    other_name = scrapy.Field()
    area = scrapy.Field()
    post_time = scrapy.Field()
    total_amount = scrapy.Field()
    start_sell_num = scrapy.Field()
    price = scrapy.Field()
    characters = scrapy.Field()
    pictures = scrapy.Field()
    from_url = scrapy.Field()
