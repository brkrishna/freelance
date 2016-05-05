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

url = 'http://directory.potsdam.edu/index.pl'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		data = {'nameField':term.replace("\n", ""), 'nameOptions':'contains', 'searchButton':'Student Search'}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//tr[@bgcolor='#e0e0e0' or @bgcolor='#FFFFFF']")

		records = []
		for tr in students:
			temp = tr.xpath("*//text()[normalize-space()]")
			row = OrderedDict()
			try:
				if temp[0].replace(r"\\xa0", "").strip() != '':
					row['name'] = temp[0].strip()
				else:
					continue
			except:
				continue
			try:
				row['address'] = temp[1].strip()
			except:
				row['address'] = ''
				pass
			try:
				row['email'] = temp[2].strip()
			except:
				row['email'] = ''
				pass
			try:
				row['phone'] = temp[3].replace(r'\\xa0','').strip()
			except:
				row['phone'] = ''
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('potsdam_edu.csv')
			with open('potsdam_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('potsdam_terms', 'a') as f:
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
		if os.path.isfile('potsdam_terms'):
			finished_terms = set(open('potsdam_terms').readlines())
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

