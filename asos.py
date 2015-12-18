# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:        asos
# Purpose:     given a list of products, this script searches for them on asos.com,
#               adds the product to basket and scrapes price and shipping specifications
#               to be returned as a dictionary
# Author:      Ramakrishna
#
# Created:     18/Dec/2015
# Copyright:   (c) Ramakrishna 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time, random, re #time - for delay to allow pages to load, random - to generate random wait time,
                        #re - regular expressions to read amounts from text
from selenium import webdriver # - Can leverage Firefox / PhantomJS
from lxml import html # to parse basket and shipping terms from html page

'''
Logging temporarily for debug purposes, can be removed once the script is stable or integrated with other code
'''
import logging

# create logger with 'spam_application'
logger = logging.getLogger('asos_scraper')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('asos.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

#TODO - Can read the list of products from external file or db
PRODUCTS = ['Poker Denim Jacket Distressed Trucker Washed Grey','Ted Baker Zacks Bifold Leather Wallet',
            'ASOS Bobble Beanie in Blue Fair Isle','ASOS Wash Bag In Khaki Camouflage Print Canvas And Faux Leather']
            
#TODO - Calibrate the min and max values based on internet speeds to load the pages
URL = 'http://asos.com'
MIN_WAIT = 2
MAX_WAIT = 5

def main():
    d = None
    try:
        #TODO - Can leverage firefox for full blown browser or phantomjs for headless version
        d = webdriver.PhantomJS("..\phantomjs.exe")
        #d = webdriver.Firefox()
        for product in PRODUCTS:
            logger.debug(product)
            d.get(URL)
            time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
            try:
                #Perform search on the product name
                elem = d.find_element_by_xpath("//*[@id='txtSearch']")
                elem.clear()
                elem.send_keys(product)
                d.find_element_by_partial_link_text('Go').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                
                #Check if there is a size column that need to be checked before navigating to basket
                try:
                    d.find_element_by_xpath('//*[@id="ctl00_ContentMainPage_ctlSeparateProduct_drpdwnSize"]/option[2]').click()
                except:
                    pass
                
                #Add to basket and navigate to parse values
                d.find_element_by_partial_link_text('ADD TO BAG').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                d.find_element_by_class_name('total').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
            except Exception as e:
                print(e.__doc__)
                print(e.args)
                
            tree = html.fromstring(d.page_source)
            basket = tree.xpath("//table[@class='items basket-items']")
            if len(basket) < 1: continue # No items in basket, move to next product
            
            records = []
            
            #Shipping terms
            s_terms = tree.xpath("//select[@id='ctl00_ContentMainPage_ctlDeliveryOptionsAndTotals1_ddlDeliveryOptions']/option/text()")
            if len(s_terms) < 1: continue #Shipping terms not found, move to next product
            
            method = price = free_limit = ''
            count = len(s_terms)
            for i in range(0, count):
                line = str(s_terms[i].encode('ascii', 'ignore'))
                try:
                    method = line[:line.find("(")] if line.find("(") != -1 else line[:line.rfind(" ")]
                    numbers = re.findall('\d+\.?\d+', line)
                    
                    if len(numbers) > 1:
                        free_limit = numbers[0]
                        price = numbers[1]
                    else:
                        price = numbers[0]
                        
                    row = {}
                    row["product"] = basket[0].xpath("//p[@class='name']//text()[normalize-space()]")[0]
                    row["color"] = basket[0].xpath("//dd[@class='colour']/text()[normalize-space()]")[0]
                    row["size"] = basket[0].xpath("//dd[@class='size']/text()[normalize-space()]")[0]
                    row["item_price"] = tree.xpath("//span[@id='totalAmount']/text()")[0].encode('ascii', 'ignore')
                    row["shipping_method"] = method.strip()
                    row["free_limit"] = free_limit
                    row["price"] = price
                    records.append(row)
                    
                except Exception as e:
                    print(e.__doc__)
                    print(e.args)
                    pass
            #Let's remove this product from basket since we are done with it
            d.find_element_by_partial_link_text('EMPTY BAG').click()
            #Log the specifications
            logger.debug(records)
            
    except Exception as e:
        print(e.__doc__)
        print(e.args)
        
    finally:
        if d != None:
            d.quit()
            
if __name__ == '__main__':
    main()

