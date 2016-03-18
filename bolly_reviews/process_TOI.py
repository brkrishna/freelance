#-------------------------------------------------------------------------------
# Name:        process_TOI
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

        page_content = data.find('div', {'class' : 'lstpg'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor != None and review_anchor.has_attr('href'):
                    if 'movie-review' in review_anchor['href']:
                        anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:
                        soup = BeautifulSoup(response)
                        page = soup.find('div', {'class':'maintable12'})
                        if page != None:
                            title = page.find('h1')
                            if title != None:
                                row = {}
                                row['name'] = title.text.strip()
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''
                                row['year'] = date.today().year
                            else:
                                continue
                        else:
                            continue

                        byline = page.find('span', {'class':'byline'})
                        if byline != None:
                            byline = byline.text.strip()
                            critic = byline[:byline.find(',')]
                            critic = critic.replace('The Critic has posted comments on this Movie', '')
                            row['critic'] = critic

                            year = re.findall(r'\d{4}', byline)
                            if len(year) > 0:
                                row['year'] = year[0]

                        rating = page.find('div', {'style':'display:inline-block'})
                        if rating != None:
                            spans = rating.find_all('span')
                            for span in spans:
                                if span != None:
                                    if span.has_attr('class'):
                                        rating_val = span['class']
                                        if len(rating_val) > 0:
                                            rating_val = rating_val[0]

                                        if 'rtimg' in rating_val:
                                            rating_val = re.findall(r'\d', rating_val)
                                            if len(rating_val) > 0:
                                                rating_val = int(rating_val[0])

                                            if rating_val > 5:
                                                rating_val = rating_val / 10

                                            row['rating'] = rating_val
                                            row['max_rtng'] = 5


                        content = page.find('div', {'class':'Normal'})
                        if content != None:
                            row['rvw_smy'] = content.text.strip()

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)