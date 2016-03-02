# -- coding: utf-8 --
import requests, os, time, random, csv
from lxml import html

url = 'http://www.orimregionelombardia.it/AM-risultatiRicerca.php?operatore=AND&chiaveRicerca=&provincia=&nazionalita=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&action=ricerca'
base_url = 'http://www.orimregionelombardia.it/'

def main():
	try:

		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=headers)
		tree = html.fromstring(r.content)
		anchors = tree.xpath("//table[@class='standard']//a/@href")

		rows = []
		for anchor in anchors:
			link = base_url + anchor
			r2 = requests.get(link, headers=headers)
			tree2 = html.fromstring(r2.content)
			trs = tree2.xpath("//table//tr")

            '''
C:\Python27\python.exe "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 5.0.4\helpers\pydev\pydevconsole.py" 60435 60436
PyDev console: starting.

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\upwork\\freelance'])

Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
>>> import requests
>>> from lxml import html
>>> url = 'http://www.orimregionelombardia.it/AM-risultatiRicerca.php?operatore=AND&chiaveRicerca=&provincia=&nazionalita=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&obiettivi%5B%5D=0&action=ricerca'
>>> headers = {'User-Agent': 'Mozilla/5.0'}
>>> r = requests.get(url, headers=headers)
>>> tree = html.fromstring(r.content)
>>> anchors = tree.xpath("//table[@class='standard']//a/@href")
>>> len(anchors)
402
>>> base_url = 'http://www.orimregionelombardia.it/'
>>> r = requests.get(base_url + anchors[0], headers=headers)
>>> r.url
u'http://www.orimregionelombardia.it/AM-scheda.php?ID=3364'
>>> tree = html.fromstring(r.content)
>>> tree.xpath("//a[@name='_top']/@href")
[]
>>> tree.xpath("//div[@id='divContenuti']/h1/text()")
['Associazione dei Senegalesi della Provincia di Lecco']
>>> tree.xpath("//table[@class='no_border']/td//text()[normalize-space()]")
['Indirizzo', '23900 Lecco (LC)', 'Telefono Principale', '0341/488237', 'Fax', '0341/488245', 'Email principale', 'medinaserv@libero.it', u'Nazionalit\xe0 prevalente degli associati', 'Senegal', 'Presidente', 'Casset El Hadji Mama', 'Tel. 347/8128557', 'Obiettivi', u'Creare rapporti, organizzare comunit\xe0 immigrata', 'Scambio, mediazione interculturale, convivenza pacifica', 'Cooperazione internazionale']
'''

			for tr in trs:
                try:

				recs = tr.xpath("*//text()[normalize-space()]")
				if len(recs) > 1:
					try:
						col =  tr.xpath("*//text()[normalize-space()]")[0].encode("ascii")
					except UnicodeError:
						col =  tr.xpath("*//text()[normalize-space()]")[0].encode("utf-8")
					else:
						pass
					try:
						val = tr.xpath("*//text()[normalize-space()]")[1].encode("ascii")
					except UnicodeError:
						val = tr.xpath("*//text()[normalize-space()]")[1].encode("utf-8")
					else:
						pass
					col = col.replace("\r", "").replace("\n", " ").strip()
					val = val.replace("\r", "").replace("\n", " ").strip()
					row[col] = val
			rows.append(row)

		unique_keys = {}
		for r in rows:
			for key in r:
				if key not in unique_keys:
					unique_keys[key] = ''

		data = []
		for r in rows:
			record = {}
			for ukey in unique_keys.iterkeys():
				if ukey in r:
					record[ukey] = r[ukey]
				else:
					record[ukey] = ''

			data.append(record)

		with open('cittametropolitana.csv', 'w') as f:
			wrote_header = False
			for d in data:
				if wrote_header == False:
					w = csv.DictWriter(f, unique_keys.keys())
					w.writeheader()
					wrote_header = True
				w.writerow(d)

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

