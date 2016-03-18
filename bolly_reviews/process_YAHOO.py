#-------------------------------------------------------------------------------
# Name:        process_YAHOO
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
        anchors = []
        unique_anchors = []

        page_content = data.find('div', {'class' : 'yom-mod yom-blog-index'})
        if page_content != None:
            links = page_content.find_all('h2', {'class':'headline'})
            for link in links:
                a = link.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + url)
                    if response != None:
                        soup = BeautifulSoup(response)
                        page = soup.find('div', {'class':'yog-col yog-16u yom-primary'})
                        if page != None:
                            title = page.find('h1', {'class':'headline'})
                            if title != None:
                                row = {}
                                title = title.text.strip()
                                title = title.replace('Yahoo Movies Review:', '')
                                row['name'] = title
                                row['source_cd'] = source_cd
                                row['rvw_link'] = base_url + url
                                row['rvw_smy'] = ''
                                row['year'] = date.today().year
                            else:
                                continue
                        else:
                            continue

                        byline = page.find('cite', {'class':'byline vcard'})
                        if byline != None:
                            author = byline.find('a', {'rel':'author'})
                            if author != None:
                                row['critic'] = author.text.strip()

                            year = re.findall(r'\d{4}', byline.text.strip())
                            if len(year) > 0:
                                row['year'] = year[0]

                        content = page.find('div', {'itemprop':'articleBody'})
                        if content != None:

                            rating = content.text.strip()

                            row['rvw_smy'] = content.text.strip()


                            if rating != None:
                                if 'Rating' in rating:

                                    rating_stars = rating.count('*')
                                    if '1/2' in rating:
                                        rating_val = rating_stars + 0.5
                                    else:
                                        rating_val = rating_stars

                                    if rating_val > 0:
                                        row['rating'] = rating_val
                                        row['max_rtng'] = 5

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)