#-------------------------------------------------------------------------------
# Name:        process_IT
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

        page_content = data.find('div', {'class' : 'leftnav'})
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

                            page = soup.find('div', {'class':'strleft'})
                            if page != None:
                                title = page.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    title = title.replace('Movie review:', '')
                                    row['name'] = title
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = base_url + url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'class':'strstrap'})
                            if author != None:
                                if author != None:
                                    critic = author.find('span')
                                    critic = critic.text.strip()
                                    row['critic'] = critic

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
                                            if '/star.gif' in img['src']:
                                                rating_val = rating_val + 1
                                            elif '/halfstar.gif' in img['src']:
                                                rating_val = rating_val + 0.5

                                        if rating_val != '':
                                            row['rating'] = rating_val
                                            row['max_rtng'] = 5

                                    elif review != '' and row['rvw_smy'] == '':
                                        row['rvw_smy'] = review
                                        break

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


