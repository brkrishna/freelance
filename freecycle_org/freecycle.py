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
import requests, csv, urllib, re
from bs4 import BeautifulSoup, SoupStrainer

base_url = 'https://groups.freecycle.org/group/bathfreecycle/posts/all'
url_2 = '?page='
url_3 = '&resultsperpage=100&showall=off&include_offers=off&include_wanteds=off&include_receiveds=off&include_takens=off'

headers = {'User-Agent': 'Mozilla/5.0'}


def main():
	#get_urls()
	get_details()

def get_details():
	try:

		with open('urls', 'r') as f:
			urls = f.readlines()

		rows = []
		for url in urls:
			row = {}
			r = requests.get(url.replace("\n", ""), headers=headers)
			tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'group_post'}))

			try:
				post_id = tree.find('h2', text = re.compile('post*', re.IGNORECASE))
				row['post_id'] = re.search("[0-9]+", post_id.text).group()
			except:
				row['post_id'] = ''
				pass

			try:
				type_content = tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
				if type_content == None:
					type_content = tree.find('h2', text = re.compile('wanted*', re.IGNORECASE))
					type = 'WANTED'
				else:
					type = 'OFFER'

				content = type_content.text
				content = content[content.find(":")+1:].strip()
				row['type'] = type
				row['content'] = content
			except:
				row['type'] = ''
				row['content'] = ''
				pass

			try:
				details = tree.find('div',{'id':'post_details'})
				if details:
					details = details.text
					loc = details[details.find("Location :")+10:details.find("Date")].strip()
					time = re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})", details).group()
					date = details.replace(loc, "").replace(time, "").replace(":", "").replace("Location", "").replace("Date", "").strip()
					row['loc'] = loc
					row['date'] = date
					row['time'] = time
			except:
				row['loc'] = ''
				row['date'] = ''
				row['time'] = ''
				pass

			try:
				desc = tree.find("div", {"id":"group_post"}).find("p")
				if desc:
					desc = desc.text.strip()
					row['desc'] = desc.replace("\r", "$$$").replace("\n", "###").strip()
			except:
				row['desc'] = ''
				pass

			try:
				image_url = tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)
				if image_url:
					href = image_url[0]['href']
					urllib.request.urlretrieve(href, "images/" + str(row['post_id']) + ".jpg")
			except Exception as e:
				print(e.__doc__)
				print(e.args)
				pass

			row['url'] = url.replace("\n","")
			rows.append(row)

		with open('freecycle.csv', 'w') as f:
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

def get_urls():
	try:
		r = requests.get(base_url, headers=headers)
		tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('table', {'id':'group_posts_table'}))

		with open('urls', 'a') as f:
			anchors = tree.findAll('a', href=True)

			i = 2
			while len(anchors) > 0:
				url_links = []
				for a in anchors:
					url_links.append(a['href'])

				url_links = sorted(set(url_links))
				for a in url_links:
					f.write(a + "\n")
				anchors = 0

				link = base_url + url_2 + str(i) + url_3
				print(link)
				r = requests.get(link, headers=headers)
				tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('table', {'id':'group_posts_table'}))

				try:
					anchors = tree.findAll('a', href=True)
					i += 1
				except:
					pass

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()

