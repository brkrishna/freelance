#-------------------------------------------------------------------------------
# Name:        process_SIFY
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

        page_content = data.find('div', {'class' : 'content-blocks-outer-wrapper'})
        if page_content != None:
            review_anchors = page_content.find_all('div', {'class':'more'})
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

                        page = soup.find('div', {'id':'mreview-article-wrapper'})
                        if page != None:
                            title = page.find('div', {'class':'mreview-heading-wrapper'})
                            if title != None:
                                title = title.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    title = title[:title.find('review')]
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = url
                                row['rvw_smy'] = ''
                                row['rating'] = 0
                                row['year'] = date.today().year
                            else:
                                continue

                            author = page.find('div', {'id':'mreview-admin-name'})
                            if author != None:
                                author = author.text.strip()
                                row['critic'] = author

                            content = page.find('div', {'class':'mreview-article-content-wrapper'})
                            if content != None:
                                pColl = content.find_all('p')
                                rvw_smy = ''
                                rating_val = 0
                                for p in pColl:
                                    review = p.text.strip()

                                    if 'Rating' in p.text.strip():
                                        if 'One' in review:
                                            rating_val = rating_val + 1
                                        if 'Two' in review:
                                            rating_val = rating_val + 2
                                        if 'Three' in review:
                                            rating_val = rating_val + 3
                                        if 'Four' in review:
                                            rating_val = rating_val + 1
                                        if 'half' in review:
                                            rating_val = rating_val + 0.5

                                        if rating_val == 0:
                                            rating = re.findall("\d*\.\d+|\d+", review)
                                            rating_val = rating[0]

                                        if rating_val != '' and row['rating'] == 0:
                                            row['rating'] = rating_val
                                            row['max_rtng'] = 5
                                    else:
                                        rvw_smy = rvw_smy + p.text.strip()

                                rvw_smy = rvw_smy[:500]
                                if rvw_smy != '':
                                    row['rvw_smy'] = rvw_smy

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)