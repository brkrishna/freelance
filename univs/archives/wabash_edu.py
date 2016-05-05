# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         wabash_edu
# Purpose:      Wabash University
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
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

url = 'https://www.wabash.edu/aboutwabash/home.cfm?pages_id=4'
headers = {'User-Agent': 'Mozilla/5.0'}

def search(term):
	try:
		print(term.replace("\n", ""))
		s = requests.session()
		data = {'first':'', 'last':term.replace("\n", ""), 'student_matches':'1', 'vUsername':''}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//div[@class='employee']")

		records = []
		for s in students:
			row = OrderedDict()
			try:
				row['name'] = s.xpath("div/div/h3[@class='panel-title'][1]/text()[normalize-space()]")[0].replace("\r\n","").strip()
			except:
				continue
			try:
				row['email'] = s.xpath("div/div/div/div/div/div/a/@href")[0].replace("mailto:","").strip()
			except:
				pass
			try:
				row['loc']  = s.xpath("div/div/div/div/div/div[2]/text()")[0].strip()
			except:
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('wabash_edu.csv')
			with open('wabash_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('wabash_terms', 'a') as f:
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
		if os.path.isfile('wabash_terms'):
			finished_terms = set(open('wabash_terms').readlines())
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

