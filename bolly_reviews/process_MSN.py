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

        page_content = data.find('ul', {'class' : 'imglinkabslist1 cf'})
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
                            if soup != None:

                                page = soup.find('div', {'class':'article1'})
                                if page != None:
                                    title = page.find('h1')
                                    if title != None:
                                        title = title.text.strip()
                                        title = title.replace('Review: ', '')
                                        title = title.replace("'", "")
                                        row['name'] = title
                                        row['source_cd'] = source_cd
                                        row['rvw_link'] = url
                                        row['rvw_smy'] = ''

                                    author = page.find('span', {'class':'author'})
                                    if author != None:
                                        if author != None:
                                            critic = author.text.strip()
                                            critic = critic.replace(',', '')
                                            row['critic'] = critic

                                    year = page.find('span' , {'class': 'date'})
                                    if year != None:
                                        year = re.findall(r'\d{4}', year.text.strip())
                                        if len(year) > 0:
                                            row['year'] = year[0]

                                    review = page.find('div', {'class': 'articlebody'})
                                    if review != None:
                                        pColl = review.find_all('p')
                                        if pColl != None:
                                            for p in pColl:
                                                review = p.text.strip()
                                                if review != '':
                                                    row['rvw_smy'] = review
                                                    break

                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


