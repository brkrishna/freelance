# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         baker_edu
# Purpose:      Baker University
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
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

url = 'http://www.bakeru.edu/index.php?option=com_searchdirectory&view=searchcas&Itemid=13235&limitstart=0&searchword='
url_2 = '&submit=Search'
headers = {'User-Agent': 'Mozilla/5.0'}

def search(term):
	try:
		print(term.replace("\n", ""))
		s = requests.session()
		r = s.get(url + '%' + term.replace("\n", "") + '%' + url_2, headers=headers)
		tree = html.fromstring(r.content)

		divs = tree.xpath("//div[@style='margin-bottom:8px; padding-bottom:8px; border-bottom:1px solid #866c52;']")

		records = []
		for d in divs:
			row = OrderedDict()
			try:
				row['name'] = d.xpath("./text()[normalize-space()]")[0].strip()
			except:
				continue
			try:
				row['email'] = d.xpath("a/@href")[0].replace("mailto:","").strip()
			except:
				pass

			records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('baker_edu.csv')
			with open('baker_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('baker_terms', 'a') as f:
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
		if os.path.isfile('baker_terms'):
			finished_terms = set(open('baker_terms').readlines())
			terms -= finished_terms

		terms = list(terms)
		terms = list(string.ascii_lowercase)
		queue = Queue()

		for x in range(4):
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

