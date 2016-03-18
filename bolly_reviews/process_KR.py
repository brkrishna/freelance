#-------------------------------------------------------------------------------
# Name:        process_KM
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

        page_content = data.find('li', {'id' : 'recent-posts-2'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                        response = my_caching.get_content(source_cd, url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'class':'entry-content'})
                            if page != None:
                                row['name'] = ''
                                row['rvw_smy'] = ''

                                pColl = page.find_all('p')
                                if pColl != None:
                                    for p in pColl:

                                        review = p.text.strip()

                                        if row['name'] == '':
                                            row['name'] = review
                                            row['source_cd'] = source_cd
                                            row['rvw_link'] = url
                                            row['year'] = date.today().year
                                            row['critic'] = 'Komal Nahta'

                                        elif row['rvw_smy'] == '':
                                            row['rvw_smy'] = review
                                            break


                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


