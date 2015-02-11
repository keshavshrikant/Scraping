# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    shirts = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()


class ColorItem(scrapy.Item):
    color = scrapy.Field()
    im_link = scrapy.Field()