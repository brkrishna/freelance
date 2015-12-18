# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:        parser
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     08/09/2015
# Copyright:   (c) Ramakrishna 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sqlite3, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import urllib

BASE_URL = 'https://www.getpopulrrewards.com'

def main():
    conn = driver = None
    try:
        driver = webdriver.Firefox()

        conn = sqlite3.connect("gppr.db3")
        cur = conn.cursor()

        cur.execute("select id, catg, subcatg from links where done = 0 order by id")

        review_urls = cur.fetchall()

        driver.get('https://www.getpopulrrewards.com')
        time.sleep(3)

        for url in review_urls:
            id = url[0]
            catg = url[1]
            subcatg = url[2]
            next_page = ''
            print catg, subcatg
            try:
                driver.find_element_by_link_text('SHOP ALL').click()
                time.sleep(1)
                driver.find_element_by_link_text(catg).click()
                time.sleep(1)
                driver.find_element_by_link_text(subcatg).click()
                time.sleep(1)
            except NoSuchElementException as e:
                print(e.__doc__)
                print(e.args)
                pass

            try:
                main_window = driver.current_window_handle

                try:
                    pager = driver.find_element_by_class_name("pagination")
                    lis = pager.find_elements_by_tag_name("li")
                    if lis != None and len(lis) >= 3:
                        l = lis[3]
                        if l.find_element_by_tag_name('a') != None:
                            next_page = l.find_element_by_tag_name('a')
                        else:
                            next_page = '' # empty string as we want it to loop through the first page
                except NoSuchElementException as e:
                    next_page = ''
                    print(e.__doc__)
                    print(e.args)
                    pass

                while next_page != None:

                    links = driver.find_elements_by_class_name("shortDescription")
                    time.sleep(1)
                    for link in links:
                        name = points = item_no = prod_url = descr = notes = None

                        elem = link.find_element_by_tag_name('a')

                        elem.send_keys(Keys.CONTROL + Keys.RETURN)
                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
                        time.sleep(1)
                        second_window = driver.current_window_handle
                        driver.switch_to_window(second_window)

                        soup = BeautifulSoup(driver.page_source, parse_only=SoupStrainer('body'))
                        if soup != None:

                            try:
                                div_name = soup.find('span', {'id':'itemName'})
                                if div_name != None:
                                    name = div_name.text.strip()
                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                print "name not found"
                                pass

                            try:
                                div_item_no = soup.find('span', {'id':'itemNo'})
                                if div_item_no != None:
                                    item_no = div_item_no.text

                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                print "item no not found"
                                pass

                            selected = soup.find('div', {'state':'selected'})
                            if selected != None:
                                url = selected['style']
                                prod_url = url[url.find("https"):url.find("?")]

                                #Save image locally
                                urllib.urlretrieve(prod_url, "images/" + item_no + ".jpg")

                            try:
                                desc = soup.find('div', {'id':'itemDescr'})
                                if desc != None:
                                    descr = desc.getText("$$$")
                                    '''
                                    for d in desc.contents:
                                        if d != None:
                                            d = str(d)
                                            descr += d.strip() if d != None else ''
                                    '''
                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                print "desc not found"
                                pass
                            '''
                            try:
                                note = soup.find('div', {'class':'itemSummary'})
                                if note != None:
                                    note = note.contents
                                    for n in note:
                                        n = n.text.encode('ascii', 'ignore').decode('ascii').replace('\n','').strip()
                                        notes += n + " "
                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                print "item summary not found"
                                pass
                            '''
                            try:
                                div_points = soup.find_all('p', {'class':'points'})
                                if div_points != None:
                                    for p in div_points:

                                        if p.text.strip() != '':
                                            points = p.text.strip()
                                            break

                            except NoSuchElementException as e:
                                print(e.__doc__)
                                print(e.args)
                                print "points not found"
                                pass

                            sql = "insert into records(name, catg, subcatg, points, item_no, img_url, descr) values (?,?,?,?,?,?,?)"
                            #print name, catg, subcatg, points, item_no, prod_url, descr
                            print catg, subcatg, name
                            if name != None and points != None and item_no != None and prod_url != None:
                                cur.execute(sql, (name, catg, subcatg, points, item_no, prod_url, descr))

                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                        time.sleep(1)

                    driver.switch_to_window(main_window)

                    cur.execute("update links set done = 1 where id = ? and done = 0", (str(id),))
                    conn.commit()

                    try:
                        next_page = None
                        pager = driver.find_element_by_class_name("pagination")
                        lis = pager.find_elements_by_tag_name("li")
                        if lis != None and len(lis) >= 3:
                            l = lis[3]
                            if l.find_element_by_tag_name('a') != None:
                                next_page = l.find_element_by_tag_name('a')
                                next_page.click()
                            else:
                                next_page = None

                    except IndexError as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    except NoSuchElementException as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                driver.switch_to_window(main_window)

            except NoSuchElementException as e:
                print(e.__doc__)
                print(e.args)
                pass

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        if conn != None:
            conn.commit()
            conn.close()
        if driver != None:
            driver.close()

if __name__ == '__main__':
    main()

