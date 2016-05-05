# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:		    MIS
# Purpose:      Gets the MIS statistics of mywebgrocer
#
# Author:	    Ramakrishna
#
# Dated:		27/Mar/2016
# Copyright:	(c) Ramakrishna 2016
# Licence:	    <your licence>
#-------------------------------------------------------------------------------
import csv, re, datetime, sys, time, random
import os.path
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#import socks, socket

#socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
#socket.socket = socks.socksocket

MIN = 1
MAX = 2

start_url = 'http://shop.mywebgrocer.com/shop.aspx?strid=5F3D126398'
h1_term = h2_term = h3_term = h4_term = ''
h1s = h2s = h3s = h4s = None

def switch_to(d):
	global h1s, h2s, h3s, h4s, h1_term, h2_term, h3_term, h4_term
	try:
		time.sleep(random.randint(MIN, MAX))
		d.switch_to.default_content()
		d.switch_to.frame(d.find_element_by_name('MidFrame'))
		d.switch_to.frame(d.find_element_by_name('MenuFrame'))
		ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
		try:
			h1s = ul.find_elements_by_tag_name('h1')
		except Exception as e:
			print(e.__doc__)
			print(e.args)
			print("h1s not found...")
			pass

	except Exception as e:
		print(e.__doc__)
		print(e.args)
		pass

