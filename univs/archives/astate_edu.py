# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         astate_edu
# Purpose:      Parse Arkansas State University
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

url = 'http://webapps.astate.edu/directory/student/searchstuddir.php'
headers = {'User-Agent': 'Mozilla/5.0'}


def search(term):
	try:
		print(term.replace("\n", ""))
		s = requests.session()
		data = {'SearchField': term.replace("\n", "")}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		table = tree.xpath("//table")

		rows = []
		for tr in table[0].xpath("//tr"):
			rows.append("$$$".join(tr.xpath("*//text()[normalize-space()]")))

		records = []
		for r in rows:
			if 'Name:' in r:
				rec = OrderedDict()
				rec['name'] = r[r.find('$$$')+3:].strip()
			elif 'Email' in r:
				rec['email'] = r[r.find("$$$")+3:].strip()
			else:
				records.append(rec)

		file_exists = os.path.isfile('astate_data.csv')
		wrote_header = False
		with open('astate_data.csv', 'a') as f:
			for d in records:
				if file_exists == True and wrote_header == False:
					w = csv.DictWriter(f, d.keys())
					wrote_header = True
				elif file_exists == False and wrote_header == False:
					w = csv.DictWriter(f, d.keys())
					w.writeheader()
					wrote_header = True
				w.writerow(d)

		with open('astate_terms', 'a') as f:
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
		if os.path.isfile('astate_terms'):
			finished_terms = set(open('astate_terms').readlines())
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

