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

        page_content = data.find_all('div', {'class' : 'views-field views-field-nid'})
        if page_content != None:

            for movie in page_content:
                if movie != None:
                    review_anchor = movie.find('a')
                    row = {}
                    if review_anchor.has_attr('href'):
                        url = review_anchor['href']
                        if url != None:

                            row['source_cd'] = source_cd
                            start = url.find('/movies/') + 8
                            end = url.find('/', url.find('/movies/') + 8)
                            row['name'] = url[start : end]
                            row['rvw_link'] = base_url + url
                            #Year
                            row['year'] = date.today().year

                            # Review
                            r = movie.find('div', { 'class' : 'hollywood-news-body'})
                            if r != None:
                                r = r.text.strip()
                                row['rvw_smy'] = r


                            #rating
                            img = movie.find('div', { 'class' : 'fivestar-widget-static fivestar-widget-static-vote fivestar-widget-static-5 clear-block'})
                            if img != None:
                                rtng = img.find('span', {'class' : 'on'})
                                if rtng != '':
                                    row['rating'] = rtng.text.strip()

                            #max_rating
                            row['max_rtng'] = 5


                            #TODO: Separate cast and director from review summary
                            record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


