#-------------------------------------------------------------------------------
# Name:        process_BW3
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

        page_content = data.find('div', {'id' : 'coloredblock4'})
        if page_content != None:
            review_anchors = page_content.find_all('div', { 'id': 'colorcontentwrap4'})
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    a = movie.find('a')
                    if a.has_attr('href'):
                        url = a['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('div', { 'class' : 'post'})
                                if article != None:

                                    name = article.find('h1')
                                    if name != None:
                                        name = name.text.strip()
                                        name = name.replace('Movie Review:', '')
                                        row['source_cd'] = source_cd
                                        row['name'] = name.strip()
                                        row['rvw_link'] = url
                                        row['rvw_smy'] = ''

                                    #Year
                                    row['year'] = date.today().year

                                    #Critic
                                    pColl = article.find_all('p')
                                    if pColl != None:
                                        for p in pColl:

                                            p_text = p.text.strip()

                                            #Assuming the first paragraph has review content
                                            if row['rvw_smy'] == '':
                                                row['rvw_smy'] = p_text

                                            if 'Reviewed by' in p_text:
                                                #Critic
                                                critic = p_text
                                                row['critic'] = critic[12:]

                                            if 'Bollywood3 Rating' in p_text:
                                                #Rating
                                                rating_val = re.findall("\d*\.\d+|\d+", p_text)
                                                row['rating'] = rating_val[1]

                                    #max_rating
                                    row['max_rtng'] = 5

                                    #TODO: Separate cast and director from review summary
                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


