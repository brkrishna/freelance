#-------------------------------------------------------------------------------
# Name:        process_IG
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

        page_content = data.find('table', {'width' : '95%'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'class':'red'})
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

                            page = soup.find('div', {'style':'float:right;width:650px;margin-top:5px'})
                            if page != None:
                                title = page.find('h2')
                                if title != None:
                                    title = title.text.strip()
                                    title = title[:title.find('-')].strip()
                                    row['name'] = title
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['rvw_smy'] = ''

                            author = page.find('td', {'class':'black'})
                            if author != None:
                                author = author.text.strip()
                                content = author[:author.find('[')]
                                if content != None:
                                    critic = content.strip()
                                    if 'document.write' in critic:
                                        critic = critic[critic.find('<i>') + 3: critic.find('</i>')]
                                        row['critic'] = critic

                                year = re.findall(r'\d{4}', author)
                                row['year'] = year[0]

                                pColl = page.find_all('p', {'align':'justify'})
                                if pColl != None:
                                    for p in pColl:

                                        review = p.text.strip()

                                        rating_val = 0
                                        if 'Rating' in review:

                                            rating_stars = review.count('*')
                                            if '1/2' in review:
                                                rating_val = rating_stars + 0.5
                                            else:
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


