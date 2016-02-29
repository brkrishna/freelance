# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         albonazionalegestoriambientali_it
# Purpose:      Parse linked in given a list of companies and write users to a csv file
#
# Author:       Ramakrishna
#
# Created:      21/Feb/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from lxml import html
import time, random, os, re
import sqlite3

MIN_WAIT = 1
MAX_WAIT = 3
URL = 'http://www.albonazionalegestoriambientali.it/ElenchiIscritti.aspx'

SECTIONS = ['13', '21', '17', '18', '15', '8', '6', '12', '7', '3', '11', '14', '1', '16', '20', '19', '9', '4', '10', '2', '5']

def main():
    d = conn = None
    try:
        server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
        dc = DesiredCapabilities.HTMLUNIT

        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        d = webdriver.Remote(server_url, dc)
        #d = webdriver.Firefox()
        d.get(URL)
        for section in SECTIONS:
            try:
                d.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlSezioni"]/option[@value="' + section + '"]').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                print("section - " +  str(section))    
                d.find_element_by_xpath('//*[@id="risultatiPerPagina"]/option[@value="100"]').click()
                d.find_element_by_id('btnCerca').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))

                tree = html.fromstring(d.page_source.encode('utf-8'))
                impresa_list = tree.xpath("//input[@value='Dettagli']/@onclick")
                while len(impresa_list) > 0:

                    impresas = []
                    for impresa in impresa_list:
                        temp = re.search("[0-9]{1,8}", impresa).group()
                        cur.execute("insert or ignore into impresas (impresa) values (?)", (temp,))

                    try:
                        next_page = d.find_element_by_xpath("//div[@class='pagerPageSelected']/following-sibling::div[@class='pagerPage']")
                        print("next page - " + str(next_page.text))
                        next_page.click()
                        time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                        tree = html.fromstring(d.page_source.encode('utf-8'))
                        impresa_list = tree.xpath("//input[@value='Dettagli']/@onclick")
                    except:
                        break

            except Exception as e:
                print(e.__doc__)
                print(e.args)
                continue

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        if d != None:
        	d.quit()
        	d = None
        if conn != None:
        	conn.commit()
        	conn = None

if __name__ == '__main__':
	main()