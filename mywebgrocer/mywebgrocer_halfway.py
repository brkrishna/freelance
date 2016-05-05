# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:		 parser
# Purpose:
#
# Author:	   Ramakrishna
#
# Dated:		07/Mar/2016
# Copyright:	(c) Ramakrishna 2016
# Licence:	  <your licence>
#-------------------------------------------------------------------------------
import csv, re, datetime, sys, time
import os.path
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

start_url = 'http://shop.mywebgrocer.com/shop.aspx?strid=5F3D126398'

def search(process_url):
	d = None
	try:
		'''
		dc = DesiredCapabilities.HTMLUNIT
		dc['permissions.default.image'] = 2
		'''
		#binary = FirefoxBinary("C:\\Users\\Administrator\\Desktop\\Tor Browser\\Browser\\firefox.exe")
		binary = FirefoxBinary("C:\\Users\\Administrator\\Desktop\\Tor Browser\\Browser\\firefox.exe")v
		d = webdriver.Firefox(firefox_binary=binary)

		#d = webdriver.Firefox()
		time.sleep(20)
		d.get(start_url)

		finished_terms = []

		if os.path.isfile('mwg_terms'):
			finished_terms = set(open('mwg_terms').read().splitlines())
			finished_terms = list(finished_terms)

		term = ''
		h1_term = h2_term = h3_term = h4_term = ''

		d.switch_to_default_content()
		d.switch_to.frame(d.find_element_by_name('MidFrame'))
		d.switch_to.frame(d.find_element_by_name('MenuFrame'))
		ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
		h1s = ul.find_elements_by_tag_name('h1')
		start = 0
		end = round(len(h1s)/2)
		for h1 in range(start, end):
			try:
				d.switch_to_default_content()
				d.switch_to.frame(d.find_element_by_name('MidFrame'))
				d.switch_to.frame(d.find_element_by_name('MenuFrame'))
				ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
				h1s = ul.find_elements_by_tag_name('h1')

				h1s[h1].click()
				term = h1s[h1].text.strip() + ";"
				h1_term = h1s[h1].text.strip()
				h2s = h1s[h1].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h2')
				for h2 in range(0, len(h2s)-1):

					d.switch_to_default_content()
					d.switch_to.frame(d.find_element_by_name('MidFrame'))
					d.switch_to.frame(d.find_element_by_name('MenuFrame'))
					ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
					h1s = ul.find_elements_by_tag_name('h1')
					h2s = h1s[h1].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h2')

					h2s[h2].click()
					term += h2s[h2].text.strip() + ";"
					h2_term = h2s[h2].text.strip()
					h3s = h2s[h2].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h3')
					for h3 in range(0, len(h3s)-1):


						d.switch_to_default_content()
						d.switch_to.frame(d.find_element_by_name('MidFrame'))
						d.switch_to.frame(d.find_element_by_name('MenuFrame'))
						ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
						h1s = ul.find_elements_by_tag_name('h1')
						h2s = h1s[h1].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h2')
						h3s = h2s[h2].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h3')

						h3s[h3].click()
						term += h3s[h3].text.strip() + ";"
						h3_term = h3s[h3].text.strip()
						h4s = h3s[h3].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h4')
						if h4s:
							for h4 in range(0, len(h4s)-1):

								d.switch_to_default_content()
								d.switch_to.frame(d.find_element_by_name('MidFrame'))
								d.switch_to.frame(d.find_element_by_name('MenuFrame'))
								ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
								h1s = ul.find_elements_by_tag_name('h1')
								h2s = h1s[h1].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h2')
								h3s = h2s[h2].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h3')
								h4s = h3s[h3].find_element_by_xpath('..').find_element_by_xpath('..').find_elements_by_tag_name('h4')

								term += h4s[h4].text.strip() + ";"
								h4_term = h4s[h4].text.strip()
								h4s[h4].click()

								try:
									d.switch_to_default_content()
									d.switch_to.frame(d.find_element_by_name('MidFrame'))
									d.switch_to.frame(d.find_element_by_name('MainFrame'))
									a_next = d.find_element_by_id('btnNext_top')
								except:
									a_next = "runOnce"
									pass

								while a_next != None:
									try:
										rows = []
										main_window = d.current_window_handle
										d.switch_to_default_content()
										d.switch_to.frame(d.find_element_by_name('MidFrame'))
										d.switch_to.frame(d.find_element_by_name('MainFrame'))
										plinks = d.find_elements_by_class_name('ProductItem')

										for i in range(0, len(plinks)-1):
											try:

												main_window = d.current_window_handle
												d.switch_to_default_content()
												d.switch_to.frame(d.find_element_by_name('MidFrame'))
												d.switch_to.frame(d.find_element_by_name('MainFrame'))
												plinks = d.find_elements_by_class_name('ProductItem')
												if term + plinks[i].get_attribute('id') + ";" in finished_terms:
													continue
												with open('mwg_terms', 'a') as f:
													f.write(term + plinks[i].get_attribute('id') + ";" + "\n")
												try:
													elem = plinks[i].find_element_by_tag_name('a')
												except:
													break

												row = OrderedDict()
												row['catg'] = h1_term
												row['dept'] = h2_term
												row['sub_dept'] = h3_term
												row['sub_sub_dept'] = h4_term

												elem.send_keys(Keys.CONTROL + Keys.RETURN)
												d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
												time.sleep(1)
												second_window = d.current_window_handle
												d.switch_to_window(second_window)

												d.switch_to_default_content()
												d.switch_to.frame(d.find_element_by_name('MidFrame'))
												d.switch_to.frame(d.find_element_by_name('MainFrame'))
												time.sleep(1)
												soup = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('body'))

												try:
													row['brand'] = soup.find('b', {'class':'ProductDetail-Brand'}).text.replace("\n","").strip()
												except:
													row['brand'] = ''
													pass
												try:
													row['product_name'] = soup.find('b', {'class':'ProductDetail-ProductName'}).text.replace("\n","").strip()
												except:
													row['product_name'] = ''
													pass
												try:
													temp =soup.find('b', {'class':'sm'}).parent.text.replace("\n","").strip()
													row['size'] = temp[:temp.find("SKU/UPC:")].strip().encode("ascii", "replace")
													row['upc'] = temp[temp.find("SKU/UPC:")+8:].strip()
												except:
													row['size'] = ''
													row['upc'] = ''
													pass
												try:
													row['prod_img_src'] = soup.find('div', {'class':'imgWrapper'}).find('img').get('src')
												except:
													row['prod_img_src'] = ''
													pass

												rows.append(row)

												d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
												d.switch_to_window(main_window)

											except (NoSuchElementException, StaleElementReferenceException) as e:
												print(e.__doc__)
												print(e.args)
												continue

										if len(rows) > 0:
											file_exists = os.path.isfile('mywebgrocer.csv')
											with open('mywebgrocer.csv', 'a', newline='', encoding='utf-8') as outfile:
												fp = csv.DictWriter(outfile, rows[0].keys())
												if file_exists == False:
													fp.writeheader()
												fp.writerows(rows)

										try:
											a_next = None
											d.switch_to_default_content()
											d.switch_to.frame(d.find_element_by_name('MidFrame'))
											d.switch_to.frame(d.find_element_by_name('MainFrame'))
											a_next = d.find_element_by_id('btnNext_top')
											if a_next:
												a_next.click()
										except:
											a_next = None
											pass

									except Exception as e:
										print(e.__doc__)
										print(e.args)
										pass
						else:
							try:
								d.switch_to_default_content()
								d.switch_to.frame(d.find_element_by_name('MidFrame'))
								d.switch_to.frame(d.find_element_by_name('MainFrame'))
								a_next = d.find_element_by_id('btnNext_top')
							except:
								a_next = "runOnce"

							while a_next != None:
								try:
									rows = []
									main_window = d.current_window_handle
									d.switch_to_default_content()
									d.switch_to.frame(d.find_element_by_name('MidFrame'))
									d.switch_to.frame(d.find_element_by_name('MainFrame'))
									plinks = d.find_elements_by_class_name('ProductItem')

									for i in range(0, len(plinks)-1):
										try:

											main_window = d.current_window_handle
											d.switch_to_default_content()
											d.switch_to.frame(d.find_element_by_name('MidFrame'))
											d.switch_to.frame(d.find_element_by_name('MainFrame'))
											plinks = d.find_elements_by_class_name('ProductItem')

											if term + plinks[i].get_attribute('id') + ";"  in finished_terms:
												continue

											with open('mwg_terms', 'a') as f:
												f.write(term + plinks[i].get_attribute('id') + ";" + "\n")

											try:
												elem = plinks[i].find_element_by_tag_name('a')
											except IndexError:
												break

											row = OrderedDict()
											row['catg'] = h1_term
											row['dept'] = h2_term
											row['sub_dept'] = h3_term
											row['sub_sub_dept'] = h4_term

											elem.send_keys(Keys.CONTROL + Keys.RETURN)
											d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
											time.sleep(1)
											second_window = d.current_window_handle
											d.switch_to_window(second_window)

											d.switch_to_default_content()
											d.switch_to.frame(d.find_element_by_name('MidFrame'))
											d.switch_to.frame(d.find_element_by_name('MainFrame'))
											time.sleep(1)
											soup = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('body'))

											try:
												row['brand'] = soup.find('b', {'class':'ProductDetail-Brand'}).text.replace("\n","").strip()
											except:
												row['brand'] = ''
												pass
											try:
												row['product_name'] = soup.find('b', {'class':'ProductDetail-ProductName'}).text.replace("\n","").strip()
											except:
												row['product_name'] = ''
												pass
											try:
												temp =soup.find('b', {'class':'sm'}).parent.text.replace("\n","").strip()
												row['size'] = temp[:temp.find("SKU/UPC:")].strip().encode("ascii", "replace")
												row['upc'] = temp[temp.find("SKU/UPC:")+8:].strip()
											except:
												row['size'] = ''
												row['upc'] = ''
												pass
											try:
												row['prod_img_src'] = soup.find('div', {'class':'imgWrapper'}).find('img').get('src')
											except:
												row['prod_img_src'] = ''
												pass

											rows.append(row)

											d.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
											d.switch_to_window(main_window)

										except (NoSuchElementException, StaleElementReferenceException) as e:
											print(e.__doc__)
											print(e.args)
											continue

									if len(rows) > 0:
										file_exists = os.path.isfile('mywebgrocer.csv')
										with open('mywebgrocer.csv', 'a', newline='', encoding='utf-8') as outfile:
											fp = csv.DictWriter(outfile, rows[0].keys())
											if file_exists == False:
												fp.writeheader()
											fp.writerows(rows)

									try:
										a_next = None
										d.switch_to_default_content()
										d.switch_to.frame(d.find_element_by_name('MidFrame'))
										d.switch_to.frame(d.find_element_by_name('MainFrame'))
										a_next = d.find_element_by_id('btnNext_top')
										if a_next:
											a_next.click()
									except:
										a_next = None
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
		if d != None:
			d = None

def main():
	search(start_url)

if __name__ == '__main__':
	main()