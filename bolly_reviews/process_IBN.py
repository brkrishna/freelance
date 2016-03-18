#-------------------------------------------------------------------------------
# Name:        process_IBN
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

        page_content = data.find('div', {'id' : 'news_mid'})
        if page_content != None:
            review_anchors = page_content.find_all('h2')
            for review_anchor in review_anchors:
                a = review_anchor.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    if not 'now-showing' in url:
                        response = my_caching.get_content(source_cd, url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'id':'aleft_box'})
                            if page != None:
                                title = page.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    row['name'] = title
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'id':'btbox'})
                            if author != None:
                                content = author.find('span', {'class':'fwb'})
                                if content != None:
                                    content = content.text.strip()
                                    critic = content[:content.find(',')]
                                    row['critic'] = critic

                                year = author.find('div', {'class':'blbox'})
                                if year != None:
                                    year = re.findall(r'\d{4}', year.text.strip())
                                    row['year'] = year[0]

                            article = page.find('div', { 'id' : 'atxt_box'})

                            if article != None:

                                pColl = article.find_all('p')
                                if pColl != None:
                                    for p in pColl:

                                        review = p.text.strip()

                                        rating_val = 0
                                        if 'Rating' in review:

                                            rating_stars = review[8:review.find('/')]
                                            if rating_stars != '':
                                                rating_val = rating_stars

                                            if rating_val != '':
                                                row['rating'] = rating_val
                                                row['max_rtng'] = 5
                                                break

                                        if review != '' and rating_val == 0:
                                            row['rvw_smy'] = review

                                record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


