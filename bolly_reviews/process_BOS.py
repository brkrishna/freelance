#-------------------------------------------------------------------------------
# Name:        process_BOS
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

        page_content = data.find('div', {'class' : 'moviereviewslist'})
        if page_content != None:
            review_anchors = page_content.find_all('a')
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):
                        url = movie['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('div', { 'class' : 'hreview'})
                                if article != None:

                                    name = article.find('h1')
                                    if name != None:
                                        row['source_cd'] = source_cd
                                        row['name'] = name.text.strip()
                                        row['rvw_link'] = url

                                    #Year
                                    year = article.find('span', {'class' : 'date dtreviewed'}).text.strip()
                                    if year != '':
                                        year = re.findall(r'\d{4}', year)
                                        row['year'] = year[0]

                                    #Critic
                                    critic = article.find('span', {'class' : 'author reviewer'})
                                    if critic != None:
                                        row['critic'] = critic.text.strip()

                                    #rating
                                    img = article.find('div', { 'class' : 'rating_bar'})
                                    if img != None:
                                        rtng = img['title']
                                        if rtng != '':
                                            rtng = rtng[:3]
                                            rating_val = re.findall("\d*\.\d+|\d+", rtng)
                                            row['rating'] = rating_val[0]

                                    #max_rating
                                    row['max_rtng'] = 5

                                    # Review
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


