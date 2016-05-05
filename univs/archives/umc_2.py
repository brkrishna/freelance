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


url = 'https://cf-prod1.crk.umn.edu/Directory/Data.cfc?method=getName&_cf_ajaxproxytoken=737EF18EA1FAAC&returnFormat=json&argumentCollection=%7B%22myID%22%3A'
url_2 = '%7D&_cf_nodebug=true&_cf_nocache=true&_cf_clientid=4E59BE12DBD77EE326E72449F95BDE9D&_cf_rc=6'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'}

def search(term):
	try:
		s = requests.session()
		r = s.get(url + term + url_2, headers=headers)
		if r.status_code != 200:
			return
		tree = html.fromstring(r.content)

		records = []
		row = OrderedDict()
		try:
			row['name'] = tree.xpath("//span[@class='Caption_Name']/text()")[0]
		except:
			return
		try:
			row['address'] = " ".join(tree.xpath("//span[@class='Caption_Position']/*//text()")).replace("\r","").replace("\n","").replace("\t","").replace("\\t","").replace("\\n","").replace("\xa0","").strip()
		except:
			row['address'] = ''
			pass
		try:
			row['email'] = tree.xpath("//span[@class='Caption_Email']/a/text()")[0]
		except:
			row['email'] = ''
			pass
		try:
			row['phone'] = tree.xpath("//span[@class='Caption_Phone']/*//text()")[1].strip()
		except:
			row['phone'] = ''
			pass

		records.append(row)

		if len(records) > 0:
			file_exists = os.path.isfile('umc2_edu.csv')
			with open('umc2_edu.csv', 'a', newline='', encoding='utf-8') as outfile:
				fp = csv.DictWriter(outfile, records[0].keys())
				if not file_exists:
					fp.writeheader()
				fp.writerows(records)

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
		queue = Queue()

		for x in range(16):
			worker = Worker(queue)
			worker.daemon = True
			worker.start()

		with open('umc_edu.csv', 'r', newline='', encoding='utf-8') as outfile:
			terms = csv.reader(outfile)

			for row in terms:
				queue.put(row[1])

		queue.join()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

