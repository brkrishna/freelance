# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         linkedin
# Purpose:      Parse linked in given a list of companies and write users to a csv file
#
# Author:       Ramakrishna
#
# Created:      21/Jan/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver # - Can leverage Firefox / PhantomJS
from selenium.webdriver.common.keys import Keys #Used to simulate user typing in search box
#from lxml import html # to parse members list from html page
from bs4 import BeautifulSoup #Using BS4 instead of lxml - customer is king :-)
import configparser #To read settings for the program
import time, random, os, re #time - for delay to allow pages to load, random - to generate random wait time,
                        #os - get Operating system handle, re - regular expressions to read amounts from text

'''
Logging temporarily for debug purposes, can be removed once the script is stable or integrated with other code
'''
import logging

# create logger
logger = logging.getLogger('linkedin_scraper')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('linkedin.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)


SECTION ='SETUP'

def main():
    d = None
    try:
        
        Config = configparser.ConfigParser()
        Config.read('settings.ini')
        settings = {}
        options = Config[SECTION]
        for option in options:
            try:
                settings[option] = Config[SECTION][option]
            except:
                settings[option] = None
                
        min_wait = int(settings['min_wait'])
        max_wait = int(settings['max_wait'])
                
        logger.debug("Finished reading config settings...")
        
        companies = set(open('companies').readlines())
        if os.path.isfile('companies_done'):
            finished_companies = set(open('companies_done').readlines())
            companies -= finished_companies
        
        logger.debug("Filtered companies to be processed...")
        
        d = webdriver.Firefox()
        
        d.get(settings['base_url'])
        
        d.find_element_by_id('login-email').send_keys(settings['user_id'])
        d.find_element_by_id('login-password').send_keys(settings['passwd'])
        logger.debug("Logged in...")
        d.find_element_by_name('submit').click()
        time.sleep(random.randint(min_wait,max_wait))
        
        d.find_element_by_id('main-search-box').clear()
        for company in companies:
            try:
                logger.debug("Searching for company - " + company.replace("\n",""))
                d.find_element_by_id('main-search-box').clear()
                d.find_element_by_id('main-search-box').send_keys(company.replace("\n",""))
                d.find_element_by_name('search').click()
                time.sleep(random.randint(min_wait,max_wait))
                
                #tree = html.fromstring(d.page_source)
                tree = BeautifulSoup(d.page_source, "html.parser") #the default parser
                #Loop through for all pages as long as you have records
                records = []
                counter = 4
                while tree != None:
                    #Loop only for 3 pages, to test
                    counter -= 1
                    if counter == 0:
                        tree = None
                        continue
                    
                    #user_details = tree.xpath("//div[@class='bd']")
                    user_details = tree.find_all('div', {'class':'bd'})
                    logger.debug("Found - " + str(len(user_details)) + " records...")
                    for user in user_details:
                        name = role = org = location = industry = ''
                        row = {}
                        try:
                            #temp = user.xpath("h3//text()")
                            #name = '"' + temp[:1][0] + '"'
                            name = user.find('h3').find('a').text
                            #TODO - Can derive the level of connection with rest of the temp value
                        except:
                            continue #We cannot do anything without name, so move on to next record
                        try:
                            #temp = user.xpath("div[@class='description']//text()")
                            temp = user.find('div', {'class':'description'}).text
                            #role = '"' + temp[:1][0].replace('at', "").strip() + '"'
                            #org = '"' + temp[1:][0].strip() + '"'
                            role = '"' + temp[:temp.find("at")].strip() + '"'
                            org = '"' + temp[temp.find("at")+2:].strip() + '"'
                        except:
                            #pass
                            continue #We cannot do anything without role, so move on to next record
                        try:
                            #temp = user.xpath("dl[@class='demographic']//text()")
                            #location = '"' + temp[1] + '"'
                            location = '"' + user.find('dl',{'class':'demographic'}).find_all('dd')[0].text
                            #industry = '"' + temp[3] + '"'
                            industry = '"' + user.find('dl',{'class':'demographic'}).find_all('dd')[1].text
                        except:
                            pass
                        records.append(name + "," + role + "," + org + "," + location + "," + industry + "\n")
                    try:
                        logger.debug("Parsing members for company - " + company.replace("\n",""))
                        next_page = d.find_element_by_partial_link_text('Next')
                        next_page.click()
                        time.sleep(random.randint(min_wait,max_wait))
                        tree = html.fromstring(d.page_source)
                    except:
                        tree = None
                        pass
                    
                file_name = company.replace("\n","").replace(" ", "_").lower()
                wrote_header = False
                
                if os.path.isfile(file_name + '.csv'): #file exists don't write header
                    wrote_header = True
                    
                with open(file_name + '.csv', 'a') as f:
                    for record in records:
                        if wrote_header == False:
                            f.write("name, role, org, location, industry" + "\n")
                            wrote_header = True
                        f.write(record)

            except Exception as e:
                print(e.__doc__)
                print(e.args)
            finally:
                with open('companies_done','a') as f:
                    f.write(company)
                
    except Exception as e:
        print(e.__doc__)
        print(e.args)
    finally:
        d.quit() if d != None else None

if __name__ == '__main__':
    main()
