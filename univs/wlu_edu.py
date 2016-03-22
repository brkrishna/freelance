# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         baker_edu
# Purpose:      Washington and Lee University
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
import os, csv, string
from lxml import html
from collections import OrderedDict
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = 'https://managementtools3.wlu.edu/Directory/'

def main():
	try:
		d = webdriver.Firefox()
		d.get(url)
		d.find_element_by_id('ApplicationContentPlaceHolder_SearchPeopleCheckBoxList_1').click()

		terms = list(string.ascii_lowercase)

		if os.path.isfile('wlu_terms'):
			finished_terms = set(open('wlu_terms').readlines())
			terms -= finished_terms

		terms_count = len(terms)

		for i in range(0, terms_count):

			d.find_element_by_id('ApplicationContentPlaceHolder_SearchPeopleTextBox').clear()
			d.find_element_by_id('ApplicationContentPlaceHolder_SearchPeopleTextBox').send_keys('%' + terms[i] + '%')
			d.find_element_by_id('ApplicationContentPlaceHolder_SearchPeopleButton').click()

			tree = html.fromstring(d.page_source)
			lis = tree.xpath("//li[@class='item' or @class='altrow item']")

			records = []
			for l in lis:
				row = OrderedDict()
				try:
					row['name'] = l.xpath("div[@class='firstcolumn']/b/text()")[0].strip()
				except:
					continue
				try:
					row['year'] = l.xpath("div[@class='firstcolumn']/text()")[0].strip()
				except:
					row['year'] = ''
					pass
				try:
					row['email'] = l.xpath("div[@class='secondcolumn']/a/text()")[0].strip()
				except:
					pass

				records.append(row)

			if len(records) > 0:
				file_exists = os.path.isfile('wlu_edu.csv')
				with open('wlu_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
					fp = csv.DictWriter(outfile, records[0].keys())
					if file_exists == False:
						fp.writeheader()
					fp.writerows(records)

			with open('wlu_terms', 'a') as f:
				f.write(terms[i] + "\n")

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None

	finally:
		if d != None:
			d.close()

if __name__ == '__main__':
	main()

