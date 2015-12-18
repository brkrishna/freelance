# -- coding: utf-8 --
__author__ = 'Ramakrishna'

# Purpose: To fetch address details from addresses.com
# Author: Ramakrishna
# Version: 15/Oct/2015 - Initial version

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from lxml import html
import sqlite3, time, re

BASE_URL = 'http://www.addresses.com'

def main():
    try:
        conn = sqlite3.connect("addresses_com.db3")
        cur = conn.cursor()
        cur.execute("select id, name, region, state from businesses where address is null order by id")
        search_terms = cur.fetchall()
        
        #d = webdriver.PhantomJS('phantomjs.exe')
        d = webdriver.Firefox()
        try:
            for s in search_terms:
                
                id = 0
                phone = address = city = zip = ''

                d.get(BASE_URL)
                id = s[0]
                d.find_element_by_id('Business_Name').clear()
                d.find_element_by_id('Business_Name').send_keys(s[1])
                d.find_element_by_id('Business_Loc').clear()
                d.find_element_by_id('Business_Loc').send_keys(s[2] + ', ' + s[3])
                d.find_element_by_css_selector('div.form_inner:nth-child(2) > div:nth-child(3) > button:nth-child(2)').click()
                try:
                    time.sleep(20)
                    tree = html.fromstring(d.page_source)
                    
                    try:
                        records = []
                        tables = tree.xpath("//table[@class='yp_multi_listing']")
                        for t in tables:
                        	records.append(t.xpath("*//text()[normalize-space()]"))
                        
                        if len(records) > 0:
                            rec_count = len(records)
                            for i in range(0, rec_count):
                                if s[1].lower() in records[i][0].lower():
                                    address = records[i][1].strip()
                                    city = records[i][2][:records[i][2].find(',',1)].strip()
                                    zipcd = re.search(r'\d{5}', records[i][2])
                                    if zipcd:
                                        zip = zipcd.group().strip()
                                    phone = records[i][3].strip()

                    except IndexError as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                        
                    if address != '':
                        sql = "update businesses set phone = ?, address = ?, city = ?, zip = ? where id = ?"
                        cur.execute(sql, (phone,address,city,zip,id,))
                    else:
                        sql = "update businesses set address = ? where id = ?"
                        cur.execute(sql, ('NA',id,))
                    conn.commit()

                except NoSuchElementException as e:
                    print(e.__doc__)
                    print(e.args)
                
        except NoSuchElementException as e:
            print(e.__doc__)
            print(e.args)
            exit
        
    except Exception as e:
        print(e.__doc__)
        print(e.args)
    finally:
        conn.commit()
        d.quit()
    
if __name__ == '__main__':
    main()

        
    