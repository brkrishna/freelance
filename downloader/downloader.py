#-------------------------------------------------------------------------------
# Name:        downloader
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     19/02/2016
# Copyright:   (c) Ramakrishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pycurl, os

DOWNLOAD_PATH = "C:\\upwork\\downloader\\"

'''
Logging temporarily for debug purposes, can be removed once the script is stable or integrated with other code
'''
import logging

# create logger with 'spam_application'
logger = logging.getLogger('downloader')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('downloader.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

def main():
    try:
        #Reading urls to be downloaded
        urls = open('urls').readlines()

        #This could be running in a batch, remove what has been downloaded
        if os.path.isfile('urls_done'):
            finished_urls = open('urls_done').readlines()
            urls -= finished_urls

        c = pycurl.Curl()

        for url in urls:
            try:
                #Construct a unique filename with appropriate replacements . -> _, / -> $, : -> -
                file_name = url.replace(".", "_").replace("/", "$").replace(":", "-")
                f = open(DOWNLOAD_PATH + "\\" + file_name, 'wb')
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.VERBOSE, True)
                c.setopt(c.WRITEDATA, f)
                try:
                    c.perform()
                except pycurl.error as e:
                    logger.debug("Failed to download - " + url + ", with the following error - " + e.args[0])
                    pass

                total_time = c.getinfo(pycurl.TOTAL_TIME)
                download_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
                logger.debug(url + " - Downloaded as - " + file_name + " of size - " + str(download_size) + " in " + str(total_time) + " second(s)")

                open('urls_done', 'a').write(url + '\n')

            except Exception as e:
                logger.debug("Failed to download - " + url + ", with the following error - " + e.args[0])

    except pycurl.error:
        logger.debug("Error - " + e.args[0])

    finally:
        if c:
            c.close()
            c = None

if __name__ == '__main__':
    main()
