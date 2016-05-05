# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         umrf
# Purpose:      University of Wisconsin-River Falls
#
# Author:       Ramakrishna
#
# Dated:        13/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'https://www.uwrf.edu/PeopleSearch/Search.cfm?eduPersonNickname=&sn='
url_2 = '&searchtype=like&student=Yes&searchSubmit=Search'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		r = s.get(url + term.replace("\n","") + url_2, headers=headers)
		tree = html.fromstring(r.content)

		students = tree.xpath("//div[@class='CS_Textblock_Text']/table//tr")

		records = []
		skip_first_row = False
		for stu in students:
			if skip_first_row == False:
				skip_first_row = True
				continue

			row = OrderedDict()
			try:
				row['name'] = stu.xpath("td[1]/p/text()")[0].strip()
			except:
				continue
			try:
				row['email'] = stu.xpath("td[2]/p/a/@href")[0].replace("mailto:","").strip()
			except:
				continue
			try:
				row['phone'] = stu.xpath("td[2]/p/text()")[0].replace("ph:","").strip()
			except:
				continue

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('uwrf.csv')
			with open('uwrf.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('uwrf_terms', 'a') as f:
			f.write(term)

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None

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
		terms = set(open('threechars').readlines())
		if os.path.isfile('uwrf_terms'):
			finished_terms = set(open('uwrf_terms').readlines())
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

