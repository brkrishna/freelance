# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:         parser
# Purpose:
#
# Author:       Ramakrishna
#
# Dated:        07/Mar/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
import requests, csv, urllib
from bs4 import beautifulSoup

base_url = 'https://groups.freecycle.org/group/bathfreecycle/posts/all'
url_2 = '?page='
url_3 = '&resultsperpage=100&showall=off&include_offers=off&include_wanteds=off&include_receiveds=off&include_takens=off'

def main():
	#get_urls()

def get_details():
	try:
		with open('urls', 'r') as f:
			urls = f.readlines()
			for url in urls:
				r = requests.get(url.replace("\n", ""), headers=headers)
				tree = html.fromstring(r.content)

		pass
	except Exception as e:
		print(e.__doc__)
		print(e.args)

def get_urls():
	try:
		headers = {'User-Agent': 'Mozilla/5.0'}
		r = requests.get(base_url, headers=headers)
		tree = html.fromstring(r.content)

		with open('urls', 'a') as f:
			anchors = tree.xpath("//table[@id='group_posts_table']//a/@href")

			i = 2
			while anchors != None:
				anchors = sorted(set(anchors))
				for a in anchors:
					print(a)
					f.write(a + "\n")
				anchors = None

				link = base_url + url_2 + str(i) + url_3
				print(link)
				r = requests.get(link, headers=headers)
				tree = html.fromstring(r.content)

				try:
					print("here")
					anchors = tree.xpath("//table[@id='group_posts_table']//a/@href")
					print(len(anchors))
					i += 1
					if i > 8:
						break
				except:
					pass

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

