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

        page_content = data.find('div', {'class' : 'col-xs-12 col-md-8 nopadding-left listingwrp'})
        if page_content != None:
            review_anchors = page_content.find_all('a', {'class' : 'imgwrp'})
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    if movie.has_attr('href'):

                        url = movie['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, base_url + url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('section', { 'class' : 'container'})
                                if article != None:

                                    name = article.find('h1', {'class' : 'pageheading'})
                                    if name != None:
                                        name = name.text.strip()
                                        name = name.replace('Film Review:', '')
                                        name = name.replace('Film review:', '')
                                        row['name'] = name.strip()

                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = base_url + url
                                    row['year'] = date.today().year
                                    #max_rating
                                    row['rating'] = 0
                                    row['max_rtng'] = 5

                                    year = article.find('div', {'class' : 'pubdate'}).text.strip()
                                    if year != '':
                                        year = re.findall(r'\d{4}', year)
                                        row['year'] = year[0]

                                    #Critic
                                    critic = article.find('p', {'class' : 'authorname'})
                                    if critic != None:
                                        row['critic'] = critic.text.strip()

                                    article = article.find('div', {'class' : 'content-story'})

                                    pColl = article.find_all('p')
                                    if pColl != None:
                                        for p in pColl:

                                            rating_val = 0

                                            p_text = p.text.strip()

                                            if 'Rating' in p_text:

                                                rating_stars = p.text.count('*')
                                                if '1/2' in p_text:
                                                    rating_val = rating_stars + 0.5
                                                else:
                                                    rating_val = rating_stars

                                                if rating_val > 0:
                                                    row['rating'] = rating_val

                                            #Writing last paragraph of as review content
                                            row['rvw_smy'] = p_text

                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


