# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         xing
# Purpose:      Parse xing in given a list of companies and write users to a csv file
#
# Author:       Ramakrishna
#
# Created:      15/Feb/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver # - Can leverage Firefox / PhantomJS
from selenium.webdriver.common.keys import Keys #Used to simulate user typing in search box
from bs4 import BeautifulSoup #Using BS4 instead of lxml - customer is king :-)
import time, random, os, re #time - for delay to allow pages to load, random - to generate random wait time,
                        #os - get Operating system handle, re - regular expressions to read amounts from text
import html #clean up special characters

BASE_URL = 'http://www.xing.com'
USER_ID = ''
PASSWD = ''
MIN_WAIT = 3
MAX_WAIT = 6

def main():
    d = None
    try:

        companies = set(open('companies').readlines())
        if os.path.isfile('companies_done'):
            finished_companies = set(open('companies_done').readlines())
            companies -= finished_companies

        d = webdriver.Firefox()
        d.get(BASE_URL)
        os.system("pause")
        '''
        
        d.find_element_by_class_name('login-dropdown').click()

        d.find_element_by_name('login_form[username]').send_keys(USER_ID)
        d.find_element_by_id('login_form[password]').send_keys(PASSWD)
        d.find_element_by_name('submit').click()
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))

        '''
        for company in companies:
            try:
                d.find_element_by_name('keywords').clear()
                d.find_element_by_name('keywords').send_keys(company.replace("\n",""))
                d.find_element_by_tag_name('button').click()
                time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                #os.system("pause")
                tree = BeautifulSoup(d.page_source, "html.parser") #the default parser
                #Loop through for all pages as long as you have records
                records = []
                while tree != None:
                    time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                    user_details = tree.find_all('div', {'class':'bd'})
                    for user in user_details:
                        name = title = org = public_url = ''
                        row = {}
                        try:
                            name = '"' + "{0}".format(user.find('a', {'class':'name-page-link'}).text.encode('ascii','ignore').decode('utf-8')) + '"'
                        except:
                            continue #We cannot do anything without name, so move on to next record
                        try:
                            public_url = '"' + BASE_URL + user.find('a', {'class':'name-page-link'}).get('href') + '"'
                        except:
                            continue #We cannot do anything without name, so move on to next record
                        try:
                            org = '"' + "{0}".format(user.find('div', {'class':'company-name'}).text.encode('ascii','ignore').decode('utf-8')).strip().replace("\n", "") + '"'
                        except:
                            pass
                        try:
                            title = '"' + "{0}".format(user.find('div', {'class':'occupation-title'}).text.encode('ascii','ignore').decode('utf-8')).strip().replace("\n", "") + '"'
                        except:
                            pass

                        records.append(name + "," + title + "," + org + "," + public_url +  "\n")

                    tree = None
                    try:
                        next_page = d.find_element_by_class_name('foundation-icon-shape-arrow-right')
                        if next_page.get_attribute('href') != None:
                            next_page.click()
                            time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                            tree = BeautifulSoup(d.page_source, "html.parser")
                        else:
                            tree = None
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
                            f.write("name, title, org, public_url" + "\n")
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
