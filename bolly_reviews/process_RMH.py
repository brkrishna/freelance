#-------------------------------------------------------------------------------
# Name:        process_RMH
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

        page_content = data.find('div', {'class' : 'fullbottomline'})
        if page_content != None:
            review_items = page_content.find_all('div', {'class':'reviewitem'})
            if review_items != None:
                for review_item in review_items:
                    link = review_item.find('a')
                    if link != None:
                        row = {}
                        row['source_cd'] = source_cd
                        row['rvw_link'] = base_url + link['href']
                        row['rvw_smy'] = ''
                        row['rating'] = ''
                        row['year'] = date.today().year

                    meta = review_item.find('div', {'class':'review-moviename'})
                    if meta != None:
                        critic = meta.find('span')
                        if critic != None:
                            critic = critic.text.strip().replace('Reviews', '')
                            row['critic'] = critic

                        title = meta.text.strip()
                        if title != None:
                            title = title.replace(critic, '')
                            title = title.replace('Reviews', '')
                            row['name'] = title
                        else:
                            continue

                    ratings = review_item.find('div', {'class':'movieinfo'})
                    if ratings != None:
                        tds = ratings.find_all('td')
                        if tds != None:
                            for td in tds:
                                rating = td.find('b')
                                if rating != None:
                                    rating_val = re.findall("\d*\.\d+|\d+", rating.text.strip())
                                    if len(rating_val) > 0 and row['rating'] == '':
                                        row['rating'] = rating_val[0]
                                        row['max_rtng'] = 10

                    review = review_item.find('p', {'style':'font-weight:normal'})
                    if review != None:
                        row['rvw_smy'] = review.text.strip()

                    record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)