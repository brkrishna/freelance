# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         umsl_edu
# Purpose:      University of Missouri - St Louis
#
# Author:       Ramakrishna
#
# Dated:        11/Apr/2016
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

url = 'https://apps.umsl.edu/webapps/ITS/DirectorySearch/Search.cfm'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		data = {'LastName':term.replace("\n", ""), 'dept':'', 'div':'', 'divname':'', 'saveForm':'Search', 'um_type':'S'}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//table[@id='myResults']//tr")

		records = []
		count = len(students)
		for i in range(1,count):
			temp = "$$$".join(students[i].xpath("*//text()[normalize-space()]")).replace("\r\n\t","").replace("\t","").strip()
			row = OrderedDict()
			name = email = ''
			try:
				name, email = temp.split("$$$")
				row['name'] = name
				row['email'] = email
			except:
				continue
			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('umsl_edu.csv')
			with open('umsl_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('umsl_terms', 'a') as f:
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
		terms = set(open('twochars').readlines())
		if os.path.isfile('umsl_terms'):
			finished_terms = set(open('umsl_terms').readlines())
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

