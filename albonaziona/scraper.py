# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         albonazionalegestoriambientali_it
# Purpose:      Parse linked in given a list of companies and write users to a csv file
#
# Author:       Ramakrishna
#
# Created:      21/Feb/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from lxml import html
import time, random, os, re
import sqlite3

MIN_WAIT = 3
MAX_WAIT = 5
URL = 'http://www.albonazionalegestoriambientali.it/ElenchiIscritti.aspx'

SECTIONS = ['13', '21', '17', '18', '15', '8', '6', '12', '7', '3', '11', '14', '1', '16', '20', '19', '9', '4', '10', '2', '5']

def main():
    d = conn = None
    try:
        #server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
        #dc = DesiredCapabilities.HTMLUNIT

        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        #d = webdriver.Remote(server_url, dc)
        d = webdriver.Firefox()
        d.get(URL)
        for section in SECTIONS:
            try:
                d.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlSezioni"]/option[@value="' + section + '"]').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))

                d.find_element_by_xpath('//*[@id="risultatiPerPagina"]/option[@value="100"]').click()
                d.find_element_by_id('btnCerca').click()
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                page = 1
                curr_url = d.current_url
                dettaglis = d.find_elements_by_xpath("//div[@id='divListaImprese']//input[@value='Dettagli']")
                dettaglis_length = len(dettaglis) - 1

                for i in range(0, dettaglis_length):
                    dettaglis = d.find_elements_by_xpath("//div[@id='divListaImprese']//input[@value='Dettagli']")
                    time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                    try:
                        det = dettaglis[i]
                        if det and det.is_displayed():
                            det.click()
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        continue

                    try:
                        time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                        dettagli_details = d.find_elements_by_xpath("//input[@value='Dettagli']")

                        for det_b in dettagli_details:
                            try:
                                if det_b.is_displayed():
                                    det_b.click()
                                else:
                                    continue
                            except Exception as e:
                                print(e.__doc__)
                                print(e.args)
                                pass
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    try:
                        tree = html.fromstring(d.page_source.encode('utf-8'))
                        impresa = p_iscrizione = n_iscrizione = denominazione = codicefiscale = via = cap = comune = sigla_provincia = ''
                        name_address = tree.xpath("//div[@id='divResultArea']/div/text()[normalize-space()]")
                        try:
                            #impresa = int(d.current_url[d.current_url.rfind("=")+1:])
                            impresa = re.search("[0-9]{3,8}", tree.xpath("//input[@value='Dettagli']/@onclick")[0]).group()
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            continue
                        try:
                            p_iscrizione = re.search("[A-Z]{2}(\/)?", name_address[0]).group()[:2]
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                        try:
                            n_iscrizione = re.search("(\/)?[0-9]{1,6}", name_address[0]).group()[1:].strip()
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                        try:
                            if name_address[1].find('"') > 0:
                                res = re.search(r'\"(.+?)\"', name_address[1])
                                denominazione = res.group().replace('"', '').strip()
                            else:
                                 denominazione = name_address[1].strip()
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                        try:
                            codicefiscale = name_address[2].replace("\n", "").replace("\t","").strip()
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                        try:
                            via = name_address[3].replace("\n", "").replace("\t","").strip()
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                        try:
                            res = name_address[4].replace("\n", "").replace("\t","").strip()
                            cap = re.search("[0-9]{5}", res).group().strip()
                            res = res.replace(cap, "")
                            sigla_provincia = re.search("\([A-Z]{2}\)", res).group()
                            res = res.replace(sigla_provincia, "")
                            comune = res.strip()
                            sigla_provincia = sigla_provincia.replace("(", "").replace(")", "")
                        except Exception as e:
                            print(e.__doc__)
                            print(e.args)
                            pass
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        sql = "insert into companies(impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia) values"
                        sql += "(?,?,?,?,?,?,?,?,?)"
                        cur.execute(sql, (impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia,))
                        print("companies impresa - " + str(impresa))
                    except sqlite3.IntegrityError as e:
                        continue
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    try:
                        trs = tree.xpath("//div[@id='divResultArea']/div/table[@class='tableListe']//tr")

                        row = {}
                        for r in range(1, len(trs)):
                            for i in range(0,9):
                                column = trs[0].xpath("th")[i]
                                value = trs[r].xpath("td")[i]
                                row[column.xpath("./text()")[0]] = value.xpath("./text()")[0].strip() if value.xpath("./text()") else ''
                                row['impresa'] = str(impresa)
                            keys, values = row.keys(), row.values()
                            sql = "insert into categories (" + ",".join(keys).lower().replace(" ", "_")  + ") values (?,?,?,?,?,?,?,?,?,?) "
                            cur.execute(sql, tuple(row.values()))
                        print("categories")
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    try:
                        records = ()
                        rows = []
                        trs = tree.xpath("//div[@id='divCerListDetail' or @id='divCPListDetail']/table//tr")
                        if len(trs) > 0:
                            for tr in trs:
                                records = tuple(tr.xpath("*/text()"))
                                if records != None:
                                    rows.append((str(impresa),) + records)
                            sql = "insert into cer_own_account (impresa, codice, descrizione) values (?,?,?) "
                            if len(rows) > 0:
                            	cur.executemany(sql, rows)
                        print("cer_own_account")
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    try:
                        '''media list'''
                        records = ()
                        rows = []
                        d.find_element_by_xpath('//select[@class="itemsPerPage"]/option[@value="100"]').click()
                        time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                        tree = html.fromstring(d.page_source)
                    except:
                        pass

                    try:
                        trs = tree.xpath("//div[@id='divMezziList']/div[2]/div/table[@class='tableListe']//tr")
                        if len(trs) > 0:
                            for tr in trs:
                                records = tuple(tr.xpath("*/text()"))
                                if records != None:
                                    rows.append((str(impresa),) + records)
                            sql = "insert into media_list (impresa, targa, tipo_mezzo, catg_attive) values (?,?,?,?) "
                            if len(rows) > 0:
                                cur.executemany(sql, rows)
                        print("media_list")
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    try:
                        next_page = d.find_element_by_xpath("//li[@class='selected page']/following-sibling::li[@class='gotoPage page']")
                        while next_page:
                            next_page.click()
                            time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                            tree = html.fromstring(d.page_source)
                            records = ()
                            rows = []

                            trs = tree.xpath("//div[@id='divMezziList']/div[2]/div/table[@class='tableListe']//tr")
                            if len(trs) > 0:
                                for tr in trs:
                                    records = tuple(tr.xpath("*/text()"))
                                    if records != None:
                                        rows.append((str(impresa),) + records)
                                sql = "insert into media_list (impresa, targa, tipo_mezzo, catg_attive) values (?,?,?,?) "
                                if len(rows) > 0:
                                    cur.executemany(sql, rows)

                            next_page = None
                            try:
                                next_page = d.find_element_by_xpath("//li[@class='selected page']/following-sibling::li[@class='gotoPage page']")
                            except:
                                break

                        print("media_list")
                        '''media list end'''
                    except:
                        pass

                    conn.commit()

                    try:
                        d.find_element_by_id('divTornaAllaListaImprese').click()

                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                print("page - " + str(page))
                new_url = curr_url.replace("paginaCorrente=" + str(page - 1), "paginaCorrente=" + str(page))
                print(new_url)
                d.get(new_url)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                dettaglis = d.find_elements_by_xpath("//div[@id='divListaImprese']//input[@value='Dettagli']")
                if dettaglis == None:
                    continue

            except Exception as e:
                print(e.__doc__)
                print(e.args)
                continue

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        if d != None:
        	d.quit()
        	d = None
        if conn != None:
        	conn.commit()
        	conn = None

if __name__ == '__main__':
	main()