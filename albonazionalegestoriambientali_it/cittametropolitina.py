# -- coding: utf-8 --
import requests, os, time, random
from lxml import html

url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online/htm/tab_riassuntiva.htm'
base_url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online'

def main():
	try:

		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=headers)
		tree = html.fromstring(r.content)
		anchors = tree.xpath("//a[contains(@href, 'javascript:openBrWindow')]/@href")

		with open('cittametropolitana_v1','a') as f:
			for anchor in anchors:
				link = base_url + "/" + anchor[anchor.find("/")+1:anchor.find(".htm")+4]
				r2 = requests.get(link, headers=headers)
				tree2 = html.fromstring(r2.content)
				trs = tree2.xpath("//table//tr")
				rows = []
				for tr in trs:
					rows.append("$$$".join(tr.xpath("*//text()[normalize-space()]")).replace("\r", "&&&").replace("\n", "&&&"))

				line = '###'.join(rows)
				f.write(line + "\n")

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

