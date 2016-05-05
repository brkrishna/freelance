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
			print(link)
			r2 = requests.get(link, headers=headers)
			tree2 = html.fromstring(r2.content)
			trs = tree2.xpath("//table//tr")

			row = {}
			try:
				row['title'] = tree2.xpath("//div[@id='divContenuti']/h1/text()")[0].strip()
			except:
				row['title'] = ''
				pass
			try:
				temp = tree2.xpath("//table[@class='no_border']/td//text()[normalize-space()]")
				try:
					idx = temp.index("Indirizzo")
					if idx >= 0:
						row['indirizzo'] = temp[idx+1]
				except:
					row['indirizzo'] = ''
					pass
				try:
					idx = temp.index("Telefono Principale")
					if idx >= 0:
						row['telefono_principale'] = temp[idx+1]
				except:
					row['telefono_principale'] = ''
					pass
				try:
					idx = temp.index("Fax")
					if idx >= 0:
						row['fax'] = temp[idx+1]
				except:
					row['fax'] = ''
					pass
				try:
					idx = temp.index("Email principale")
					if idx >= 0:
						row['email_principale'] = temp[idx+1]
				except:
					row['email_principale'] = ''
					pass
				try:
					idx = temp.index("Nazionalità prevalente degli associati")
					if idx >= 0:
						row['nazionalit_prevalente_degli_associati'] = temp[idx+1]
				except:
					row['nazionalit_prevalente_degli_associati'] = ''
					pass
				try:
					idx = temp.index("Presidente")
					if idx >= 0:
						row['presidente'] = temp[idx+1]
				except:
					row['presidente'] = ''
					pass
				try:
					idx_start = temp.index("Presidente")
					idx_end = temp.index("Obiettivi")

					if idx_start > 0 and idx_end > 9:
						row['tel'] = temp[idx_start+2:idx_end]
				except:
					row['tel'] = ''
					pass
				try:
					idx = temp.index("Obiettivi")
					if idx > 0:
						row['obiettivi'] = "$$$".join(temp[idx+1:])
				except:
					row['obiettivi'] = ''
					pass

			except Exception as e:
				print(e.__doc__)
				print(e.args)
					
			rows.append(row)

		with open('orimregionelombardia.csv', 'w') as f:
			wrote_header = False
			for d in rows:
				if wrote_header == False:
					w = csv.DictWriter(f, d.keys())
					w.writeheader()
					wrote_header = True
				w.writerow(d)

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

