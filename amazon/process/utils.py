#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbit25
#
# Created:     29/07/2015
# Copyright:   (c) sbit25 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def find_domain(url):

    secured = 0

    pos = url[7:].find('/')
    if pos == 0:
        pos = url[8:].find('/')
        secured = 1

    if pos == -1:
        pos = url[7:].find('?')
        if pos == -1:
            return url
    else:
        if secured == 0:
            return url[:pos+7]
        else:
            return url[:pos+8]
