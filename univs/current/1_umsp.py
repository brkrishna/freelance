# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         umsp
# Purpose:      University of Wisconsin-Stevens Point
#
# Author:       Ramakrishna
#
# Dated:        13/Apr/2016
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

url = 'https://mypoint.uwsp.edu/regrec/RegRec006/Regrec006.aspx'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		data = {
			'__EVENTTARGET':'',
			'__EVENTARGUMENT':'',
			'__VIEWSTATEGENERATOR':'257ADFE7',
			'q':'Search this site...',
			'UWSPMaster:MainContent:TERM':'201520',
			'UWSPMaster:MainContent:TEXT_SEARCH':term.replace("\n",""),
			'UWSPMaster:MainContent:btn_submit':'Click here to BEGIN SEARCH'
		}
		r = s.get(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//table[@id='UWSPMaster_MainContent_DG_Result']//tr")

		records = []
		skip_first_row = False
		for stu in students:
			if skip_first_row:
				skip_first_row = True
				continue

			row = OrderedDict()
			try:
				row['name'] = stu.xpath("td[1]/b/text()")[0].strip()
			except:
				continue
			try:
				row['email'] = stu.xpath("td[2]/text()")[0].strip()
			except:
				continue
			try:
				row['phone'] = "$$$".join(stu.xpath("td[3]//text()")).strip()
			except:
				continue

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('umsp.csv')
			with open('umsp.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('umsp_terms', 'a') as f:
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
		terms = set(open('threechars').readlines())
		if os.path.isfile('umsp_terms'):
			finished_terms = set(open('umsp_terms').readlines())
			terms -= finished_terms

		terms = list(terms)

		queue = Queue()

		for x in range(16):
			worker = Worker(queue)
			worker.daemon = True
			worker.start()

		terms = ['abb\n']
		terms_count = len(terms)
		for i in range(0, terms_count):
			queue.put(terms[i])

		queue.join()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

