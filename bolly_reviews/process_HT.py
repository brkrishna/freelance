#-------------------------------------------------------------------------------
# Name:        process_HT
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

        page_content = data.find('div', {'class' : 'listing_pg_pad'})
        if page_content != None:
            review_anchors = page_content.find_all('div', {'class':'read_more'})
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

                        article = soup.find('div', { 'class' : 'story_wid'})

                        if article != None:

                            name = article.find('h1', {'class':'sty_head_30'})
                            if name != None:
                                name = name.text.strip()
                                name = name.replace('Movie review:', '')
                                row['name'] = name.strip()

                            row['source_cd'] = source_cd
                            row['rvw_link'] = url
                            row['rvw_smy'] = ''

                            review = article.find('div', {'class':'sty_txt'})
                            if review != None:
                                pColl = review.find_all('p')
                                if pColl != None:
                                    for p in pColl:
                                        review = p.text.strip()
                                        if review != '':
                                            row['rvw_smy'] = review

                                        rating_val = 0
                                        if 'Rating' in review:

                                            rating_stars = review.count('*')
                                            if '1/2' in review:
                                                rating_val = rating_stars + 0.5
                                            else:
                                                rating_val = rating_stars

                                            if rating_val > 0:
                                                row['rating'] = rating_val
                                                row['max_rtng'] = 5


                            critic = article.find('span', {'class' :'sty_agn'})
                            if critic != None:
                                critic = critic.text.strip()
                                critic = critic.replace(', Hindustan Times', '')
                                row['critic'] = critic

                            year = article.find('div', {'class' :'sty_pub'})
                            if year != None:
                                year = re.findall(r'\d{4}', year.text.strip())
                                row['year'] = year[0]

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


