# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Url(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	link = scrapy.Field()
	pass

class ShopData(scrapy.Item):
	name = scrapy.Field()
	join_date = scrapy.Field()
	sales = scrapy.Field()
	reviews = scrapy.Field()
	admirers = scrapy.Field()
	total_items = scrapy.Field()
	sections = scrapy.Field()
	owner = scrapy.Field()
	location = scrapy.Field()
	pass
