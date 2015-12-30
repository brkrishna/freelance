Overview
========

This Python script takes the site directory of amazon site as input and scrapes all the sub categories in it. 

Next, there is a routine which picks these urls and scrapes product review links from each product in a category, scrolling through the pagers where applicable

The last routine takes these review urls, navigates through the pagers in product reviews and scrapes the results

Features
========

At each stage, be it subcategories, review urls or actual reviews, the data is persisted into csv file 
Processing flags to ensure that we resume from where we left in case of any failure 

System Requirements
===================

Tested on Win7 64 bit with python 2.7.10, along with the following python plugins
scrapy - for spider scraping routines
pandas - for reading and writing from flat files

Files in package
================

amazon/process/
	categories - List of categories from the site directory - csv with url and status
	catg_out.txt - log file which recorded previous output, can be safely deleted
	convert_json.py - python script to convert csv file to json format
	items.py - classes to map the data structures of parsing elements
	pipelines.py - scrapy system file
	review_urls - staging file which holds review urls against each category - csv with url and status
	reviews - csv delimited reviews file that gets generated 
	rvw_urls_out.txt - log file which recorded previous output, can be safely deleted	
	rvws_out.txt - log file which recorded previous output, can be safely deleted
	settings.py - scrapy system file
amazon/process/spiders
	catgs_spider.py - python script file to crawl and scrape categories
	review_urls_spider.py - python script file to crawl and scrape review urls
	reviews_spider.py - python script file to scrape reviews

How to use this package
=====================

from command prompt navigate to amazon/process directory. This is the root directory of the project. 
If you are running from scratch, please delete categories, review_urls, reviews and *_out.txt files.  
To fetch categories 
At the command prompt type : scrapy crawl catg 

To fetch review_urls type: scrapy crawl review_urls
To fetch reviews type: scrapy crawl reviews

Finally, type: python convert_json 
This will convert the csv file generated to json format

As you can see from the log files, it took about 
6 seconds to get all categories
7:31 seconds to get 1600 review urls from 10 categories
~ 3 hours to get 223,625 reviews from above 1600 review urls

