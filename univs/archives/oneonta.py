# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         suny_oneonta
# Purpose:      State University of New York Oneonta
#
# Author:       Ramakrishna
#
# Dated:        09/Apr/2016
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

url = 'https://webservices.oneonta.edu/produc/suco_directory_search.list'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		data = {'first_name':term.replace("\n", "")}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//table[@class='inner']")[0]
		trs = students.xpath("//tr")

		records = []
		for tr in trs:

			if tr.xpath("td[1]/a[@class='showcard']/text()"):
				row = OrderedDict()
				try:
					row['name'] = tr.xpath("td[1]/a[@class='showcard']/text()")[0].strip()
				except:
					continue
			try:
				row['email'] = tr.xpath("td[3]/a/@href")[0].replace("mailto:", "").strip()
				records.append(row)
			except:
				pass

		if len(records) > 0:
			file_exists = os.path.isfile('oneonta_edu.csv')
			with open('oneonta_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('oneonta_terms', 'a') as f:
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
		terms = set(open('terms.txt').readlines())
		if os.path.isfile('oneonta_terms'):
			finished_terms = set(open('oneonta_terms').readlines())
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

