#-------------------------------------------------------------------------------
# Name:        process_SULEKHA
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     17/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
from datetime import date
import re
import my_caching

def process(source_cd, base_url, data):
    try:
        record= []
        anchors = []
        unique_anchors = []

        page_content = data.find('div', {'class' : 'yui-g yuiubugfix'})
        if page_content != None:
            review_anchors = page_content.find_all('div', {'class':'bd'})
            for review_anchor in review_anchors:
                a = review_anchor.find_all('a')
                for link in a:
                    if link != None:
                        anchors.append(link['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'yui-panel panelborder'})
                        if page != None:
                            title = page.find('div', {'class':'hd'})
                            if title != None:
                                title = title.find('h2')
                                if title != None:
                                    title = title.text.strip()
                                    title = title[:title.find('Movie')]
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = url
                                row['rvw_smy'] = ''
                                row['year'] = date.today().year
                            else:
                                continue

                            content = page.find('div', {'id':'blogitem'})
                            if content != None:
                                p = content.find_all('p')
                                for t in p:
                                    if t.text.strip() != '':
                                        row['rvw_smy'] = t.text.strip()
                                        break

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)