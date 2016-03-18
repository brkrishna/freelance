#-------------------------------------------------------------------------------
# Name:        process_RM
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

        page_content = data.find('div', {'class' : 'have-you-seen'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'have-you-seen'})
                        if page != None:
                            title = page.find('h3')
                            if title != None:
                                title = title.text.strip()
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = url
                                row['critic'] = 'Rajeev Masand'
                                row['rvw_smy'] = ''
                                row['year'] = ''
                            else:
                                continue

                        pColl = page.find_all('p')
                        rvw_smy = ''
                        rating_val = 0
                        for p in pColl:

                            rvw_smy = rvw_smy + p.text.strip()

                            review = p.text.strip()
                            year = re.findall(r'\d{4}', review)
                            if len(year) > 0 and row['year'] == '':
                                row['year'] = year[0]

                            if 'Rating' in p.text.strip():
                                img = p.find('img')
                                if img != None:
                                    rating_val = img['alt']

                                if rating_val != '':
                                    row['rating'] = rating_val
                                    row['max_rtng'] = 5

                        rvw_smy = rvw_smy[100:500]
                        if rvw_smy != '':
                            row['rvw_smy'] = rvw_smy

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)