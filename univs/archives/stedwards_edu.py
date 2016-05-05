# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         swos_edu
# Purpose:      Stedwards University
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

url = 'https://www.stedwards.edu/directory?search='
url_2 = '&type=student&field_employee_school=All&academic_department=All&administrative_department=All&page='

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		page = 0

		s = requests.session()
		link = url + term.replace("\n", "") + url_2 + str(page)
		try:
			r = s.get(link, headers=headers)
			if r.status_code != 200:
				return
		except requests.exceptions.ConnectionError as e:
			with open('stewards_terms', 'a') as f:
				f.write(term)
			return


		tree = html.fromstring(r.content)
		students = tree.xpath("//div[@class='info-upper']")

		records = []

		while len(students) > 0:
			count = len(students)
			for i in range(0, count):

				row = OrderedDict()
				try:
					row['name'] = "".join(students[i].xpath("span[@class='name']//text()[normalize-space()]")).strip()
				except:
					continue
				try:
					row['email'] = "".join(students[i].xpath("span[@class='email']//text()[normalize-space()]")).replace(" [at] ", r"@").strip()
				except:
					pass

				records.append(row)

			page += 1
			link = url + term.replace("\n", "") + url_2 + str(page)
			r = s.get(link, headers=headers)
			tree = html.fromstring(r.content)
			students = tree.xpath("//div[@class='info-upper']")

		if len(records) > 0:
			file_exists = os.path.isfile('stewards_edu.csv')
			with open('stewards_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('stewards_terms', 'a') as f:
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
		if os.path.isfile('stewards_terms'):
			finished_terms = set(open('stewards_terms').readlines())
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

