#-------------------------------------------------------------------------------
# Name:        process_SH
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

        page_content = data.find('div', {'id' : 'articleListing'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor.has_attr('href'):
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:

                        soup = BeautifulSoup(response)
                        if soup != None:
                            page = soup.find('div', {'id':'SHPH1_musicLeftColumn'})
                            if page != None:
                                title_div = page.find('div', {'id':'aRATitle'})
                                if title_div != None:
                                    a = title_div.find('a')
                                    if a != None:
                                        title = a.text.strip()
                                        if title != None:
                                            row = {}
                                            row['name'] = title
                                            row['source_cd'] = source_cd
                                            row['rvw_link'] = base_url + url
                                            row['rvw_smy'] = ''
                                            row['year'] = date.today().year
                                        else:
                                            continue
                                else:
                                    continue

                                article = page.find('div', {'id':'articleContainer'})
                                if article != None:
                                    p = article.find('p')
                                    if p != None:
                                        rvw_smy = p.text.strip()

                                    if rvw_smy != '':
                                        row['rvw_smy'] = rvw_smy

                                    article = article.text.strip()
                                    if article != None:
                                        row['critic'] = article[article.find('By') + 3 : article.find('\n', article.find('By'))]

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)