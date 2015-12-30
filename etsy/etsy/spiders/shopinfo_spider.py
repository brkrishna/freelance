# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.selector import HtmlXPathSelector
import os.path
from etsy.items import ShopData

class ShopInfoSpider(scrapy.Spider):
	name = "shopinfo"
	allowed_domains = ["www.etsy.com"]        
	start_urls = ["https://www.etsy.com/in-en/search/jewelry"]
	
	def parse(self, response):
		review_urls = set(open('urls').readlines())
		len(review_urls)
		if os.path.isfile('urls_done'):
			finished_review_urls = set(open('urls_done').readlines())
			review_urls -= finished_review_urls
		len(review_urls)
		for url in review_urls:
			yield scrapy.Request(url.strip(), callback=self.shop_urls)
		
	def shop_urls(self, response):
		url = response.meta.get('redirect_urls', response.url)	
		
		details = response.xpath("//div[@class='secondary v2']")
		if details:
			#item = ShopData()
			item = {}
			section_data = ''
			item['name'] = details.xpath("//li[@class='shopname']/a/text()").extract()[0].strip()
			item['join_date'] = str(details.xpath("//div[@class='join-date']/text()")[0].extract()).strip().replace("\n", "")
			item['sales'] = str(details.xpath("//li[@class='sales ']/a/text()")[0].extract()).strip()
			item['reviews'] = details.xpath("//span[@class='review-rating-count']/text()")[0].extract().strip()
			item['rating'] = details.xpath("//meta[@itemprop='rating']/text()")[0].extract().strip()
			item['admirers'] = str(details.xpath("//li[@class='admirers']/a/text()")[0].extract()).strip().replace("\n", "")
			item['owner'] = str(details.xpath("//a[@class='username']/text()")[0].extract()).strip()
			item['location'] = str(details.xpath("//div[@class='location']/text()").extract()[0]).strip()
			item['url'] = url
			
			outline = item['name'] + '$$$' + item['join_date'] + '$$$' + item['sales'] + '$$$' + item['reviews']
			outline += '$$$' + item['rating'] + '$$$' + item['admirers'] + '$$$' + item['owner'] + '$$$' + item['location']
			
			open('urls_done', 'a').write(url + '\n')
			with open('shopinfo', 'a') as sink:
				sink.write(outline + "\n")
			#return item
			
		
