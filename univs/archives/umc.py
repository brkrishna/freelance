# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         umc
# Purpose:      University of Minnesota Crookston
#
# Author:       Ramakrishna
#
# Dated:        11/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv, json, string
from lxml import html
import socks, socket
from collections import OrderedDict
from queue import Queue
from threading import Thread

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'https://cf-prod1.crk.umn.edu/Directory/Data.cfc?method=getNameData&&&myID='
url_2 = '&&&myPart=&pageSize=200&_cf_ajaxproxytoken=737EF18EA1FAAC&_cf_clientid=4E59BE12DBD77EE326E72449F95BDE9D&_cf_rc=0&_cf_nodebug=true&_cf_nocache=true&returnFormat=json&_dc=1460307912945&start=0&limit=200&page=1&gridsortcolumn=&gridsortdirection=ASC'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		r = s.get(url + term + url_2, headers=headers)
		if r.status_code != 200:
			return
		rows = r.json()

		row_count = len(rows['QUERY']['DATA'])
		records = []
		for i in range(0, row_count):
			row = OrderedDict()
			try:
				row['name'] = rows['QUERY']['DATA'][i][0]
			except:
				pass
			try:
				row['id'] = rows['QUERY']['DATA'][i][1]
			except:
				pass
			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('umc_edu.csv')
			with open('umc_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

		with open('umc_terms', 'a') as f:
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
		if os.path.isfile('umc_terms'):
			finished_terms = set(open('umc_terms').readlines())
			terms -= finished_terms

		terms = list(terms)
		terms = string.ascii_uppercase
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

