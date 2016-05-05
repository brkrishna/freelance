# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         Fort Lewis College
# Purpose:      Parse Fort Lewis College student details json
#
# Author:       Ramakrishna
#
# Created:      22/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, os, time, random, json, csv
from lxml import html
import socks, socket
from threading import Thread
from queue import Queue
from collections import OrderedDict

MIN = 0
MAX = 1

URL = 'https://www.fortlewis.edu/DesktopModules/DirectorySearch/WService.asmx/StudentSearch'

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

def main():
	try:
		terms = []
		with open('flc.csv', 'r') as f:
			records = f.read().splitlines()
			for rec in records:
				id, name = rec.split(",")
				terms.append(id)

		terms = set(terms)
		if os.path.isfile('flc_data_terms'):
			finished_terms = set(open('flc_data_terms').readlines())
			terms -= finished_terms

		terms = sorted(terms)
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

def process(term):
	try:
		headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
		data = '{"id": "' + term.replace('\n','') + '"}'
		time.sleep(random.randint(MIN, MAX))
		r = requests.post(URL, headers=headers, data=data)

		recs = []
		if r.status_code == 200:
			records = r.json()
			row = OrderedDict()
			try:
				row['address'] = records['d'][0]['Address']
			except Exception as e:
				row['address'] = ''
				pass
			try:
				row['city'] = records['d'][0]['City']
			except Exception as e:
				row['city'] = ''
				pass
			try:
				row['dept'] = records['d'][0]['Department']
			except Exception as e:
				row['dept'] = ''
				pass
			try:
				row['email'] = records['d'][0]['Email']
			except Exception as e:
				row['email'] = ''
				pass
			try:
				row['fname'] = records['d'][0]['FirstName']
			except Exception as e:
				row['fname'] = ''
				pass
			try:
				row['initial'] = records['d'][0]['Initial']
			except Exception as e:
				row['initial'] = ''
				pass
			try:
				row['lname'] = records['d'][0]['LastName']
			except Exception as e:
				row['lname'] = ''
				pass
			try:
				row['id'] = records['d'][0]['Id']
			except Exception as e:
				return
			try:
				row['mobile'] = records['d'][0]['Mobile']
			except Exception as e:
				row['mobile'] = ''
				pass
			try:
				row['phone'] = records['d'][0]['Phone']
			except Exception as e:
				row['phone'] = ''
				pass
			try:
				row['office'] = records['d'][0]['Office']
			except Exception as e:
				row['office'] = ''
				pass
			try:
				row['title'] = records['d'][0]['Title']
			except Exception as e:
				row['title'] = ''
				pass
			recs.append(row)

			if len(recs) > 0:
				file_exists = os.path.isfile('flc_data.csv')
				with open('flc_data.csv', 'a', newline='', encoding='utf-8') as outfile:
					fp = csv.DictWriter(outfile, recs[0].keys())
					if not file_exists:
						fp.writeheader()
					fp.writerows(recs)

			with open('flc_data_terms', 'a') as f:
				f.write(term + "\n")

	except Exception as e:
		print(e.__doc__)
		print(e.args)

class Worker(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			term = self.queue.get()
			process(term)
			self.queue.task_done()

if __name__ == '__main__':
	main()

