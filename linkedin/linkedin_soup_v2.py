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
from bs4 import BeautifulSoup #Using BS4 instead of lxml - customer is king :-)
import time, random, os, re #time - for delay to allow pages to load, random - to generate random wait time,
                        #os - get Operating system handle, re - regular expressions to read amounts from text

BASE_URL = 'http://linkedin.com'
USER_ID = ''
PASSWD = ''
MIN_WAIT = 2
MAX_WAIT = 5

def main():
    d = None
    try:
        
        companies = set(open('companies').readlines())
        if os.path.isfile('companies_done'):
            finished_companies = set(open('companies_done').readlines())
            companies -= finished_companies
        
        d = webdriver.Firefox()
        
        d.get(BASE_URL)
        
        d.find_element_by_id('login-email').send_keys(USER_ID)
        d.find_element_by_id('login-password').send_keys(PASSWD)
        d.find_element_by_name('submit').click()
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
        
        d.find_element_by_id('main-search-box').clear()
        for company in companies:
            try:
                d.find_element_by_id('main-search-box').clear()
                d.find_element_by_id('main-search-box').send_keys(company.replace("\n",""))
                d.find_element_by_name('search').click()
                time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                
                tree = BeautifulSoup(d.page_source, "html.parser") #the default parser
                #Loop through for all pages as long as you have records
                records = []
                while tree != None:
                    
                    user_details = tree.find_all('div', {'class':'bd'})
                    for user in user_details:
                        name = role = org = location = industry = ''
                        row = {}
                        try:
                            name = user.find('h3').find('a').text
                            #TODO - Can derive the level of connection with rest of the temp value
                        except:
                            continue #We cannot do anything without name, so move on to next record
                        try:
                            temp = user.find('div', {'class':'description'}).text
                            role = '"' + temp[:temp.find("at")].strip() + '"'
                            org = '"' + temp[temp.find("at")+2:].strip() + '"'
                        except:
                            continue #We cannot do anything without role, so move on to next record
                        try:
                            location = '"' + user.find('dl',{'class':'demographic'}).find_all('dd')[0].text
                            industry = '"' + user.find('dl',{'class':'demographic'}).find_all('dd')[1].text
                        except:
                            pass
                        records.append(name + "," + role + "," + org + "," + location + "," + industry + "\n")
                    try:
                        next_page = d.find_element_by_partial_link_text('Next')
                        next_page.click()
                        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                        tree = BeautifulSoup(d.page_source, "html.parser")
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
