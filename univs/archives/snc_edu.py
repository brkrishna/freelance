# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         snc_edu
# Purpose:      St. Norbert College
#
# Author:       Ramakrishna
#
# Dated:        07/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread

#socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
#socket.socket = socks.socksocket

url = 'http://www.snc.edu/cgi-bin/people/search.cgi'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}
#service_args = ['--proxy=127.0.0.1:9150','--proxy-type=socks5',]

def search(term):
	try:
		server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
		dc = DesiredCapabilities.HTMLUNIT
		d = webdriver.Remote(server_url, dc)

		d.get(url)
		d.find_element_by_name('str').clear()
		d.find_element_by_name('str').send_keys(term.replace("\n", ""))
		d.find_element_by_name('sbutton').click()

		tree = html.fromstring(d.page_source.encode("utf-8"))

		trs = tree.xpath("//table[@style='border-collapse: collapse']//tr")

		count = len(trs)
		records = []
		for i in range(3, count):
			rec = "$$$".join(trs[i].xpath("./td[1]//text()[normalize-space()]")).replace("\r\n", "").replace("  ", "").strip()
			if 'Student' not in rec:
				continue

			row = OrderedDict()
			try:
				row['name'] = rec[:rec.find("Student")].replace("$$$", "").strip()
			except:
				continue
			try:
				row['email'] = rec[rec.find("Student$$$")+10:].replace("$$$", "")
			except:
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('snc_edu.csv')
			with open('snc_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('snc_terms', 'a') as f:
			f.write(term + "\n")

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None
	finally:
		if d:
			d = None

class Worker(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			term = self.queue.get()
			search(term)
			self.queue.task_done()
def main():
	try:
		terms = set(open('terms.txt').readlines())
		if os.path.isfile('snc_terms'):
			finished_terms = set(open('snc_terms').readlines())
			terms -= finished_terms

		terms = list(terms)

		queue = Queue()

		for x in range(16):
			worker = Worker(queue)
			worker.daemon = True
			worker.start()

		terms_count = len(terms)
		for i in range(0, terms_count):
			queue.put(terms[i])

		queue.join()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

