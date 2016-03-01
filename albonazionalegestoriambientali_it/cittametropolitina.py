# -- coding: utf-8 --
# encoding=utf8
import requests, os, time, random, csv
from lxml import html

url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online/htm/tab_riassuntiva.htm'
base_url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online'

def main():
	try:

		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=headers)
		tree = html.fromstring(r.content)
		anchors = tree.xpath("//a[contains(@href, 'javascript:openBrWindow')]/@href")

		rows = []
		for anchor in anchors:
			link = base_url + "/" + anchor[anchor.find("/")+1:anchor.find(".htm")+4]
			r2 = requests.get(link, headers=headers)
			tree2 = html.fromstring(r2.content)
			trs = tree2.xpath("//table//tr")
			row = {}
			for tr in trs:
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

