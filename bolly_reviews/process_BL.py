#-------------------------------------------------------------------------------
# Name:        process_BL
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

def process(source_cd, base_url, data):
    try:
        record= []

        #data = data.find('div', { 'class' : 'inner'})
        if data != None:

            movie_coll = data.find_all('a')
            if movie_coll != None:
                for movie in movie_coll:
                    if movie.has_attr('href'):
                        href = movie['href']
                        if href != None:
                            row = {}
                            rvw_url = re.search('movie-review', href)
                            if rvw_url != None:
                                response = my_caching.get_content(source_cd, href)
                                if response != None:
                                    soup = BeautifulSoup(response)

                                    article = soup.find('section', { 'id' : 'content'})
                                    if article != None:

                                        name = article.find('h1')
                                        if name != None:
                                            #Movie Name
                                            row['source_cd'] = source_cd
                                            row['name'] = name.text.strip()

                                            #Year
                                            year = article.find('span', {'class' : 'posted'}).text.strip()
                                            if year != '':
                                                year = re.findall(r'\d{4}', year)
                                                row['year'] = year[0]

                                            #Review link
                                            row['rvw_link'] = href

                                            #Critic
                                            critic = article.find('a', {'rel' : 'author'})
                                            if critic != None:
                                                row['critic'] = critic['title']

                                            #rating
                                            img = article.find('img', { 'class' : 'rating'})
                                            if img != None:
                                                rtng = img['title']
                                                if rtng != '':
                                                    rtng = rtng[:3]
                                                    rating_val = re.findall("\d*\.\d+|\d+", rtng)
                                                    row['rating'] = rating_val[0]

                                            #max_rating
                                            row['max_rtng'] = 5

                                            #comments
                                            article = article.find('article', { 'class' : 'entry-content cunlock_main_content'})
                                            if article != None:
                                                rvw_smy = article.find('p').text.strip()
                                                if rvw_smy != '':
                                                    row['rvw_smy'] = rvw_smy

                                            record.append(row)


        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)

