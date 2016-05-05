# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         flc
# Purpose:      Fort Lewis College
#
# Author:       Ramakrishna
#
# Dated:        22/Apr/2016
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

url = 'https://www.fortlewis.edu/directories/Faculty-Staff-Directories/ctl/ViewStudent/mid/9719.aspx'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
           'Cookie':'dnn_IsMobile=False; language=en-US; .ASPXANONYMOUS=P3hXnsrS0QEkAAAAMGMyMGZiOWEtMmIyOC00MWZiLTk4YzEtMTRkZTdkZmQ0MzE40'}

def search(term):
	try:
		s = requests.session()
		data = {'dnn$ctr9719$ViewStudent$textBoxLastName':term.replace("\n",""),
		        'dnn$ctr9719$ViewStudent$buttonSearch':'Search',
		        '__dnnVariable':'{"__scdoff":"1"}',
		        'ScrollTop':'285',
				'__VIEWSTATE':'/wEPDwUJNTQyMDU2MDYzD2QWAgIGD2QWAgIBD2QWAgIHD2QWAmYPZBYCAgUPZBYCZg9kFgJmD2QWAgIDD2QWAmYPZBYCAgEPZBYGAgMPZBYCAgUPDxYCHgdWaXNpYmxlaGRkAgUPZBYCAgUPDxYCHwBoZGQCCw8WAh4EVGV4dAVTPGRpdiBpZD0iZmxjLWRpci1yZXN1bHRzIiBjbGFzcz0ibm8tcmVzdWx0cyI+Tm8gU2VhcmNoIFJlc3VsdHMgd2VyZSByZXR1cm5lZC48L2Rpdj5kZNgf6nbC3b2K+O68te7ENKz32iUc',
				'__VIEWSTATEGENERATOR':'CA0B0334',
				'__EVENTVALIDATION':'/wEdAAfCrlgu9Ui9s7UHmPjmL2USpqTvtHV2rnpg+KLRH6zcqtekMu+77RooOk7G3BRHg1XSGDseovg2C82zX1/P3KAlRHOpKO8Fp+o9thVXV75QR1fJ82cLYuNHga3Vmj3QvawglYTgmyD61+C5CtBsuVtAjYYRWQ/fqJeb82O+/JWRVwXoxOw=',
				'ScriptManager_TSM':';;System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35:en:d28568d3-e53e-4706-928f-3765912b66ca:ea597d4b:b25378d2'}

		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		students = tree.xpath("//div[@class='contact']")

		records = []
		for stu in students:
			row = OrderedDict()
			try:
				row['id'] = stu.xpath("div[@class='id']/text()[normalize-space()]")[0].strip()
			except:
				pass
			try:
				row['name'] = stu.xpath("div[@class='name']/text()[normalize-space()]")[0].strip()
			except:
				continue

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('flc.csv')
			with open('flc.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('flc_terms', 'a') as f:
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
		if os.path.isfile('flc_terms'):
			finished_terms = set(open('flc_terms').readlines())
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

