# -- coding: utf-8 --
import requests, os, time, random
from lxml import html
from multiprocessing import Pool

url = 'http://tulane.edu/phonebook.cfm'
DOMAIN = 'http://tulane.edu/'

def main():
	terms = set(open('twochars').readlines())
	if os.path.isfile('tulane_terms'):
		finished_terms = set(open('tulane_terms').readlines())
		terms -= finished_terms

	terms = list(terms)
	with Pool(5) as p:
		terms_count = len(terms)
		for i in range(0, terms_count, 5):
			p.map(worker,terms[i:i+5])

def worker(term):
	try:
		headers = {'User-Agent': 'Mozilla/5.0'}
		data = {'name':term.replace("\n",""),'Search':'Search','S':''}

		r = requests.post(url, headers=headers, data=data)
		#time.sleep(random.randint(0,1))
		tree = html.fromstring(r.content)
		records = []
		links = tree.xpath("//tr[@class='even' or @class='odd']/td/p/a/@href")
		for link in links:
			r2 = requests.get(DOMAIN + link, headers=headers)
			tree2 = html.fromstring(r2.content)

			id = r2.url[r2.url.find("=")+1:]
			trs = tree2.xpath("//table[@class='phone_list']//tr")

			r = []
			with open('tulane_data','a') as f:
				for tr in trs:
					for td in tr.xpath("td"):
						r.append(",".join(td.xpath("*//text()")))
				try:
					#line = r2.url[r2.url.find("=")+1:] + "|" + r[1][1] + "|" + r[1][3] + "|" + r[2][1] + "|" + r[5][1]  + "|" + r[7][1] + "|" + r[8][1]
					line = r2.url[r2.url.find("=")+1:] + "|" + r[1] + "|" + r[5] + "|" + r[3] + "|" + r[7]  + "|" + r[15] + "|" + r[21] + "|" + r[23]
					f.write(line + "\n")

				except Exception as e:
					print(e.__doc__)
					print(e.args)
					continue

		with open('tulane_terms','a') as f:
			f.write(term)

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()
