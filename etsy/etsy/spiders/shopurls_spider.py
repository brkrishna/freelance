# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.selector import HtmlXPathSelector

class ShopUrlsSpider(scrapy.Spider):
	name = "shopurls"
	allowed_domains = ["www.etsy.com"]        
	start_urls = ["https://www.etsy.com/in-en/search/jewelry"]
	
	def parse(self, response):
		yield scrapy.Request(response.url, self.shop_urls)

	def shop_urls(self, response):
		urls = response.xpath("//a[@class='card-shop-name card-meta-row-item text-gray-lighter text-truncate overflow-hidden']")
		with open('urls', 'a') as sink:
			for url in urls:
				sink.write(url.xpath("@href").extract()[0].encode('utf-8') + '\n')

		next_page_url = response.xpath('//a[position() = last() and @class="btn btn-secondary btn-group-item btn-icon "]/@href').extract()
		if next_page_url:
			yield scrapy.Request(next_page_url[0], self.shop_urls)
