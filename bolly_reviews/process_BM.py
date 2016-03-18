#-------------------------------------------------------------------------------
# Name:        process_BM
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     17/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import re
import my_caching
from datetime import date

def process(source_cd, base_url, data):
    try:
        record= []

        page_content = data.find('div', {'class' : 'content'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):
                        url = movie['href']
                        if '/movie-review/' in url:

                            response = my_caching.get_content(source_cd, base_url + url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('article', { 'class' : 'news'})
                                if article != None:

                                    name = article.find('h1')
                                    if name != None:
                                        row['name'] = name.text.strip()
                                        row['source_cd'] = source_cd
                                        row['rvw_link'] = base_url + url
                                        row['year'] = date.today().year

                                    pColl = article.find_all('p')
                                    if pColl != None:
                                        rvw_smy = ''
                                        for p in pColl:
                                            rvw_smy = rvw_smy + p.text.strip()

                                        rvw_smy = rvw_smy[:500]
                                        row['rvw_smy'] = rvw_smy

                                    #TODO: Separate cast and director from review summary
                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


