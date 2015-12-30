# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.selector import HtmlXPathSelector
from process.items import CatgUrl
import pandas as pd
from urlparse import urlparse

#Constants
BASE_URL = 'http://www.amazon.cn'
START_URL_SUFFIX = "/gp/site-directory/"

file_suffix = ''
allowed_domains = ["http://www.amazon.cn", "http://www.amazon.es"]

class CatgSpider(scrapy.Spider):
    try:
        name = "catg"
        def __init__(self, *args, **kwargs):
            super(CatgSpider, self).__init__(*args, **kwargs)
            self.start_urls = [kwargs.get('start_url') + START_URL_SUFFIX]

        def parse(self, response):
            try:
                global allowed_domains
                parsed_uri = urlparse(response.url)
                domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)

                #Ensure that this domain is handled, otherwise quit
                if domain not in allowed_domains:
                    print response.url + ' is not a domain that is programmed for parsing...'
                    exit

                if domain != None:
                    file_suffix = domain[domain.rfind('.') + 1 : ]

                if domain == 'http://www.amazon.cn':
                    urls = response.xpath("//a[@class='nav_a a-link-normal a-color-base']")
                elif domain == 'http://www.amazon.es':
                    urls = response.xpath("//a[@class='nav_a']")
                else:
                    urls = ''

                url_links = []
                for sel in urls:
                    item = CatgUrl()
                    url = sel.xpath("@href").extract()[0].encode('utf-8')
                    item['link'] = url if url.startswith('http://') else domain + url

                    #Ignore links to other domains
                    if domain not in item['link']:
                        continue

                    url_links.append(item['link'])

                if len(url_links) > 0:
                    df = pd.DataFrame(data = url_links, columns=['link'])
                    df.to_csv('catg_' + file_suffix, mode='a', header=False, index=False)

            except Exception as e:
                print(e.__doc__)
                print(e.args)

    except Exception as e:
        print(e.__doc__)
        print(e.args)
