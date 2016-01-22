# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:        offbeatbride
# Purpose:     Pick all category links and browse through vendors listing to parse data
# Author:      Ramakrishna
#
# Created:     20/Jan/2016
# Copyright:   (c) Ramakrishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time, random, re, csv #time - for delay to allow pages to load, random - to generate random wait time,
                        #re - regular expressions to read amounts from text
                        #csv - to store data as comma separated values
from selenium import webdriver # - Can leverage Firefox / PhantomJS
from lxml import html # to parse basket and shipping terms from html page

'''
Logging temporarily for debug purposes, can be removed once the script is stable or integrated with other code
'''
import logging

# create logger with 'spam_application'
logger = logging.getLogger('offbeatbride_scraper')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('offbeatbride.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

URL = 'http://vendors.offbeatbride.com'
MIN_WAIT = 0
MAX_WAIT = 3

def main():
    d = None
    try:
        #TODO - Can leverage firefox for full blown browser or phantomjs for headless version
        #d = webdriver.PhantomJS("..\phantomjs.exe")
        d = webdriver.Firefox()
        logger.debug(URL)
        d.get(URL)
        time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
        try:
            #Pick all categories
            tree = html.fromstring(d.page_source)
            catg_urls = tree.xpath("//div[@class='category col-xs-6 col-sm-6 col-md-3 col-lg-2']/a/@href")
            vendor_urls = []
            for catg_url in catg_urls:
                d.get(catg_url)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                tree = html.fromstring(d.page_source)
                vendor_urls += tree.xpath("//h1[@class='entry-title']/a/@href")
                break

            records = []
            for vendor_url in vendor_urls:
                d.get(vendor_url)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                tree = html.fromstring(d.page_source)
                row = {}
                try:
                    row['title'] = tree.xpath("//h1[@class='entry-title']/text()")[0]
                except IndexError:
                    continue #What will we do withtout a title, move on to the next record
                try:
                    row['address'] = ' '.join(tree.xpath("//i[@class='fa fa-fw fa-li fa-home']/parent::li//text()")).replace("\n"," ")
                except IndexError:
                    row['address'] = ''
                    pass
                try:
                    row['phone'] = tree.xpath("//i[@class='fa fa-fw fa-li fa-phone']/parent::li//text()")[0]
                except IndexError:
                    row['phone'] = ''
                    pass

                records.append(row)

            with open('offbeatbride.csv', 'a') as f:
                wrote_header = False
                for record in records:
                    if wrote_header == False:
                        w = csv.DictWriter(f, record.keys())
                        w.writeheader()
                        wrote_header = True
                    w.writerow(record)

        except Exception as e:
            print(e.__doc__)
            print(e.args)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        if d != None:
            d.quit()

if __name__ == '__main__':
    main()
