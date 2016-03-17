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
import requests, csv, urllib, re, datetime, sys
import os.path
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict

home_url = 'https://my.freecycle.org/login'
uk_base_url = 'https://www.freecycle.org/browse/UK'
pager_line1 = '/posts/all?page='
pager_line2 = '&resultsperpage=10&showall=off&include_offers=off&include_wanteds=off&include_receiveds=off&include_takens=off'

headers = {'User-Agent': 'Mozilla/5.0'}
data = {'username':'alanh777', 'pass':'Orange101', 'referer':''}

def get_details():
	try:

		s = requests.session()
		r = s.post(home_url, headers=headers, data=data)

		with open('freecycle_groups.csv', 'r') as f:
			group_urls = csv.DictReader(f)

			finished_urls = []
			if os.path.isfile('urls_done'):
				finished_urls = open('urls_done').read().splitlines()

			for gu in group_urls:
				post_urls = []
				if gu['group_url'].replace("\n", "") in finished_urls:
					continue

				r = requests.get(gu['group_url'].replace("\n", ""), headers=headers)
				tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('table', {'id':'group_posts_table'}))

				anchors = tree.findAll('a', href=True)
				i = 2

				while len(anchors) > 0:
					for a in anchors:
						post_urls.append(a['href'])

					anchors = 0

					link = gu['group_url'].replace("\n", "") + pager_line1 + str(i) + pager_line2
					res = s.get(link, headers=headers)
					tree2 = BeautifulSoup(res.content, "html.parser", parse_only=SoupStrainer('table', {'id':'group_posts_table'}))

					try:
						anchors = tree2.findAll('a', href=True)
						i += 1
					except:
						pass

				post_urls = sorted(set(post_urls))
				rows = []
				for pu in post_urls:

					r = s.get(pu.replace("\n", ""))
					tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'group_post'}))
					type = region = group = loc = post_id = title = date = time = posted_by = desc = url = ''

					#To join the group if not already part of it
					try:
						a = tree.find('a', href=re.compile('join_group'))
						r = s.get(a['href'])

						r = s.get(pu.replace("\n", ""))
						tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'group_post'}))
					except:
						pass
					#End join the group

					try:
						post_id = tree.find('h2', text = re.compile('post*', re.IGNORECASE))
						post_id = re.search("[0-9]+", post_id.text).group()
					except:
						pass

					try:
						type_content = tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
						if type_content == None:
							type_content = tree.find('h2', text = re.compile('wanted*', re.IGNORECASE))
							type = 'WANTED'
						else:
							type = 'OFFER'

						content = type_content.text
						title = content[content.find(":")+1:].strip()

					except:
						pass

					try:
						details = tree.find('div',{'id':'post_details'})
						if details:
							details_text = details.text
							loc = details_text[details_text.find("Location :")+10:details_text.find("Date")].strip()
							time = re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})", details_text).group()
							date = details_text.replace(loc, "").replace(time, "").replace(":", "").replace("Location", "").replace("Date", "").strip()
							date = date[:date.find("Posted")]
							date = date.replace("PM UTC", "").replace("AM UTC", "").strip()
							date = date.replace("PM UT", "").replace("AM UT", "").strip()
							try:
								d = datetime.datetime.strptime(date, '%a %b %d %Y')
								date = d.strftime('%d/%m/%y')
							except:
								try:
									d = datetime.datetime.strptime(date, '%a %d %b %Y')
									date = d.strftime('%d/%m/%y')
								except:
									pass

							try:
								posted_by = details.find('span', text = re.compile('posted by*', re.IGNORECASE)).findParent().text
								posted_by = posted_by[posted_by.find(":")+1:].replace("Posted by","").strip()
							except:
								pass
					except:
						pass

					try:
						desc = tree.find("div", {"id":"group_post"}).find("p")
						if desc:
							desc = desc.text.strip()
					except:
						pass

					try:
						image_url = tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)
						if image_url:
							href = image_url[0]['href']
							urllib.request.urlretrieve(href, "images/" + str(post_id) + ".jpg")
					except Exception as e:
						print(e.__doc__)
						print(e.args)
						pass

					try:
						row = OrderedDict()

						row['type'] = type
						row['region'] = gu['region']
						row['group'] = gu['group']
						row['loc'] = loc
						row['post_id'] = post_id
						row['title'] = title
						row['date'] = date
						row['time'] = time
						row['posted_by'] = posted_by
						row['desc'] = desc
						row['url'] = pu.replace("\n", "")
						rows.append(row)
					except:
						pass
				if len(rows) > 0:
					file_exists = os.path.isfile('freecycle.csv')
					with open('freecycle.csv', 'a', newline='', encoding='utf-8') as outfile:
						fp = csv.DictWriter(outfile, rows[0].keys())
						if file_exists == False:
							fp.writeheader()
						fp.writerows(rows)

				open('urls_done', 'a').write(gu['group_url'].replace("\n","") + '\n')

	except Exception as e:
		print(e.__doc__)
		print(e.args)

def get_urls():
	try:
		s = requests.session()
		r = s.post(home_url, headers=headers, data=data)
		r = s.get(uk_base_url, headers=headers)

		tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('article', {'id':'active_regions'}))
		regions = tree.findAll('a', {'href':re.compile('http://www.freecycle.org/')})

		region_urls = []
		for r in regions:
			row = {}
			row['region'] = r.text.strip()
			row['region_url'] = r['href']
			region_urls.append(row)

		group_urls = []
		for ru in region_urls:
			r = s.get(ru['region_url'], headers=headers)
			tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('article', {'id':'active_groups'}))
			groups = tree.findAll('a', {'href':re.compile('http://groups.freecycle.org/')})

			for g in groups:
				row = OrderedDict()
				row['region'] = ru['region']
				row['group'] = g.text.strip()
				row['group_url'] = g['href']
				group_urls.append(row)

		with open('freecycle_groups.csv', 'w', newline='') as outfile:
			fp = csv.DictWriter(outfile, group_urls[0].keys())
			fp.writeheader()
			fp.writerows(group_urls)

	except Exception as e:
		print(e.__doc__)
		print(e.args)

def main(argv):
	try:
		process_source = None
		if len(argv) > 1:
			process_source = argv[1]
			if process_source == "URLS":
				get_urls()
			elif process_source == "POSTS":
				get_details()
			else:
				print("Invalid choice, please specify either of URLS or POSTS...")
				exit
		else:
			print("Please specify the choice you wish to run - URLS or POSTS...")
		exit

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main(sys.argv)

