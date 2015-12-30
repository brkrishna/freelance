# -- coding: utf-8 --

import scrapy, os
from scrapy.selector import HtmlXPathSelector
from process.items import RvwUrl
import pandas as pd

#Constants
BASE_URL = 'http://www.amazon.cn'

class RvwUrlSpider(scrapy.Spider):
	name = "review_urls"
	allowed_domains = ["amazon.cn"]
	start_urls = [BASE_URL]

	def parse(self, response):
		review_urls = set(open('categories').readlines())

		if os.path.isfile('categories_done'):
			finished_review_urls = set(open('categories_done').readlines())
			review_urls -= finished_review_urls

		for url in review_urls:
			yield scrapy.Request(url.strip(), callback=self.get_review_urls)

		def get_review_urls(self, response):
			urls = response.meta.get('redirect_urls', [response.url])
			nodes = response.xpath('//*[@data-asin]/@data-asin').extract()
			with open('review_urls', 'a') as sink:
				for node in nodes:
					sink.write("%s/gp/product-reviews/%s\n" % (BASE_URL, node))

			more_buttons = response.xpath('//a[contains(@class, "dv-view-all")]/@href').extract()
			if more_buttons:
				for button in more_buttons:
					yield scrapy.Request(BASE_URL + button, self.get_review_urls)

			next_links = response.xpath('//a[@id="pagnNextLink"]/@href').extract()
			if next_links:
				for link in next_links:
					yield scrapy.Request(BASE_URL + link, self.get_review_urls)

			#Push the url to done queue
			df_catg_done = pd.DataFrame(data = urls, columns=['link'])
			df_catg_done.to_csv('categories_done', mode='a', header=False, index=False)
