# _*_ coding:utf-8 _*_
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
import html #clean up special characters

BASE_URL = 'http://www.linkedin.com'
DOMAIN_URL = 'https://www.linkedin.com'
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

        d.find_element_by_id('login-email').send_keys(USER_ID)
        d.find_element_by_id('login-password').send_keys(PASSWD)
        d.find_element_by_name('submit').click()
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))

        d.find_element_by_id('main-search-box').click()
        main_window = d.current_window_handle

        d.find_element_by_partial_link_text('Go to Recruiter').click()
        time.sleep(10)
        handles = d.window_handles
        d.switch_to_window(handles.pop())
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
        d.find_element_by_id('search-link').click()
        time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
        d.find_element_by_id('search-input-company').clear()

        for company in companies:
            try:
                d.find_element_by_id('search-input-company').clear()
                d.find_element_by_id('search-input-company').send_keys(company.replace("\n",""))
                d.find_element_by_class_name('search-overlay-submit').click()
                time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                os.system("pause")
                tree = BeautifulSoup(d.page_source, "html.parser") #the default parser
                #Loop through for all pages as long as you have records
                records = []
                while tree != None:
                    time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
                    user_details = tree.find_all('div', {'class':'bd'})
                    for user in user_details:
                        name = role = org = location = industry = public_url = ''
                        row = {}
                        try:
                            name = '"' + "{0}".format(user.find('h3').find('a').text.encode('ascii','ignore').decode('utf-8')) + '"'
                            #TODO - Can derive the level of connection with rest of the temp value
                        except:
                            continue #We cannot do anything without name, so move on to next record
                        try:
                            temp = "{0}".format(user.find('p', {'class':'headline'}).text.encode('ascii','ignore').decode('utf-8'))
                            try:
                                output = re.search(r'\b(at)\b', temp)
                                if output.start() > 0:
                                    role = '"' + temp[:output.start()].strip() + '"'
                                    org = '"' + temp[output.start()+2:].strip() + '"'
                            except AttributeError:
                                role = '"' + temp.strip() + '"'
                                pass
                        except:
                            continue #We cannot do anything without role, so move on to next record
                        try:
                            location = '"' + "{0}".format(user.find('dl',{'class':'demographic'}).find_all('dd')[0].text.encode('ascii','ignore').decode('utf-8')) + '"'
                            industry = '"' + "{0}".format(user.find('dl',{'class':'demographic'}).find_all('dd')[1].text.encode('ascii','ignore').decode('utf-8')) + '"'
                        except:
                            pass
                        try:
                            public_url = '"' + DOMAIN_URL + user.find('a', {'class':'title'}).get('href') + '"'
                        except:
                            pass

                        records.append(name + "," + role + "," + org + "," + location + "," + industry + "," + public_url +  "\n")
                    tree = None
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
                            f.write("name, role, org, location, industry, public_url" + "\n")
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
