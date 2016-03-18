#-------------------------------------------------------------------------------
# Name:        process_FF
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

        page_content = data.find('section', {'class' : 'lhs'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):

                        url = movie['href']
                        if url != None:

                            if 'movie-review' in url:

                                response = my_caching.get_content(source_cd, url)
                                if response != None:

                                    soup = BeautifulSoup(response)

                                    article = soup.find('section', { 'class' : 'lhs Featuredsection'})
                                    if article != None:

                                        name = article.find('h1')
                                        if name != None:
                                            name = name.text.strip()
                                            name = name.replace('Movie Review:', '')
                                            row['name'] = name.strip()

                                        row['source_cd'] = source_cd
                                        row['rvw_link'] = url

                                        review = article.find('div', {'class' :'desc'})
                                        if review != None:
                                            row['rvw_smy'] = review.text.strip()

                                        critic = article.find('span', {'class' :'written'})
                                        if critic != None:
                                            critic = critic.find('a')
                                            if critic != None:
                                                row['critic'] = critic.text.strip()

                                        year = article.find('span', {'class' :'time'})
                                        if year != None:
                                            year = re.findall(r'\d{4}', year.text.strip())
                                            row['year'] = year[0]

                                        rating = article.find('span', {'id' : 'rate_val_change'})
                                        if rating != None:
                                            rating = rating['class']
                                            if rating != None:
                                                rating = rating[0]
                                                rating = re.findall("\d*\.\d+|\d+", rating)

                                                row['rating'] = rating[0]
                                                row['max_rtng'] = 5

                                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


