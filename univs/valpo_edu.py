# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         astate_edu
# Purpose:      Valparaiso University
#
# Author:       Ramakrishna
#
# Dated:        12/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
#socket.socket = socks.socksocket

url = 'http://www.valpo.edu/directory/assets/includes/directory.php?requestType=searchPeople&searchTerm='
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0)',
           'Host':'www.valpo.edu',
           'Cookie':'__utma=185939886.1715528207.1457803219.1457803219.1457803219.1; __utmz=185939886.1457803219.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'en-US,en;q=0.5',
           'Connection':'keep-alive'}

def search(term):
	d = None
	try:
		#s = requests.session()
		#r = s.get(url + term.replace("\n", "") + "+", headers=headers)
		#tree = html.fromstring(r.content)
		#d = webdriver.Firefox()
		server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
		dc = DesiredCapabilities.HTMLUNIT
		d = webdriver.Remote(server_url, dc)

		d.get(url + term.replace("\n", "") + "+")
		tree = html.fromstring(d.page_source.encode('utf-8'))

		records = []
		for d in tree.xpath("//div[@class='olDetailLabels olDeptEmpName']"):
			row = OrderedDict()
			row['name'] = d.xpath("./text()")[0].strip()
			row['details'] = "$$$".join(d.xpath("./following-sibling::div[1]//text()[normalize-space()]")).replace("\n", "").replace("\r","").strip()
			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('valpo_edu.csv')
			with open('valpo_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('valpo_terms', 'a') as f:
			f.write(term)

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None
	finally:
		if d != None:
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
		terms = set(open('terms').readlines())
		if os.path.isfile('valpo_terms'):
			finished_terms = set(open('valpo_terms').readlines())
			terms -= finished_terms

		terms = list(terms)

		queue = Queue()

		for x in range(8):
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

