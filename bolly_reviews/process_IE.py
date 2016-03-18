#-------------------------------------------------------------------------------
# Name:        process_IE
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

        page_content = data.find('div', {'class' : 'top-release'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

        page_content = data.find('div', {'class' : 'lead-stories listing'})
        if page_content != None:
            review_anchors = page_content.find_all('h6')
            for review_anchor in review_anchors:
                a = review_anchor.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                        response = my_caching.get_content(source_cd, url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'class':'story-details nobg'})
                            if page != None:
                                title = page.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    title = title.replace('Movie Review: ', '')
                                    row['name'] = title.strip()
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'class':'editor'})
                            if author != None:
                                content = author.find('a')
                                if content != None:
                                    critic = content.text.strip()
                                    row['critic'] = critic

                                year = re.findall(r'\d{4}', author.text.strip())
                                row['year'] = year[0]

                            review = page.find('div', { 'class' : 'text'})
                            if review != None:
                                row['rvw_smy'] = review.text.strip()

                            rating_val = 0
                            rating_stars = page.find('div', {'class': 'story-rating'})
                            if rating_stars != None:
                                imgs = rating_stars.find_all('img')
                                for img in imgs:
                                    if 'star-one-1.png' in img['src']:
                                        rating_val = rating_val + 1
                                    elif 'star-half-1.png' in img['src']:
                                        rating_val = rating_val + 0.5

                                if rating_val != '':
                                    row['rating'] = rating_val
                                    row['max_rtng'] = 5

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


