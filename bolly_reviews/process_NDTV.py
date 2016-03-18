#-------------------------------------------------------------------------------
# Name:        process_NDTV
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

        page_content = data.find('div', {'class' : 'story_list'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'class':'linka12bld'})
            for review_anchor in review_anchors:
                anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'story_body'})
                        if page != None:
                            title = page.find('h1', {'class':'pageheadlineh1'})
                            if title != None:
                                title = title.find('i').text.strip()
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''

                        author = page.find('span', {'id':'MainContent_lb_StoryBy'})
                        if author != None:
                            row['critic'] = author.text.strip()

                        year = page.find('span', {'id':'MainContent_lb_PostedDate'})
                        if year != None:
                            year = year.text.strip()
                            if year != None:
                                year = re.findall(r'\d{4}', year)
                                if len(year) > 0:
                                    row['year'] = year[0]

                        rating_val = 0
                        rating_stars = page.find('span', {'id': 'MainContent_lb_Rating'})
                        if rating_stars != None:
                            imgs = rating_stars.find_all('img')
                            for img in imgs:
                                if 'star0.gif' in img['src']:
                                    rating_val = rating_val + 1
                                elif 'star1.gif' in img['src']:
                                    rating_val = rating_val + 0.5

                            if rating_val != '':
                                row['rating'] = rating_val
                                row['max_rtng'] = 5

                        review = page.find('div', {'id': 'MainContent_lb_StoryFull'})
                        if review != None:
                            rvw_smy = review.text.strip()
                            rvw_smy = rvw_smy[:500]
                            if rvw_smy != '':
                                row['rvw_smy'] = rvw_smy

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