def search(process_url):
	d = None
	global h1s, h2s, h3s, h4s, h1_term, h2_term, h3_term, h4_term
	try:
		#binary = FirefoxBinary("C:\\Users\\Administrator\\Desktop\\Tor Browser\\Browser\\firefox.exe")
		#d = webdriver.Firefox(firefox_binary=binary)
		#d = webdriver.Firefox()
		service_args = ['--proxy=127.0.0.1:9050', '--proxy-type=socks5']
		d = webdriver.PhantomJS(service_args=service_args)

		finished_terms = []

		if os.path.isfile('mwg_terms'):
			finished_terms = set(open('mwg_terms').read().splitlines())
			finished_terms = list(finished_terms)

		d.get(start_url)

		switch_to(d)
		start = 0
		end = len(h1s)

		for h1 in range(start, end):
			try:
				switch_to(d)
				h1s[h1].click()
				h1_term = h1s[h1].text.strip()
				h2s = h1s[h1].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h2')

				for h2 in range(0, len(h2s)):
					switch_to(d)
					h2s[h2].click()
					h2_term = h2s[h2].text.strip()
					h3s = h2s[h2].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h3')

					rows = []
					for h3 in range(0, len(h3s)):
						switch_to(d)
						h3s[h3].click()
						h3_term = h3s[h3].text.strip()
						h4s = h3s[h3].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h4')

						if h4s:
							for h4 in range(0, len(h4s)):
								try:
									switch_to(d)
									h4s[h4].click()
									h4_term = h4s[h4].text.strip()

									d.switch_to.default_content()
									d.switch_to.frame(d.find_element_by_name('MidFrame'))
									d.switch_to.frame(d.find_element_by_name('MainFrame'))

									try:
										a_next = d.find_element_by_id('btnNext_top')
									except Exception as e:
										a_next = "runOnce"
										print(e.__doc__)
										print(e.args)
										pass

									while a_next != None:
										try:
											rows = []
											main_window = d.current_window_handle
											d.switch_to.default_content()
											d.switch_to.frame(d.find_element_by_name('MidFrame'))
											d.switch_to.frame(d.find_element_by_name('MainFrame'))

											product_items = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'class': re.compile(r"(ProductItem |ProductItem ProductOnSale)")}))
											terms = []
											for p in product_items:

												term = h1_term + ";" + h2_term + ";" + h3_term + ";" + h4_term + ";" + p.get('id') + ";"
												if term in finished_terms:
													continue
												else:
													terms.append(term)

												row = OrderedDict()
												row['catg'] = h1_term
												row['dept'] = h2_term
												row['sub_dept'] = h3_term
												row['sub_sub_dept'] = h4_term
												try:
													row['product_id'] = p.get('id')
												except:
													continue # Can't take a product without its ID
												try:
													row['brand'] = p.find('div', {'class':'ProductBrand'}).text.replace("\n","").strip()
												except:
													row['brand'] = ''
													pass
												try:
													row['product_name'] = p.find('div', {'class':'ProductName'}).text.replace("\n","").strip()
												except:
													row['product_name'] = ''
													pass
												try:
													row['size'] = p.find('div', {'class':'ProductQuantity'}).find('span').text.replace("\n","").strip()
												except:
													row['size'] = ''
													pass
												try:
													row['prod_img_src'] = p.find('img', {'class':'ImgLink'}).get('src')
												except:
													row['prod_img_src'] = ''
													pass
												try:
													row['product_url'] = p.find('div', {'class':'Image'}).find('a').get('href')
												except:
													row['product_url'] = ''

												rows.append(row)

											if len(rows) > 0:
												file_exists = os.path.isfile('mywebgrocer.csv')
												with open('mywebgrocer.csv', 'a', newline='', encoding='utf-8') as outfile:
													fp = csv.DictWriter(outfile, rows[0].keys())
													if file_exists:
														fp.writeheader()
													fp.writerows(rows)

											if len(terms) > 0:
												with open('mwg_terms', 'a') as f:
													f.write("\n".join(terms) + "\n")

											try:
												a_next = None
												d.switch_to.default_content()
												d.switch_to.frame(d.find_element_by_name('MidFrame'))
												d.switch_to.frame(d.find_element_by_name('MainFrame'))
												a_next = d.find_element_by_id('btnNext_top')
												if a_next:
													a_next.click()
											except Exception as e:
												a_next = None
												pass
										except Exception as e:
											print(e.__doc__)
											print(e.args)
											pass
								except Exception as e:
									print(e.__doc__)
									print(e.args)
									pass
						else:
							try:
								switch_to(d)
								d.switch_to.default_content()
								d.switch_to.frame(d.find_element_by_name('MidFrame'))
								d.switch_to.frame(d.find_element_by_name('MainFrame'))

								try:
									a_next = d.find_element_by_id('btnNext_top')
								except Exception as e:
									a_next = "runOnce"
									print(e.__doc__)
									print(e.args)
									pass

								while a_next != None:
									try:
										rows = []
										main_window = d.current_window_handle
										d.switch_to.default_content()
										d.switch_to.frame(d.find_element_by_name('MidFrame'))
										d.switch_to.frame(d.find_element_by_name('MainFrame'))

										product_items = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'class': re.compile(r"(ProductItem |ProductItem ProductOnSale)")}))
										terms = []
										for p in product_items:

											term = h1_term + ";" + h2_term + ";" + h3_term + ";" + h4_term + ";" + p.get('id') + ";"
											if term in finished_terms:
												continue
											else:
												terms.append(term)

											row = OrderedDict()
											row['catg'] = h1_term
											row['dept'] = h2_term
											row['sub_dept'] = h3_term
											row['sub_sub_dept'] = h4_term
											try:
												row['product_id'] = p.get('id')
											except:
												continue # Can't take a product without its ID
											try:
												row['brand'] = p.find('div', {'class':'ProductBrand'}).text.replace("\n","").strip()
											except:
												row['brand'] = ''
												pass
											try:
												row['product_name'] = p.find('div', {'class':'ProductName'}).text.replace("\n","").strip()
											except:
												row['product_name'] = ''
												pass
											try:
												row['size'] = p.find('div', {'class':'ProductQuantity'}).find('span').text.replace("\n","").strip()
											except:
												row['size'] = ''
												pass
											try:
												row['prod_img_src'] = p.find('img', {'class':'ImgLink'}).get('src')
											except:
												row['prod_img_src'] = ''
												pass
											try:
												row['product_url'] = p.find('div', {'class':'Image'}).find('a').get('href')
											except:
												row['product_url'] = ''

											rows.append(row)

										if len(rows) > 0:
											file_exists = os.path.isfile('mywebgrocer.csv')
											with open('mywebgrocer.csv', 'a', newline='', encoding='utf-8') as outfile:
												fp = csv.DictWriter(outfile, rows[0].keys())
												if file_exists:
													fp.writeheader()
												fp.writerows(rows)

										if len(terms) > 0:
											with open('mwg_terms', 'a') as f:
												f.write("\n".join(terms) + "\n")

										try:
											a_next = None
											d.switch_to.default_content()
											d.switch_to.frame(d.find_element_by_name('MidFrame'))
											d.switch_to.frame(d.find_element_by_name('MainFrame'))
											a_next = d.find_element_by_id('btnNext_top')
											if a_next:
												a_next.click()
										except Exception as e:
											a_next = None
											pass
									except Exception as e:
										print(e.__doc__)
										print(e.args)
										pass
							except Exception as e:
								print(e.__doc__)
								print(e.args)
								pass

			except (Exception, KeyboardInterrupt) as e:
				print(e.__doc__)
				print(e.args)
				continue

	except (Exception, KeyboardInterrupt) as e:
		print(e.__doc__)
		print(e.args)
	finally:
		if d:
			d = None

def main():
	search(start_url)

if __name__ == '__main__':
	main()