
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
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from lxml import html
import re, time, os, csv

BASE_URL = 'http://www.linkedin.com'

def main():
    d = webdriver.Firefox()
    try:
d.find_element_by_id('login-email').send_keys('brkrishna@gmail.com')
d.find_element_by_id('login-password').send_keys('parimala32')
        d.find_element_by_name('submit').click()
        d.find_element_by_id('main-search-box').clear()
d.find_element_by_id('main-search-box').send_keys('Magnaquest Technologies')
        d.find_element_by_name('search').click()

        tree = html.fromstring(d.page_source)
        users = tree.xpath("//a[@class='title main-headline']/text()")

    except Exception as e:
        print(e.__doc__)
        print(e.args)
    finally:
        d.quit()


if __name__ == '__main__':
    main()
