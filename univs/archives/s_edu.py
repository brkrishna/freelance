# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         s_edu
# Purpose:      Shepherd University
#
# Author:       Ramakrishna
#
# Dated:        04/Apr/2016
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

url = 'http://www.shepherd.edu/webinfo/people.php?go'
domain = 'http://www.shepherd.edu'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
           'Content-Type':'application/x-www-form-urlencoded',
           'X-Requested-With':'XMLHttpRequest',
           'Referer':'http://web-apps.spu.edu/whitepages'}

def search(term):
	try:
		s = requests.session()
		data = {'department':'', 'firstname':'', 'lastname':term.replace("\n", ""), 'submit':'Search', 'type':'student', 'username':''}
		r = s.post(url, headers=headers, data=data)
		if r.status_code != 200:
			return

		tree = html.fromstring(r.content)

		anchors = tree.xpath("//a[contains(@href,'/webinfo/results.php')]/@href")
		anchors = sorted(set(anchors))
		records = []
		if anchors:
			for a in anchors:
				r2 = s.get(domain + a)
				if r2.status_code != 200:
					continue
				tree2 = html.fromstring(r2.content)

				row = OrderedDict()
				for tr in tree2.xpath("//tr"):
					col1 = tr.xpath("td[1]/text()[normalize-space()]")[0].replace(" ", "_").lower().strip()
					col2 = tr.xpath("td[2]//text()[normalize-space()]")
					if col2:
						col2 = col2[0]
					else:
						col2 = ''

					row[col1] = col2

				records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('s_edu.csv')
			with open('s_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('s_terms', 'a') as f:
			f.write(term)

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None
	finally:
		if s:
			s = None

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
		if os.path.isfile('s_terms'):
			finished_terms = set(open('s_terms').readlines())
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

