#-------------------------------------------------------------------------------
# Name:        scrape
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     17/05/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, time, re
from BeautifulSoup import BeautifulSoup, SoupStrainer
from datetime import datetime
import connect_db
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

SCRAPING_REQUEST_STAGGER = 1.5 # in seconds
BASE_URL = 'http://www.albogestoririfiuti.it/ElenchiIscritti.aspx#tipoRicerca=9&idImpresa=189755'

'''
SECTIONS = ['Abruzzo',
'Alto Adige',
'Basilicata',
'Calabria',
'Campania',
'Emilia Romagna',
'Friuli Venezia Giuli',
'Lazio',
'Liguria',
'Lombardia',
'Marche',
'Molise',
'Piemonte',
'Puglia',
'Sardegna',
'Sicilia',
'Toscana',
'Trentino',
'Umbria',
'Val d''Aosta',
'Veneto']
'''

SECTIONS = ['Abruzzo', 'Calabria', 'Campania', 'Emilia Romagna', 'Friuli Venezia Giuli']

start_pager = -1

def process():
    try:

        #driver = webdriver.Firefox()
        driver = webdriver.PhantomJS('phantomjs')
        driver.get(BASE_URL)
        time.sleep(SCRAPING_REQUEST_STAGGER)
        print(BASE_URL)
        connect_db.main()

        count_sections = len(SECTIONS)
        i = 0
        for i in range(i, count_sections):

            pager = 1
            td_counter = 0

            try:
                driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlSezioni"]/option[text()="' + SECTIONS[i] + '"]').click()
                driver.find_element_by_id('btnCerca').click()
            except NoSuchElementException as e:
                print(e.__doc__)
                print(e.args)
                pass

            time.sleep(SCRAPING_REQUEST_STAGGER)

            try:
                titles = driver.find_elements_by_xpath('/html/body/form/div[3]/div/div[6]/div[2]/div[2]/div[4]/table/tbody/tr/td')
            except NoSuchElementException as e:
                print(e.__doc__)
                print(e.args)
                pass

            if start_pager > 0:
                try:
                    pager = start_pager
                    pager += 1
                    for j in range(1, pager):
                        next_page = driver.find_element_by_css_selector('div.pager:nth-child(8) > div:nth-child(' + str(j) + ')')
                        next_page.click()
                        time.sleep(SCRAPING_REQUEST_STAGGER)

                    #next_page.click()
                    #time.sleep(SCRAPING_REQUEST_STAGGER)
                    titles = driver.find_elements_by_xpath('/html/body/form/div[3]/div/div[6]/div[2]/div[2]/div[4]/table/tbody/tr/td')
                    td_counter = 0
                    dettagli_counter = -1
                except NoSuchElementException as e:
                    titles = None


            while titles != None:

                row = {}
                row['section'] = SECTIONS[i]
                row['sno'] = ''
                row['name'] = ''
                row['add1'] = ''
                row['add2'] = ''
                row['cat'] = ''
                row['regn'] = ''
                row['d_n1'] = ''
                row['d_n2'] = ''
                row['d_n3'] = ''
                row['d_n4'] = ''

                dettagli_counter = -1
                val = titles[td_counter].text
                while val != None:
                    val = val.strip() + '$$$'
                    if 'Dettagli' in val or val.find('$$$') == 0:
                        td_counter += 1
                        val = get_next(td_counter, titles)
                        continue
                    else:

                        val = val.replace('$$$', '')
                        print('page - ' + str(pager) + ' td_counter - ' + str(td_counter) +  ' val - ' + val)

                        if row['name'] == '':
                            sno = val[:val.find('\n')]
                            if sno != '':
                                row['sno'] = int(sno)

                            val = val[val.find('\n') + 2 :]
                            row['name'] = val[val.find('-') + 1:].strip()
                            row['regn'] = val[:val.find('-')].strip()
                            td_counter += 1
                            val = get_next(td_counter, titles)
                            continue

                        if row['add1'] == '':
                            row['add1'] = val
                            td_counter += 1
                            val = get_next(td_counter, titles)
                            continue

                        if row['add2'] == '':
                            row['add2'] = val
                            td_counter += 1
                            val = get_next(td_counter, titles)
                            continue

                        if row['cat'] == '' and 'Categorie:' in val:
                            row['cat'] = val[val.find('Categorie:') + 10 :].strip()

                            try:
                                dettagli_counter += 4
                                driver.find_element_by_xpath('/html/body/form/div[3]/div/div[6]/div[2]/div[2]/div[4]/table/tbody/tr[' + str(dettagli_counter) + ']/td[2]/input').click()
                            except NoSuchElementException as e:
                                break

                            time.sleep(SCRAPING_REQUEST_STAGGER)
                            elem = driver.find_element_by_css_selector('#divDettaglioImpresaSuccess')
                            if elem != None:
                                el = elem.text.replace('\n', '$$$')
                                el = el[:el.find('Categorie:')].strip()

                                print('el - ' + el)
                                temp = el[el.find('$$$') + 3 :]

                                row['d_n1'] = temp[:temp.find('$$$')]
                                temp = temp.replace(row['d_n1'] + '$$$', '')

                                row['d_n2'] = temp[:temp.find('$$$')]
                                temp = temp.replace(row['d_n2'] + '$$$', '')

                                if temp[:3] == '$$$':
                                    temp = temp[3:]

                                row['d_n3'] = temp[:temp.find('$$$')]
                                temp = temp.replace(row['d_n3'] + '$$$', '')

                                row['d_n4'] = temp[:temp.find('$$$')]

                            driver.back()

                            connect_db.at_lines(row)
                            time.sleep(SCRAPING_REQUEST_STAGGER)
                            try:
                                titles = driver.find_elements_by_xpath('/html/body/form/div[3]/div/div[6]/div[2]/div[2]/div[4]/table/tbody/tr/td')
                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                pass

                            td_counter += 1
                            val = get_next(td_counter, titles)
                            if val == None:
                                titles = None
                                break


                            row['section'] = SECTIONS[i]
                            row['sno'] = ''
                            row['name'] = ''
                            row['add1'] = ''
                            row['add2'] = ''
                            row['cat'] = ''
                            row['regn'] = ''
                            row['d_n1'] = ''
                            row['d_n2'] = ''
                            row['d_n3'] = ''
                            row['d_n4'] = ''

                try:
                    pager += 1
                    next_page = driver.find_element_by_css_selector('div.pager:nth-child(8) > div:nth-child(' + str(pager) + ')')
                    next_page.click()
                    time.sleep(SCRAPING_REQUEST_STAGGER)
                    titles = driver.find_elements_by_xpath('/html/body/form/div[3]/div/div[6]/div[2]/div[2]/div[4]/table/tbody/tr/td')
                    td_counter = 0
                    dettagli_counter = -1
                except NoSuchElementException as e:
                    titles = None

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        driver.quit()
        connect_db.close()

def get_next(counter, titles):
    try:
        try:
            val = titles[counter]
            if val != None:
                val = val.text
                return val

        except NoSuchElementException as e:
            return None
    except Exception as e:
        print(e.__doc__)
        print(e.args)

def main():
    process()

if __name__ == '__main__':
    main()

