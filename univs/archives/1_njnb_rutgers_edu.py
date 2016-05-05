# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         njnb_rutgers_edu
# Purpose:      Rutgers The State University of New Jersey-New Brunswick
#
# Author:       Ramakrishna
#
# Dated:        23/Mar/2016
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

url = 'https://www.acs.rutgers.edu/pls/pdb_p/Pdb_Display.search_results?p_name_first=&p_name_last='
headers = {'User-Agent': 'Mozilla/5.0'}

my_keys = ['Student:', 'School:', 'Academic Major(s):', 'Academic Minor(s):', 'Year of Graduation:']

def search(term):
	try:
		print(term.replace("\n", ""))
		s = requests.session()
		r = s.get(url + term.replace("\n", ""), headers=headers)
		tree = html.fromstring(r.content)

		students = tree.xpath("//table[@class='data']/*//a/@href")

		records = []
		for s_url in students:

			r2 = s.get(s_url, headers=headers)
			tree2 = html.fromstring(r2.content)

			div = tree2.xpath("//div[@id='content']")
			if div:
				for dl in div[0].xpath("//dl"):
					row = OrderedDict()
					try:
						row['name'] = div[0].xpath("//h3/text()")[0]
					except:
						continue
					try:
						temp = 	"".join(dl.xpath("dd//text() | dd/*//text()"))
						row[dl.xpath("dt/text()")[0].strip()] = temp.replace("\n","").encode('ascii', 'ignore').strip()
					except:
						pass
					try:
						row[dl.xpath("dt/text()")[1].strip()] = dl.xpath("dd/text()")[1].encode('ascii', 'ignore').strip()
					except:
						pass
					try:
						row[dl.xpath("dt/text()")[2].strip()] = dl.xpath("dd/text()")[2].encode('ascii', 'ignore').strip()
					except:
						pass
					records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('njnb_rutgers_edu.csv')
			with open('njnb_rutgers_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if file_exists == False:
					fp.writeheader()
				fp.writerows(records)

		with open('njnb_rutgers_terms', 'a') as f:
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
		if os.path.isfile('njnb_rutgers_terms'):
			finished_terms = set(open('njnb_rutgers_terms').readlines())
			terms -= finished_terms

		terms = list(terms)
		terms = ['sarjana\n']
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

