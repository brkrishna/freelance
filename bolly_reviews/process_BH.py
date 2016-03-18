#-------------------------------------------------------------------------------
# Name:        process_BH
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
from datetime import date

def process(source_cd, base_url, data):
    try:
        record= []

        movie_coll = data.find_all('div', {'class' : 'itemListing'})
        if movie_coll != None:
            for movie in movie_coll:

                row = {}
                if movie != None:

                    #Movie Name
                    name_url = movie.find('h2')
                    if name_url != None:
                        name = name_url.text.strip()
                        if name != '':
                            name = name.replace('Movie Review:', '')
                            row['source_cd'] = source_cd
                            row['name'] = name.strip()
                            row['year'] = date.today().year

                        anchor = name_url.find('a')
                        if anchor != None:
                            rvw_link = anchor['href']
                            if rvw_link != '':
                                row['rvw_link'] = base_url + rvw_link

                    #Critic
                    row['critic'] = 'dainikbhaskar.com'

                    #comments
                    rvw_smy = movie.find('div', { 'class' : 'para_txt'}).text.strip()
                    if rvw_smy != '':
                        row['rvw_smy'] = rvw_smy

                    #max_rating
                    row['max_rtng'] = 5

                    #TODO: Rating value to be captured, also hindi font to be preserved in content
                    #rating
                    li = movie.find('div', { 'class' : 'critics_rating'})
                    if li != None:
                        img = li.find('img')
                        if img != None:
                            rtng = img['src']
                            if rtng != '':
                                rating_val = rting[rtng.rfind('/'):rtng.rfind('.jpg')]
                                rating_val = re.findall("\d.+\d+", rating_val)
                                row['rating'] = rating_val[0]

                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


