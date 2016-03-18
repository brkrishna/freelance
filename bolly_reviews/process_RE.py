#-------------------------------------------------------------------------------
# Name:        process_RE
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

        page_content = data.find('div', {'class' : 'column1 gridPanel grid8'})
        if page_content != None:
            review_anchors = page_content.find_all('span', {'class':'inlineLinks'})
            for review_anchor in review_anchors:
                a = review_anchor.find_all('a')
                if a != None:
                    for p in a:
                        if p != None and 'movie-review' in p['href']:
                            anchors.append(p['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'class':'moduleBody'})
                        if page != None:
                            title = page.find('h2')
                            if title != None:
                                title = title.text.strip()
                                title = title.replace('Movie Review:', '')
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = url
                                row['rvw_smy'] = ''

                        author = page.find('div', {'class':'author'})
                        if author != None:
                            author = author.text.strip()
                            author = author.replace('By', '')
                            row['critic'] = author.strip()

                        year = page.find('div', {'class':'timestamp'})
                        if year != None:
                            year = year.text.strip()
                            if year != None:
                                year = re.findall(r'\d{4}', year)
                                if len(year) > 0:
                                    row['year'] = year[0]

                        review = page.find('div', {'id': 'postcontent'})
                        if review != None:
                            pColl = review.find_all('p')
                            rvw_smy = ''
                            for p in pColl:
                                rvw_smy = rvw_smy + p.text.strip()

                            rvw_smy = rvw_smy[rvw_smy.find(')') + 1 :500]
                            if rvw_smy != '':
                                row['rvw_smy'] = rvw_smy

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)