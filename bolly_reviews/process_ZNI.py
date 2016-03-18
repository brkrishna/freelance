#-------------------------------------------------------------------------------
# Name:        process_ZNI
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

        page_content = data.find('div', {'class' : 'sectionlist'})
        if page_content != None:
            links = page_content.find_all('h3', {'class':'list'})
            for link in links:
                a = link.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:
                        soup = BeautifulSoup(response)
                        page = soup.find('div', {'class':'span10'})
                        if page != None:
                            title = page.find('h1', {'class':'h1title'})
                            if title != None:
                                row = {}
                                title = title.text.strip()
                                if title.find("'") > 0:
                                    title = title[title.find("'") + 1: title.rfind("'")]
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''
                                row['year'] = date.today().year
                            else:
                                continue
                        else:
                            continue

                        last_updated = page.find('div', {'class':'last-updated'})
                        if last_updated != None:
                            year = re.findall(r'\d{4}', last_updated.text.strip())
                            if len(year) > 0:
                                row['year'] = year[0]


                        author = page.find('a', {'rel':'author'})
                        if author != None:
                            row['critic'] = author.text.strip()

                        content = page.find('div', {'class':'content'})
                        if content != None:

                            row['rvw_smy'] = content.text.strip()[:500]

                        rating = content.text.strip()
                        rating = rating[rating.find('readOnly:true,score:') + 20 : rating.find(',', rating.find('readOnly:true,score:') + 20)]

                        if rating != '':
                            row['rating'] = rating
                            row['max_rtng'] = 5

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)