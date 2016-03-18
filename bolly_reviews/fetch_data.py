#-------------------------------------------------------------------------------
# Name:        fetch_data
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     16/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests, time, sys
from thready import threaded
from datetime import datetime
import connect_db, process_data, my_caching, sources
from bs4 import BeautifulSoup
SCRAPING_REQUEST_STAGGER = 1 # in seconds

def process_urls(process_source):
    try:

        global sources

        urls = []
        connect_db.main()

        url_sources = connect_db.get_source_urls()

        for source in url_sources:
            if source != None:
                # read url to parse
                source_url = source['url']
                source_cd = source['source_cd']
                if process_source != None:
                    if process_source == source_cd:
                        urls.append(source_url)
                else:
                    urls.append(source_url)

        #threaded(urls, process_url, num_threads = 5, max_queue = 100)

        for url in urls:
            process_url(url)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        connect_db.close()

def process_url(url):
    try:

        record = []
        base_url = ''
        base_url = find_domain(url)
        source_cd = sources.get_source_cd(base_url)

        if source_cd == None:
            print('Not a domain in parsing database - ' + base_url)

        else:

            print('processing - ' + source_cd)
            started = datetime.now()
            #Initiated querying for data
            log(source_cd, started, started)

            #response = requests.get(source_url)
            response = my_caching.get_content(source_cd, url)
            soup = BeautifulSoup(response)

            record = process_data.process(base_url, source_cd, soup)

            if record != None:
                connect_db.create_review(record)

                time.sleep(SCRAPING_REQUEST_STAGGER)
                '''
                record = []
                row = {}

                row['source_cd'] = source_cd
                row['done'] = 1

                record.append(row)
                connect_db.set_flag(record)
                '''
                connect_db.clean_names()
                connect_db.prettify_review()

            #Process done for this source
            log(source_cd, started, datetime.now())



    except Exception as e:
        print(e.__doc__)
        print(e.args)

def log(source_cd, started, completed):

    try:

        record = {}
        record['source_cd'] = source_cd
        record['started'] = started
        record['completed'] = completed

        connect_db.run_log(record)

    except Exception as e:
        print(e.__doc__)
        print(e.args)


def find_domain(url):

    secured = 0

    pos = url[7:].find('/')
    if pos == 0:
        pos = url[8:].find('/')
        secured = 1

    if pos == -1:
        pos = url[7:].find('?')
        if pos == -1:
            return url[7:]
        url = url[7:(7+pos)]
        return url
    else:
        if secured == 0:
            return url[:pos+7]
        else:
            return url[:pos+8]

def main(argv):

    try:
        process_source = None

        if len(argv) > 1:
            process_source = argv[1]

        process_urls(process_source)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

if __name__ == '__main__':
    main(sys.argv)
