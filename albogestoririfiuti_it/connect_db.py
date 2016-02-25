#-------------------------------------------------------------------------------
# Name:        connect_db
# Purpose:
#
# Author:      sbit25
#
# Created:     14/05/2014
# Copyright:   (c) sbit25 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import dataset

db = None

def at_lines(row):
    try:
        table= db['at_lines']
        table.upsert(row, ['section', 'name'])

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def main():
    try:
        global db
        db = dataset.connect("mysql+pymysql://od:od@localhost:3306/od")

    except Exception as e:
        print(e.__doc__)
        print(e.args)

def close():
    global db
    db = None

if __name__ == '__main__':
    main()
