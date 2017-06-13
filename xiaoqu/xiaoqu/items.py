# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoquItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address= scrapy.Field()
    region_name= scrapy.Field()
    region_id= scrapy.Field()
    street_name= scrapy.Field()
    street_id= scrapy.Field()
    id=scrapy.Field()
    city=scrapy.Field()
    pass
