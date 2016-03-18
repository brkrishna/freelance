#-------------------------------------------------------------------------------
# Name:        process_FP
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

        page_content = data.find('div', {'id' : 'main'})
        if page_content != None:
            review_anchors = page_content.find_all('h3')
            for review_anchor in review_anchors:
                review_anchor = review_anchor.find('a')
                if review_anchor != None:
                    anchors.append(review_anchor['href'])

            unique_anchors = set(anchors)

            for movie in unique_anchors:
                row = {}
                if movie != None:

                    response = my_caching.get_content(source_cd, movie)
                    if response != None:

                        soup = BeautifulSoup(response)
                        if soup != None:

                            author = soup.find('div', {'id':'author'})
                            if author != None:
                                author = author.find('h3')
                                if author != None:
                                    row['critic'] = author.text.strip()
                                    row['year'] = date.today().year

                            article = soup.find('article', { 'id' : 'single'})

                            if article != None:

                                name = article.find('h1', {'class':'inner_title MT10'})
                                if name != None:
                                    name = name.text.strip()
                                    row['name'] = name.strip()

                                row['source_cd'] = source_cd
                                row['rvw_link'] = movie

                                review = article.find('div', {'class':'stry_cont'})
                                if review != None:
                                    review = review.find('p')
                                    if review != None:
                                        row['rvw_smy'] = review.text.strip()

                                critic = article.find('a', {'rel' :'author'})
                                if critic != None:
                                    row['critic'] = critic.text.strip()

                                year = article.find('span', {'class' :'date_ago '})
                                if year != None:
                                    year = re.findall(r'\d{4}', year.text.strip())
                                    row['year'] = year[0]

                                record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


