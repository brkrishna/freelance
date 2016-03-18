#-------------------------------------------------------------------------------
# Name:        process_MM
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

        page_content = data.find('div', {'class' : 'leftpart'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'class':'linkstryone'})
            for review_anchor in review_anchors:
                if review_anchor != None and 'Film-review' in review_anchor['href']:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                        response = my_caching.get_content(source_cd, base_url + url)
                        if response != None:

                            soup = BeautifulSoup(response)

                            page = soup.find('div', {'class':'leftpart'})
                            if page != None:
                                title = page.find('h1')
                                if title != None:
                                    title = title.text.strip()
                                    title = title.replace('Film review: ', '')
                                    row['name'] = title
                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = base_url + url
                                    row['rvw_smy'] = ''

                            author = page.find('div', {'class':'Normal'})
                            if author != None:
                                if author != None:
                                    critic = author.find('strong')
                                    critic = critic.text.strip()
                                    row['critic'] = critic

                                    review = author.text.strip()
                                    if review != None:
                                        review = review.replace(critic, '')
                                        review = review.replace('By: ', '')
                                        review = review[:500]
                                        row['rvw_smy'] = review

                            year = page.find('span' , {'class': 'byline'})
                            if year != None:
                                year = re.findall(r'\d{4}', year.text.strip())
                                if len(year) > 0:
                                    row['year'] = year[0]


                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


