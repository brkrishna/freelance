#-------------------------------------------------------------------------------
# Name:        process_REDIFF
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

        page_content = data.find('div', {'class' : 'newleftcontainer'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        page = soup.find('div', {'id':'leftcontainer'})
                        if page != None:
                            title = page.find('h1', {'itemprop':'headline'})
                            if title != None:
                                title = title.text.strip()
                                title = title.replace('Review:', '')
                                row['name'] = title.strip()
                                row['source_cd'] = source_cd
                                row['rvw_link'] = url
                                row['rvw_smy'] = ''
                            else:
                                continue

                        year = page.find('div', {'class':'sm1 grey1'})
                        if year != None:
                            year = year.text.strip()
                            if year != None:
                                year = re.findall(r'\d{4}', year)
                                if len(year) > 0:
                                    row['year'] = year[0]

                        pColl = page.find_all('p')
                        rvw_smy = ''
                        rating_val = 0
                        for p in pColl:
                            rvw_smy = rvw_smy + p.text.strip()

                            if 'Rating' in p.text.strip():
                                imgs = p.find_all('img')
                                for img in imgs:
                                    if 'ratinghalf' in img['src']:
                                        rating_val = rating_val + 0.5
                                    elif '/rating1' in img['src']:
                                        rating_val = rating_val + 1
                                    elif '/rating1half' in img['src']:
                                        rating_val = rating_val + 1.5
                                    elif '/rating2' in img['src']:
                                        rating_val = rating_val + 2
                                    elif '/rating2half' in img['src']:
                                        rating_val = rating_val + 2.5
                                    elif '/rating3' in img['src']:
                                        rating_val = rating_val + 3
                                    elif '/rating3half' in img['src']:
                                        rating_val = rating_val + 3.5
                                    elif '/rating4' in img['src']:
                                        rating_val = rating_val + 4
                                    elif '/rating4half' in img['src']:
                                        rating_val = rating_val + 4.5
                                    elif '/rating5' in img['src']:
                                        rating_val = rating_val + 5

                                if rating_val != '':
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