#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbit25
#
# Created:     17/07/2015
# Copyright:   (c) sbit25 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import json

csvfile = open('reviews', 'r')
jsonfile = open('reviews.json', 'w')

fieldnames = ("product","star_rating","posted","body")

def main():
    try:
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')
    except Exception as e:
        print(e.__doc__)
        print(e.args)

if __name__ == '__main__':
    main()
