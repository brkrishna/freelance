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

MIN_WAIT = 2
MAX_WAIT = 5

url  = 'http://www.albonazionalegestoriambientali.it/ElenchiIscritti.aspx#tipoRicerca=9&idImpresa='

def main():
    d = conn = None
    try:
        server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
        dc = DesiredCapabilities.HTMLUNIT

        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        results = cur.execute("select impresa from impresas where done = 0 order by impresa")
        impresa_list = results.fetchall()

        d = webdriver.Remote(server_url, dc)
        #d = webdriver.Firefox()
        #impresa_list = [('176169'), ('23980'),]
        for impresa in impresa_list:
            try:
                link = url + impresa[0]
                print(link)
                d.get(link)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
            except Exception as e:
                print(e.__doc__)
                print(e.args)
                break

            try:
                dettagli_details = d.find_elements_by_xpath("//input[@value='Dettagli']")
                for det_b in dettagli_details:
                    try:
                        if det_b.is_displayed():
                            det_b.click()
                            time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
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
                impresa = p_iscrizione = n_iscrizione = denominazione = codicefiscale = via = cap = comune = sigla_provincia = raw_text = ''
                name_address = tree.xpath("//div[@id='divResultArea']/div/text()[normalize-space()]")
                raw_text = "$$$".join(tree.xpath("//div[@id='divResultArea']/div/text()[normalize-space()]")).replace("\n", "").replace("\t","").strip()
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

                try:
                    sql = "insert into companies(impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia, raw_text) values"
                    sql += "(?,?,?,?,?,?,?,?,?,?)"
                    cur.execute(sql, (impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia, raw_text,))
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
                        for i in range(0,10):
                            column = trs[0].xpath("th")[i]
                            value = trs[r].xpath("td")[i]
                            row[column.xpath("./text()")[0].strip()] = value.xpath("./text()")[0].strip() if value.xpath("./text()") else ''
                            row['impresa'] = str(impresa)
                        #row['raw_text'] = "$$$".join(value.xpath("./text()[normalize-space()]")[0].strip()).replace("\n", "").replace("\t","").strip()
                        keys, values = row.keys(), row.values()
                        column_names = ",".join(keys).lower().strip().replace(" ", "_")
                        sql = "insert into categories (" + column_names + ") values (?,?,?,?,?,?,?,?,?,?,?) "
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
                            records = tuple(r.strip() for r in records)
                            #raw_text = "$$$".join(records)
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
                    tree = html.fromstring(d.page_source.encode('utf-8'))
                except:
                    pass

                try:
                    trs = tree.xpath("//div[@id='divMezziList']/div[2]/div/table[@class='tableListe']//tr")
                    if len(trs) > 0:
                        for tr in trs:
                            records = tuple(tr.xpath("*/text()[normalize-space()]"))
                            records = tuple(r.strip() for r in records)
                            if records != None:
                                rows.append((str(impresa),) + records + ("$$$".join(records),))
                        sql = "insert into media_list (impresa, targa, tipo_mezzo, catg_attive,raw_text) values (?,?,?,?,?) "
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
                        tree = html.fromstring(d.page_source.encode('utf-8'))
                        records = ()
                        rows = []

                        trs = tree.xpath("//div[@id='divMezziList']/div[2]/div/table[@class='tableListe']//tr")
                        if len(trs) > 0:
                            for tr in trs:
                                records = tuple(tr.xpath("*/text()[normalize-space()]"))
                                records = tuple(r.strip() for r in records)
                                if records != None:
                                    rows.append((str(impresa),) + records + ("$$$".join(records),))
                            sql = "insert into media_list (impresa, targa, tipo_mezzo, catg_attive, raw_text) values (?,?,?,?,?) "
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

                cur.execute("update impresas set done = 1 where impresa = ? and done  = 0", (impresa[0],))
                conn.commit()

            except Exception as e:
                print(e.__doc__)
                print(e.args)

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