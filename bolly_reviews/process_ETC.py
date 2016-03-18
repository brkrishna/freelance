#-------------------------------------------------------------------------------
# Name:        process_DNAI
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

        page_content = data.find('div', {'class' : 'leftcolumn white'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'class' : 'more'})
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):

                        url = movie['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('div', {'class' : 'leftcolumn white'})
                                if article != None:

                                    name = article.find('h2')
                                    if name != None:
                                        row['name'] = name.text.strip()

                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['year'] = date.today().year

                                    article = article.find('div', {'style' : 'text-align:justify;'})

                                    pColl = article.find_all('p')
                                    if pColl != None:
                                        for p in pColl:

                                            p_text = p.text.strip()

                                            #Writing last paragraph of as review content
                                            if p_text != '':
                                                row['rvw_smy'] = p_text

                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


