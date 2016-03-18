#-------------------------------------------------------------------------------
# Name:        process_BS
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

        review_anchors = data.find_all('a', {'class' : 'darkbluelink1'})
        if review_anchors != None:
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):
                        url = movie['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('table', { 'style' : 'line-height:15px'})
                                if article != None:

                                    name = article.find('h3')
                                    if name != None:
                                        row['source_cd'] = source_cd
                                        row['name'] = movie.text.strip()
                                        row['rvw_link'] = url

                                    #Year
                                    row['year'] = date.today().year

                                    #rating
                                    img = article.find('span', { 'class' : 'red'})
                                    if img != None:
                                        rtng = img.text[:img.text.find('/')]
                                        if rtng != '':
                                            row['rating'] = rtng

                                    #max_rating
                                    row['max_rtng'] = 5

                                    # Review
                                    r = article.find('td', { 'class' : 'blacktext12'})
                                    if r != None:
                                        r = r.text.strip()
                                        row['rvw_smy'] = r

                                    #TODO: Separate cast and director from review summary
                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


