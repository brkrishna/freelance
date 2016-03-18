#-------------------------------------------------------------------------------
# Name:        process_FS
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

        page_content = data.find('div', {'id' : 'content'})
        if page_content != None:
            review_anchors = page_content.find_all('h2', {'class':'post-entry-headline'})
            for review_anchor in review_anchors:
                review_anchor = review_anchor.find('a')
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for movie in unique_anchors:
                row = {}
                if movie != None:

                    response = my_caching.get_content(source_cd, movie)
                    if response != None:

                        soup = BeautifulSoup(response)

                        article = soup.find('div', { 'id' : 'content'})

                        if article != None:

                            name = article.find('h1', {'class':'content-headline'})
                            if name != None:
                                name = name.text.strip()
                                row['name'] = name.strip()

                            row['source_cd'] = source_cd
                            row['rvw_link'] = movie
                            row['rvw_smy'] = ''

                            review = article.find('div', {'class':'entry-content'})
                            if review != None:
                                pColl = review.find_all('p')
                                for r in pColl:
                                    rvw = r.text.strip()
                                    if rvw != '' and row['rvw_smy'] == '':
                                        row['rvw_smy'] = rvw
                                        exit

                                rating_val = 0
                                pColl = review.find_all('h2')
                                for p in pColl:
                                    p_text = p.text.strip()
                                    if 'Ratings' in p_text:
                                        rating_stars = p_text.count('*')
                                        if '1/2' in p_text:
                                            rating_val = rating_stars + 0.5
                                        else:
                                            rating_val = rating_stars

                                if rating_val == 0:
                                    pColl = review.find_all('h1')
                                    for p in pColl:
                                        p_text = p.text.strip()
                                        if 'Ratings' in p_text:
                                            rating_stars = p_text.count('*')
                                            if '1/2' in p_text:
                                                rating_val = rating_stars + 0.5
                                            else:
                                                rating_val = rating_stars

                                        if rating_val > 0:
                                            row['rating'] = rating_val
                                            row['max_rtng'] = 5

                            critic = article.find('span', {'class' :'post-info-author'})
                            if critic != None:
                                row['critic'] = critic.text.strip()

                            year = article.find('span', {'class' :'post-info-date'})
                            if year != None:
                                year = re.findall(r'\d{4}', year.text.strip())
                                row['year'] = year[0]

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


