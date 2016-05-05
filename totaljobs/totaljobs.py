# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         totaljobs
# Purpose:      Parse totaljobs.com for given criteria and save results to zip file
#
# Author:       Ramakrishna
#
# Created:      29/Apr/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, random, os, re, csv
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import html
from zipfile import ZipFile

BASE_URL = 'https://recruiter.totaljobs.com/login?RHP=nav_bar_SignIn'
USER_ID = 'sarah@jenkinsjacob.com'
PASSWD = 'Jj_p@ssword123'
MIN_WAIT = 1
MAX_WAIT = 3
PATH = "/home/ramakrishna/projects/freelance/totaljobs/"
ZIP_FILES = 'zipfiles/'
STAGING = 'staging/'

def main():
	d = None
	f = None
	try:
		f = open('criteria.csv', 'r')
		searches = csv.DictReader(f, delimiter=',')

		profile = FirefoxProfile()
		profile.set_preference("browser.download.panel.shown", False)
		profile.set_preference("browser.download.folderList", 2)
		profile.set_preference("browser.download.dir", PATH + ZIP_FILES)
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/zip')

		d = webdriver.Firefox(profile)

		d.get(BASE_URL)
		#Login
		d.find_element_by_id('pagebody_0_left_0_txtUsername').clear()
		d.find_element_by_id('pagebody_0_left_0_txtUsername').send_keys('sarah@jenkinsjacob.com')
		d.find_element_by_id('pagebody_0_left_0_txtPassword').clear()
		d.find_element_by_id('pagebody_0_left_0_txtPassword').send_keys('Jj_p@ssword123')
		d.find_element_by_id('pagebody_0_left_0_btnSubmit').click()
		time.sleep(random.randint(MIN_WAIT,MAX_WAIT))

		#Navigate to advance search
		for rec in searches:
			try:
				d.find_element_by_partial_link_text('Search for candidates').click()
			except:
				pass
			try:
				d.find_element_by_id('ctl00_cphCentralPanel_LnkNewSearch').click()
			except:
				pass
			try:
				d.find_element_by_partial_link_text('Show advanced search').click()
			except:
				pass

			#enter search criteria from input file
			d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_txtBoolean').send_keys(rec['keywords'].strip())

			try:
				d.find_element_by_partial_link_text('Desired location').click()
				d.find_element_by_class_name('btn-group').click()
				d.find_element_by_partial_link_text(rec['desired_location'].strip()).click()
				d.find_element_by_class_name('btn-group').click()
			except Exception as e:
				print("Invalid entry in Desired location for row ID - " + rec['ID'])
				print(e.__doc__)
				print(e.args)

			try:
				d.find_element_by_xpath('//select[@id="ctl00_cphCentralPanel_ucSearchPart_ddlLastActivity"]/option[text()="' + rec['active_within_last'].strip() + '"]').click()
			except Exception as e:
				print("Invalid entry in Active Within Last for row ID - " + rec['ID'])
				print(e.__doc__)
				print(e.args)
			try:
				if rec['search_in'].lower().strip() == 'job title only':
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_searchTypePart_labelJobTitles').click()
				elif rec['search_in'].lower().strip() == 'profile and cv':
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_searchTypePart_labelProfileAndCV').click()
				else:
					raise('Invalid entry in Search In for row ID - ' + rec['ID'])
			except Exception as e:
				print(e.__doc__)
				print(e.args)

			try:
				if rec['work_eligibility'].lower().strip() == 'all candidates':
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_cblEligibility_0').click()
				elif rec['work_eligibility'].lower().strip() == 'candidates eligible to live and work in the uk':
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_cblEligibility_1').click()
				elif rec['work_eligibility'].lower().strip() == 'candidates eligible to live and work in the eu':
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_cblEligibility_2').click()
				else:
					raise('Invalid entry in Work Eligibility for row ID - ' + rec['ID'])
			except Exception as e:
				print(e.__doc__)
				print(e.args)

			d.find_element_by_id('ctl00_cphCentralPanel_ucSearchPart_btnAdvSearch').click()

			next_page_link = None
			try:
				next_page_link = d.find_element_by_xpath("//li[@class='paging-forward']/a")
			except:
				next_page_link = 'NA' #To allow first page parsing
				pass

			while next_page_link:
				time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
				candidates = d.find_elements_by_class_name('candidate-lnk')
				candidates_count = len(candidates)
				for i in range(0, candidates_count):
					try:
						d.find_element_by_id('ctl00_cphCentralPanel_ucSearchResults_rptResults_ctl0' + str(i) + '_chkSelect').click()
					except:
						pass

				try:
					d.find_element_by_id('ctl00_cphCentralPanel_ucSearchResults_btnDownloadSelected').click()
				except:
					pass

				time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
				next_page_link = None
				try:
					next_page_link = d.find_element_by_xpath("//li[@class='paging-forward']/a")
					next_page_link.click()
				except:
					pass

			try:
				extns = ['zip']
				files = [fn for fn in os.listdir(PATH + ZIP_FILES) if any(fn.endswith(ext) for ext in extns)]
				for file in files:
					with ZipFile(PATH + ZIP_FILES + file, 'r') as myzip:
						myzip.extractall(PATH + STAGING)

				ziph = ZipFile(PATH + rec['ID'] + ".zip", 'w')
				for root, dirs, files in os.walk(PATH + STAGING):
					for file in files:
						ziph.write(os.path.join(root,file), arcname=file)
				ziph.close()

				for root, dirs, files in os.walk(PATH + STAGING):
					for file in files:
						os.remove(PATH + STAGING + file)

				for root, dirs, files in os.walk(PATH + ZIP_FILES):
					for file in files:
						os.remove(PATH + ZIP_FILES + file)

			except Exception as e:
				print(e.__doc__)
				print(e.args)
				pass

	except Exception as e:
		print(e.__doc__)
		print(e.args)
	finally:
		if d:
			d.find_element_by_partial_link_text('Log out').click()
			time.sleep(random.randint(MIN_WAIT,MAX_WAIT))
			d.quit()
		if f:
			f.close()

if __name__ == '__main__':
	main()
