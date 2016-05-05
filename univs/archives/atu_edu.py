# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         astate_edu
# Purpose:      Parse Arkansas Tech University
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

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'https://www.atu.edu/directory/index.php'
headers = {'User-Agent': 'Mozilla/5.0'}

def search(term):
	try:
		s = requests.session()
		data = {'name': term.replace("\n", ""), 'which':'s'}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		records = []
		for p in tree.xpath("//p[@class='person']"):
			row = OrderedDict()
			row['name'] = p.xpath("span[@class='name']/text()[normalize-space()]")[0]
			row['email'] = p.xpath("span[@class='details']/a/text()[normalize-space()]")[0]
			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('atu_edu.csv')
			with open('atu_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('atu_terms', 'a') as f:
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
		terms = set(open('terms').readlines())
		if os.path.isfile('atu_terms'):
			finished_terms = set(open('atu_terms').readlines())
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

