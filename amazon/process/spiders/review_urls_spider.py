# -- coding: utf-8 --

import os.path
import re, json

import scrapy
from scrapy.selector import HtmlXPathSelector
from process.items import RvwUrl
import pandas as pd

#Constants
BASE_URL = 'http://www.amazon.cn'

class RvwSpider(scrapy.Spider):
	name = "reviews"
	allowed_domains = ["amazon.cn"]
	start_urls = ["http://www.amazon.cn"]

	def parse(self, response):

		review_urls = set(open('review_urls').readlines())

		if os.path.isfile('review_urls_done'):
			finished_review_urls = set(open('review_urls_done').readlines())
			review_urls -= finished_review_urls

		for url in review_urls:
			yield scrapy.Request(url.strip(), callback=self.get_reviews)

		def _create_review(self, helpfulness, stars, author, date, body, url):
			info_dict = {}
			if helpfulness:
				helpful_numbers = re.findall(r'\d+', helpfulness[0])
				info_dict['helpful_num'] = int(helpful_numbers[-1])
				info_dict['helpful_den'] = int(helpful_numbers[0])

				date_numbers = re.findall(r'\d+', date[0])
				info_dict['year'] = int(date_numbers[0])
				info_dict['month'] = int(date_numbers[1])
				info_dict['day'] = int(date_numbers[2])

				info_dict['stars'] = int(stars[0])
				info_dict['author'] = author[0]
				info_dict['body'] = body[0]
				info_dict['product_link'] = url
				return info_dict

		def get_reviews(self, response):
			url = response.meta.get('redirect_urls', response.url)

			reviews = response.xpath('//div[@class="a-section review"]')
			if reviews:
				review_list = []
				for review in reviews:
					helpfulness = review.xpath('.//div[@class="a-row helpful-votes-count"]/text()').extract()
					stars = review.xpath('.//i[contains(@class, "review-rating")]/span/text()').extract()
					author = review.xpath('.//a[@class="a-size-base a-link-normal author"]/text()').extract()
					date = review.xpath('.//span[@class="a-size-base a-color-secondary review-date"]/text()').extract()
					body = review.xpath('.//span[@class="a-size-base review-text"]/text()').extract()
					info_dict = self._create_review(helpfulness, stars, author, date, body, url)
					dumped_data = json.dumps(info_dict, ensure_ascii=False).encode('utf8') + '\n'
					review_list.append(dumped_data)
					
				with open('reviews', 'a') as sink:
					for review_item in review_list:
						sink.write(review_item)

				next_page_url = response.xpath('//ul[@class="a-pagination"]/li[@class="a-last"]/a/@href').extract()
				if next_page_url:
					yield scrapy.Request(BASE_URL + next_page_url[0], self.get_reviews)

				open('review_urls_done', 'a').write(url + '\n')
