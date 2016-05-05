# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:        parser
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     08/09/2015
# Copyright:   (c) Ramakrishna 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict

BASE_URL = 'https://usatrade.census.gov/'

def main():
	d = None
	try:
		d = webdriver.Firefox()
		d.get(BASE_URL)
		time.sleep(3)

		d.find_element_by_class_name('uto_button').click()
		time.sleep(3)
		d.find_element_by_id('struserid').send_keys('8GCG9XW')
		d.find_element_by_id('pwdfld').send_keys('Sanjana@1234')
		d.find_element_by_id('buttonid').click()
		time.sleep(3)
		d.find_element_by_css_selector('#Table2 > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)').click()

		d.find_element_by_partial_link_text('Measures').click()
		boxes = d.find_elements_by_class_name('rtChk')
		for box in boxes:
			if box.is_selected():
				continue
			else:
				box.click()

		d.find_element_by_partial_link_text('Commodity').click()
		d.find_element_by_css_selector('#ctl00_MainContent_RadMembersTree > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > label:nth-child(3) > input:nth-child(1)').click()
		d.find_element_by_partial_link_text('Country').click()
		d.find_element_by_id('Level1ClearImage').click()

		chks = d.find_elements_by_class_name('rtLI')
		for chk in chks:
			if chk.text == 'Afghanistan':
				chk.find_element_by_tag_name('input').click()
				break
			else:
				continue

		d.find_element_by_link_text('Report').click()

		soup = BeautifulSoup(d.page_source, parse_only=SoupStrainer('body'))
		if soup:
			row = OrderedDict()
			for th in soup.findAll("th", {"headers":"Col5"}):
				try:
					row[th.get('id')] = row[th.text.strip()]
				except:
					break

				#TODO Improvise further with Col4 for next set of keys and values
			try:
				row['']
				print(soup.find('th', {'id':'C00'}).text)
			except:
				pass
			try:
				print(soup.find('th', {'id':'C00'}).text)
			except:
				pass
	except Exception as e:
		print(e.__doc__)
		print(e.args)

	finally:
		if d:
			d.quit()
			d = None

if __name__ == '__main__':
	main()

