# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         baker_edu
# Purpose:      Savannah University
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, string, csv, os
from collections import OrderedDict
from xml.dom.minidom import parse
import xml.dom.minidom

import socks, socket
from queue import Queue
from threading import Thread

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url_1 = 'http://www.savannahstate.edu/utilities/SuggestedSearchService.asmx/Find?keyword=%25'
url_2 = '%25&numberOfPosts=200&type=employee&subtype=student'

s = requests.session()
headers = {'User-Agent': 'Mozilla/5.0'}

def search(term):
	try:
		records = []
		try:
			r = s.get(url_1 + term.replace("\n", "") + url_2, headers=headers)
			DOMTree = xml.dom.minidom.parseString(r.text)
			collection = DOMTree.documentElement
			results = collection.getElementsByTagName("SearchResult")
			print(term.replace("\n", "") + " - " + str(len(results)))
			for result in results:
				row = OrderedDict()
				try:
					row['name'] = result.getElementsByTagName('LinkText')[0].childNodes[0].data
				except:
					pass
				try:
					row['email'] = result.getElementsByTagName('LinkURL')[0].childNodes[0].data.replace("mailto:", "")
				except:
					pass
				records.append(row)

		except Exception as e:
			print(e.__doc__)
			print(e.args)
			pass

		if len(records) > 0:
			file_exists = os.path.isfile('savannah_edu.csv')
			with open('savannah_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('savannah_terms', 'a') as f:
			f.write(term)


	except Exception as e:
		print(e.__doc__)
		print(e.args)
		pass

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
		if os.path.isfile('savannah_terms'):
			finished_terms = set(open('savannah_terms').readlines())
			terms -= finished_terms

		terms = list(terms)
		queue = Queue()

		for x in range(16):
			worker = Worker(queue)
			worker.daemon = True
			worker.start()

		for term in terms:
			queue.put(term)

		queue.join()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()