#-------------------------------------------------------------------------------
# Name:        process_PB
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

        review_anchors = data.find_all('tr', {'bgcolor' : '#eeefff'})
        if review_anchors != None:
            for review_anchor in review_anchors:
                a = review_anchor.find('a')
                if a != None:
                    anchors.append(a['href'])

            unique_anchors = set(anchors)

            for url in unique_anchors:
                row = {}
                if url != None:
                    response = my_caching.get_content(source_cd, base_url + '/' + url)
                    if response != None:

                        soup = BeautifulSoup(response)

                        title = soup.find('td', {'class':'tableHeadTopRowCenter'})
                        if title != None:
                            title = title.text.strip()
                            row['name'] = title
                            row['source_cd'] = source_cd
                            row['rvw_link'] = base_url + '/' + url
                            row['rvw_smy'] = ''

                        author = soup.find('td', {'bgcolor':'#eeeeee'})
                        if author != None:
                            meta = author.find_all('a')
                            if meta != None:
                                for m in meta:
                                    if '#' not in m['href']:
                                        row['critic'] = m.text.strip()
                                    else:
                                        rating_val = re.findall("\d*\.\d+|\d+", m.text.strip())
                                        if len(rating_val) > 0:
                                            row['rating'] = rating_val[0]
                                            row['max_rtng'] = 10

                        row['year'] = date.today().year

                        pColl = soup.find_all('p')
                        rvw_smy = ''
                        for p in pColl:
                            rvw_smy = rvw_smy + p.text.strip()

                        rvw_smy = rvw_smy[:500]
                        if rvw_smy != '':
                            row['rvw_smy'] = rvw_smy

                        record.append(row)

        return record

    except Exception as e:
        print(e.__doc__)
        print(e.args)


