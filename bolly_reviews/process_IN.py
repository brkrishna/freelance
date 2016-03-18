#-------------------------------------------------------------------------------
# Name:        process_IN
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

        page_content = data.find('div', {'class' : 'archives'})
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

                            page = soup.find('div', {'class':'mid-box-2 left'})
                            if page != None:
                                title = page.find('h3')
                                if title != None:
                                    title = title.text.strip()
                                    title = title[:title.find('Review')]
                                    row['name'] = title.strip()
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'class':'post'})
                            if author != None:
                                author = author.text.strip()
                                year = re.findall(r'\d{4}', author)
                                row['year'] = year[0]

                            pColl = page.find_all('p')
                            if pColl != None:
                                for p in pColl:

                                    review = p.text.strip()
                                    rating_val = 0
                                    if 'Rating' in review:

                                        imgs = p.find_all('img')
                                        for img in imgs:
                                            if '/star.png' in img['src']:
                                                rating_val = rating_val + 1
                                            elif '/halfstar.png' in img['src']:
                                                rating_val = rating_val + 0.5

                                        if rating_val != '':
                                            row['rating'] = rating_val
                                            row['max_rtng'] = 5
                                            break


                                    if review != '' and row['rvw_smy'] == '':
                                        row['rvw_smy'] = review

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


