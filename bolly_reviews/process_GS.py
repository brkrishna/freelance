#-------------------------------------------------------------------------------
# Name:        process_GS
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

        page_content = data.find('table', {'width' : '98%'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for review_anchor in review_anchors:
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:

                    response = my_caching.get_content(source_cd, base_url + '/movies/reviews/' + url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        article = soup.find('table', { 'width' : '98%'})

                        if article != None:

                            name = article.find('h1', {'itemprop':'headline'})
                            if name != None:
                                name = name.text.strip()
                                row['name'] = name.strip()

                            row['source_cd'] = source_cd
                            row['rvw_link'] = base_url + url
                            row['rvw_smy'] = ''

                            review = article.find('div', {'style':'text-align:justify'})
                            if review != None:
                                review = review.text.strip()
                                review = review[:500]
                                if review != '':
                                    row['rvw_smy'] = review

                            rating_val = article.find('span', {'itemprop':'ratingValue'})
                            if rating_val != None:
                                rating_val = rating_val.text.strip()
                                if rating_val != '':
                                    row['rating'] = rating_val
                                    row['max_rtng'] = 5

                            critic = article.find('font', {'color' :'#606060'})
                            if critic != None:
                                critic = critic.text.strip()

                                row['critic'] = critic

                            year = article.find('font', {'class' :'newsdate'})
                            if year != None:
                                year = re.findall(r'\d{4}', year.text.strip())
                                row['year'] = year[0]

                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


