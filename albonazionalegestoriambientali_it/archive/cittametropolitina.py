# -- coding: utf-8 --
# encoding=utf8
import requests, os, time, random, csv
from lxml import html
from lxml.html.clean import Cleaner

url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online/htm/tab_riassuntiva.htm'
base_url = 'http://www.cittametropolitana.mi.it/cultura/progetti/integrando/cd-online'
cleaner = Cleaner(style=True, links=True, add_nofollow=True, page_structure=False, safe_attrs_only=False)

def main():
	try:

		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(url, headers=headers)

		tree = html.fromstring(r.content)
		anchors = tree.xpath("//a[contains(@href, 'javascript:openBrWindow')]/@href")

		with open('cittametropolitana', 'w') as f:
			for anchor in anchors:
				link = base_url + "/" + anchor[anchor.find("/")+1:anchor.find(".htm")+4]
				r2 = requests.get(link, headers=headers)
				tree2 = html.fromstring(cleaner.clean_html(r2.content))



				line = "$$$".join(tree2.xpath("*//text()[normalize-space()]")).replace("\r", "###").replace("\n", "%%%").strip()
				f.write(line + "\n")

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

