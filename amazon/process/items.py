# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CatgUrl(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    pass

class RvwUrl(scrapy.Item):
    link = scrapy.Field()
    pass

class Reviews(scrapy.Item):
    product = scrapy.Field()
    star_rating = scrapy.Field()
    posted = scrapy.Field()
    body = scrapy.Field()
    pass
