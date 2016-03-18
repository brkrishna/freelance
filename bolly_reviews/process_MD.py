#-------------------------------------------------------------------------------
# Name:        process_MD
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

        page_content = data.find('div', {'class' : 'moviereview MT15'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                        response = my_caching.get_content(source_cd, base_url + url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'class':'article_detail'})
                            if page != None:
                                title = page.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    title = title.replace('Movie Review:', '')
                                    title = title.replace("'", '')
                                    row['name'] = title.strip()
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = base_url + url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'class':'metalink'})
                            if author != None:
                                if author != None:
                                    author = author.text.strip()
                                    critic = author[author.find('By') + 3 : author.find('|')]
                                    year = re.findall(r'\d{4}', author)
                                    if len(year) > 0:
                                        row['year'] = year[0]
                                    else:
                                        row['year'] = date.today().year

                                    row['critic'] = critic

                            articleBody = page.find('span', {'itemprop': 'articleBody'})
                            if articleBody != None:
                                pColl = articleBody.find_all('p')
                                if pColl != None:
                                    for p in pColl:

                                        review = p.text.strip()

                                        rating_val = 0
                                        if 'Rating' in review:
                                            img = p.find('img')
                                            if img != None:
                                                rating_stars = img['src']
                                                if rating_stars != None:
                                                    rating_stars = rating_stars[rating_stars.rfind('/'):]
                                                    if rating_stars != None:
                                                        rating = re.findall("\d*\.\d+|\d+", rating_stars)

                                            if rating != '':
                                                if len(rating) > 0:
                                                    row['rating'] = rating[0]
                                                    row['max_rtng'] = 5

                                        '''
                                        if 'Cast:' in review:
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
                                        '''

                                        if review != '':
                                            row['rvw_smy'] = review

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


