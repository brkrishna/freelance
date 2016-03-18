#-------------------------------------------------------------------------------
# Name:        process_BWH
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

def process(source_cd, base_url, data):
    try:
        record= []

        movie_coll = data.find_all('div', {'class' : 'movfeaturesblock mht194 mfl mmb22 mml9 minline'})
        if movie_coll != None:
            for movie in movie_coll:

                row = {}
                if movie != None:
                    #Movie Name
                    name = movie.find('h2').text.strip()
                    if name != '':
                        row['source_cd'] = source_cd
                        row['name'] = name

                    #Review link

                    anchor = movie.find('a', {'class' : 'm0077 mbold'})
                    if anchor != None:
                        rvw_link = anchor['href']
                        if rvw_link != '':
                            row['rvw_link'] = base_url + rvw_link

                    #Critic
                    critic = movie.find('li', {'class' : 'movlstlirel mfl  mwidth391 mfnt11 maa00 malignlft mht30 mbold '}).text.strip()
                    if critic != '':
                        critic = critic[:critic.find(',')]
                        critic = critic.replace('By', '')
                        row['critic'] = critic

                    #Year
                    year = movie.find('span', {'class' : 'm9090'}).text.strip()
                    if year != '':
                        #year = re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', year)
                        year = re.findall(r'\d{4}', year)
                        row['year'] = year[0]

                    #comments
                    rvw_smy = movie.find('h3').text.strip()
                    if rvw_smy != '':
                        row['rvw_smy'] = rvw_smy

                    #max_rating
                    row['max_rtng'] = 5

                    #rating
                    li = movie.find('li', { 'class' : 'mlt17 mfl mmr95 minline moverflow'})
                    if li != None:
                        img = li.find('img')
                        if img != None:
                            rtng = img['alt']
                            if rtng != '':
                                row['rating'] = rtng

                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)
