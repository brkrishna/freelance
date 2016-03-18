#-------------------------------------------------------------------------------
# Name:        process_BWM
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

        page_content = data.find('div', {'class' : 'entry-content'})
        if page_content != None:
            review_anchors = page_content.find_all('div', {'class' : 'thumbnail'})
            for movie in review_anchors:
                if movie != None:
                    row = {}
                    a = movie.find('a')
                    if a.has_attr('href'):

                        # We don't need navigation links
                        if a.has_attr('class'):
                            print(a['class'])
                            if a['class'] == 'page-numbers':
                                exit

                        url = a['href']
                        if url != None:

                            response = my_caching.get_content(source_cd, url)
                            if response != None:

                                soup = BeautifulSoup(response)

                                article = soup.find('div', { 'id' : 'content'})
                                if article != None:

                                    name = article.find('h1')
                                    if name != None:
                                        name = name.text.strip()
                                        name = name.replace('Review', '')
                                        name = name[:name.find('\n')]
                                        row['name'] = name.strip()

                                    row['source_cd'] = source_cd
                                    row['rvw_link'] = url
                                    row['critic'] = 'admin'
                                    row['year'] = date.today().year
                                    #max_rating
                                    row['rating'] = 0
                                    row['max_rtng'] = 4

                                    pColl = article.find_all('p')
                                    if pColl != None:
                                        for p in pColl:

                                            rating_val = 0
                                            #Rating
                                            if p != None:
                                                img = p.find_all('img')
                                                if img != None:
                                                    for i in img:
                                                        i = i['alt']
                                                        if 'star-gold20' in i:
                                                            rating_val = rating_val + 1
                                                        elif 'gold-star-half' in i:
                                                            rating_val = rating_val + 0.5

                                                if rating_val > 0:
                                                    row['rating'] = rating_val

                                            p_text = p.text.strip()

                                            if 'Movie:' in p_text:
                                                row['name'] = p_text[7:].strip()

                                            if 'Release Date:' in p_text:
                                                year = re.findall(r'\d{4}', p_text)
                                                row['year'] = year[0]

                                            #Writing last paragraph of as review content
                                            row['rvw_smy'] = p_text

                                            if 'Star Cast:' in p_text:
                                                p_text = p_text.split(',')

                                                if p_text[0] != None:
                                                    #get rid of start cast note
                                                    actor1 = p_text[0][10:]
                                                    row['actor1'] = actor1.strip()

                                                if p_text[1] != None:
                                                    row['actor2'] = p_text[1].strip()

                                                if len(p_text) >= 3:
                                                    row['actor3'] = p_text[2].strip()

                                            if 'Director:' in p_text:
                                                row['director'] = p_text[10:].strip()

                                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


