# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         astate_edu
# Purpose:      Parse Arkansas State University
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, re, os, csv
from lxml import html
from multiprocessing import Pool
import socks, socket
from collections import OrderedDict

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

url = 'http://webapps.astate.edu/directory/student/searchstuddir.php'
headers = {'User-Agent': 'Mozilla/5.0'}

def main():
	try:
		terms = set(open('terms').readlines())
		if os.path.isfile('astate_terms'):
			finished_terms = set(open('astate_terms').readlines())
			terms -= finished_terms

		terms = list(terms)

		with Pool(5) as p:
			terms_count = len(terms)
			for i in range(0, terms_count, 5):
				results = p.map(worker,terms[i:i+5])
				results = [r for r in results if not r == []]

				data = []
				for r in results:
					for d in r:
						data.append(d)

				file_exists = os.path.isfile('astate_data.csv')
				wrote_header = False
				with open('astate_data.csv', 'a') as f:
					for d in data:
						if file_exists == True and wrote_header == False:
							w = csv.DictWriter(f, d.keys())
							wrote_header = True
						elif file_exists == False and wrote_header == False:
							w = csv.DictWriter(f, d.keys())
							w.writeheader()
							wrote_header = True
						w.writerow(d)

				open('astate_terms', 'a').write("".join(terms[i:i+5]))

	except Exception as e:
		print(e.__doc__)
		print(e.args)

def worker(term):
	try:
		s = requests.session()
		data = {'SearchField': term.replace("\n", "")}
		r = s.post(url, headers=headers, data=data)
		tree = html.fromstring(r.content)

		table = tree.xpath("//table")

		rows = []
		for tr in table[0].xpath("//tr"):
			rows.append("$$$".join(tr.xpath("*//text()[normalize-space()]")))

		records = []
		for r in rows:
			if 'Name:' in r:
				rec = OrderedDict()
				rec['name'] = r[r.find('$$$')+3:].strip()
			elif 'Email' in r:
				rec['email'] = r[r.find("$$$")+3:].strip()
			else:
				records.append(rec)
		return records

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		return None

if __name__ == '__main__':
	main()

