# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         spu_edu
# Purpose:      Seattle Pacific University
#
# Author:       Ramakrishna
#
# Dated:        03/Apr/2016
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

url = 'http://web-apps.spu.edu/whitepages/Search/Search'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
           'Content-Type':'application/x-www-form-urlencoded',
           'X-Requested-With':'XMLHttpRequest',
           'Referer':'http://web-apps.spu.edu/whitepages'}

def search(term):
	try:
		s = requests.session()
		data = {'query':'%' + term.replace("\n", "") + '%'}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//div[@class='span-18 clearfix resultBox  padded last score-1520']")

		records = []
		count = len(students)
		for i in range(0, count):
			rec_type = students[i].xpath("//div[@class='rel']/text()")[i].replace("\r\n", "").strip()
			if rec_type != 'Student':
				continue

			row = OrderedDict()
			try:
				row['name'] = students[i].xpath("//h3/text()[normalize-space()]")[i].replace("\r\n", "").replace(" ","").strip()
			except:
				continue
			try:
				row['email'] = students[i].xpath("//div[@class='email']/a/text()")[i].replace("\r\n", "").strip()
			except:
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('spu_edu.csv')
			with open('spu_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('spu_terms', 'a') as f:
			f.write(term + "\n")

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
		terms = set(open('terms.txt').readlines())
		if os.path.isfile('spu_terms'):
			finished_terms = set(open('spu_terms').readlines())
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

