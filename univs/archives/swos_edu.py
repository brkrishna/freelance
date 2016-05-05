# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         swos_edu
# Purpose:      Southwestern Oklahoma State University
#
# Author:       Ramakrishna
#
# Dated:        04/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv, time
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'http://www.swosu.edu/cgi-bin/student-directory.pl'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
           'Content-Type':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'X-Requested-With':'XMLHttpRequest',
           'Host':'www.swosu.edu',
           'Referer':'http://www.swosu.edu/cgi-bin/student-directory.pl'}

def search(term):
	try:
		s = requests.session()
		data = {'keys':term.replace("\n", ""), 'submit':'Search'}
		try:
			r = s.post(url, headers=headers, data=data)
			if r.status_code != 200:
				return
		except requests.exceptions.ConnectionError as e:
			with open('swos_terms', 'a') as f:
				f.write(term)
			return

		tree = html.fromstring(r.content)

		students = tree.xpath("//div[@class='stripe']")

		records = []
		count = len(students)
		for i in range(0, count):

			row = OrderedDict()
			try:
				row['name'] = tree.xpath("//div[@class='stripe']/ul/li[1]/text()[normalize-space()]")[i].replace("\r\n", "").strip()
			except:
				continue
			try:
				row['email'] = tree.xpath("//div[@class='stripe']/ul/li[2]/a/text()[normalize-space()]")[i].replace("\r\n", "").strip()
			except:
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('swos_edu.csv')
			with open('swos_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('swos_terms', 'a') as f:
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
		if os.path.isfile('swos_terms'):
			finished_terms = set(open('swos_terms').readlines())
			terms -= finished_terms

		terms = list(terms)

		queue = Queue()

		for x in range(2):
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

