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

        page_content = data.find('div', {'class' : 'GPcontanier'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'rel':'bookmark'})
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
                            if soup != None:

                                page = soup.find('div', {'class':'gossipeDetail'})
                                if page != None:
                                    title = page.find('h1', {'class':'heading'})
                                    if title != None:
                                        title = title.text.strip()
                                        title = title.replace('Review', '')
                                        row['name'] = title
                                        row['source_cd'] = source_cd
                                        row['rvw_link'] = url
                                        row['rvw_smy'] = ''

                                    author = page.find('span', {'class':'entry-author'})
                                    if author != None:
                                        if author != None:
                                            row['critic'] = author.text.strip()

                                    year = page.find('div', {'class':'dateNtime'})
                                    if year != None:
                                            year = year.text.strip()
                                            year = re.findall(r'\d{4}', year)
                                            if len(year) > 0:
                                                row['year'] = year[0]
                                            else:
                                                row['year'] = date.today().year

                                    pColl = page.find_all('p')
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

                                            if 'Star cast:' in review:
                                                p_text = review.split(',')

                                                if p_text[0] != None:
                                                    #get rid of start cast note
                                                    actor1 = p_text[0][10:]
                                                    row['actor1'] = actor1.strip()

                                                if p_text[1] != None:
                                                    row['actor2'] = p_text[1].strip()

                                                if len(p_text) >= 3:
                                                    row['actor3'] = p_text[2].strip()

                                            if 'Director:' in review:
                                                row['director'] = review[10:].strip()

                                            if 'Watch or Not?' in review:
                                                row['rvw_smy'] = review
                                                break

                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


