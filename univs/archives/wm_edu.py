# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         astate_edu
# Purpose:      College of William and Mary
#
# Author:       Ramakrishna
#
# Dated:        13/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv, string
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'http://directory.wm.edu/people/namelisting.cfm'
headers = {'User-Agent': 'Mozilla/5.0'}

def search(term):
	try:
		s = requests.session()
		data = {'phrase': term.replace("\n", ""), 'criteria':'contains', 'searchtype':'userid'}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		try:
			try:
				table = tree.xpath("//table[@class='displaydata tablespecial']")[1]
			except IndexError as e:
				with open('wm_terms', 'a') as f:
					f.write(term)
				return

			records = []
			skip_first_row = False
			for tr in table.xpath("tr"):
				if skip_first_row == False:
					skip_first_row = True
					continue

				row = OrderedDict()
				name = email = ''
				name = tr.xpath("td[1]/a/text()")
				row['name'] = name[0]
				email = tr.xpath("td[2]/a/text()")
				row['email'] = email[0]
				if row['name'] != '':
					records.append(row) 

			if len(records) > 0:
				file_exists = os.path.isfile('wm_edu.csv')
				with open('wm_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
					fp = csv.DictWriter(outfile, records[0].keys())
					if file_exists == False:
						fp.writeheader()
					fp.writerows(records)

			with open('wm_terms', 'a') as f:
				f.write(term)

		except Exception as e:
			print(e.__doc__)
			print(e.args)
			pass

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
		if os.path.isfile('wm_terms'):
			finished_terms = set(open('wm_terms').readlines())
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

