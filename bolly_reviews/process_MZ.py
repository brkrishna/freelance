#-------------------------------------------------------------------------------
# Name:        process_MZ
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

        page_content = data.find('div', {'class' : 'hollywood_middle_container border_radius'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'rel':'nofollow'})
            for review_anchor in review_anchors:
                anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                        response = my_caching.get_content(source_cd, url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'class':'posts-single'})
                            if page != None:
                                title = page.find('h2')
                                if title != None:
                                    title = title.text.strip()
                                    row['name'] = title
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['rvw_smy'] = ''

                            metadata = page.find('div', {'class':'categories-single'})
                            if metadata != None:
                                if metadata != None:
                                    critic = metadata.find('a')
                                    if critic != None:
                                        critic = critic.text.strip()
                                        row['critic'] = critic

                                year = metadata.text.strip()
                                if year != None:
                                    year = re.findall(r'\d{4}', year)
                                    if len(year) > 0:
                                        row['year'] = year[0]

                            review = page.find('div', {'class': 'postdescription-single'})
                            if review != None:
                                pColl = review.find_all('p')
                                if pColl != None:
                                    for p in pColl:
                                        rvw_smy = p.text.strip()
                                        if rvw_smy != '':
                                            row['rvw_smy'] = rvw_smy

                                pColl = review.find_all('li')
                                if pColl != None:
                                    for p in pColl:
                                        p = p.text.strip()
                                        if 'Ratings' in p:
                                            rating = p[p.find(':') + 1 : p.find('/')]
                                            if rating != '':
                                                row['rating'] = rating
                                                row['max_rtng'] = 5
                                                break

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


