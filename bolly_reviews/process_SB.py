#-------------------------------------------------------------------------------
# Name:        process_SB
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

        page_content = data.find('div', {'class' : 'bollywood-left-div bollywood-left-w'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor.has_attr('href'):
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'content-div-left'})
                        if page != None:
                            title = page.find('h2')
                            if title != None:
                                title = title.text.strip()
                                if title.find("'"):
                                    title = title[title.find("'") + 1: title.rfind("'")]
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''
                                row['rating'] = 0
                                row['year'] = ''
                            else:
                                continue

                            author = page.find('div', {'id':'author'})
                            if author != None:
                                author = author.text.strip().replace('By', '')
                                row['critic'] = author[:author.find(',')]

                            r_date = page.find('div', {'id':'pubdate'})
                            if r_date != None:
                                year = re.findall(r'\d{4}', r_date.text.strip())
                                if len(year) > 0:
                                    row['year'] = year[0]

                            pColl = page.find_all('p')
                            rvw_smy = ''
                            rating_val = 0
                            for p in pColl:

                                rvw_smy = rvw_smy + p.text.strip()

                                review = p.text.strip()

                                if 'Rating' in p.text.strip():
                                    rating_stars = p.text.count('*')
                                    if '1/2' in p.text:
                                        rating_val = rating_stars + 0.5
                                    else:
                                        rating_val = rating_stars

                                    if rating_val > 0 and row['rating'] == 0:
                                        row['rating'] = rating_val
                                        row['max_rtng'] = 5

                            rvw_smy = rvw_smy[:500]
                            if rvw_smy != '':
                                row['rvw_smy'] = rvw_smy

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)