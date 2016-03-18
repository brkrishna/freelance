#-------------------------------------------------------------------------------
# Name:        process_OI
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

        page_content = data.find('div', {'class' : 'collection-page-second-part-left'})
        if page_content != None:
            review_anchors = page_content.find_all('div', {'class':'collection'})
            for review_anchor in review_anchors:
                a = review_anchor.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'content_left'})
                        if page != None:
                            title = page.find('h1', {'class':'articleheading'})
                            if title != None:
                                title = title.text.strip()
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''

                        author = page.find('a', {'rel':'author'})
                        if author != None:
                            row['critic'] = author.text.strip()

                        year = page.find('div', {'class':'date_time'})
                        if year != None:
                            year = year.text.strip()
                            if year != None:
                                year = re.findall(r'\d{4}', year)
                                if len(year) > 0:
                                    row['year'] = year[0]

                        rating_val = 0
                        rating_stars = page.find('span', {'class': 'rating-value'})
                        if rating_stars != None:
                            rating_val = rating_stars.text.strip()

                            if rating_val != '':
                                row['rating'] = rating_val
                                row['max_rtng'] = 5

                        review = page.find('div', {'class': 'new_main_story_width'})
                        if review != None:
                            pColl = review.find_all('p')
                            rvw_smy = ''
                            for p in pColl:
                                rvw_smy = rvw_smy + p.text.strip()

                            rvw_smy = rvw_smy[:500]
                            if rvw_smy != '':
                                row['rvw_smy'] = rvw_smy

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


