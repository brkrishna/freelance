#-------------------------------------------------------------------------------
# Name:        connectDB
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     16/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import dataset

db = None

def get_source_urls():
    try:

        global db

        table = db['urls']
        sources = table.find(order_by='source_cd')
        #sources = table.find(order_by='source_cd', done=0)
        #sources = db.query('select source_cd, source, url from urls order by source_cd')
        return sources

    except Exception as e:
        print(e.__doc__)
        print(e.args)


def get_reviews():
    try:

        global db

        table = db['reviews']
        reviews = table.find(order_by='source_cd')
        return reviews

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def run_log(record):
    try:

        global db
        table = db['run_log']
        table.upsert(record, ['source_cd', 'started'])

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def clean_names():
    try:

        global db

        sql = "update reviews "
        sql = sql + "set name = (select clean_name from clean_names where name like '%' || clean_name || '%') "
        sql = sql + "where name in ( "
        sql = sql + "select name "
        sql = sql + "from clean_names, reviews "
        sql = sql + "where name like '%' || clean_name || '%') "

        db.query(sql)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def prettify_review():
    try:

        global db
        sql = "update reviews "
        sql = sql + "set director = (select director from movie_addl_data where clean_name = name), "
        sql = sql + "actor1 = (select actor1 from movie_addl_data where clean_name = name), "
        sql = sql + "actor2 = (select actor2 from movie_addl_data where clean_name = name), "
        sql = sql + "actor3 = (select actor3 from movie_addl_data where clean_name = name) "

        db.query(sql)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def create_review(record):
    try:

        table= db['reviews']
        for row in record:
            table.upsert(row, ['source_cd', 'year', 'rvw_link'])

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def set_flag(record):
    try:

        table = db['urls']
        for row in record:
            table.update(row, ['source_cd'])

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def main():
    try:
        global db
        db = dataset.connect("sqlite:///bolly_reviews.db3")

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def close():
    global db
    db = None

if __name__ == '__main__':
    main()
