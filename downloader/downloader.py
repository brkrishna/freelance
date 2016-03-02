#-------------------------------------------------------------------------------
# Name:        downloader
# Purpose:     To downlaod a list of files   
#
# Author:      Ramakrishna
#
# Created:     19/02/2016
# Copyright:   (c) Ramakrishna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pycurl, os

DOWNLOAD_PATH = "/home/ramakrishna/projects/freelance/downloader/"

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
        urls = set(open('urls').readlines())

        #This could be running in a batch, remove what has been downloaded
        if os.path.isfile('urls_done'):
            finished_urls = set(open('urls_done').readlines())
            urls -= finished_urls

        c = pycurl.Curl()

        for url in urls:
            try:
                #remove new line
                url = url.replace("\n", "")
                
                #Construct a unique filename with appropriate replacements . -> _, / -> -, = -> $
                file_name = url[url.rfind("://")+3:]
                file_name = file_name.replace(".", "_").replace("/", "-").replace("=", "$")
                
                f = open(DOWNLOAD_PATH + file_name, 'wb')
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.VERBOSE, True)
                c.setopt(pycurl.WRITEDATA, f)
                c.setopt(pycurl.FOLLOWLOCATION, 1)
                c.setopt(pycurl.NOPROGRESS, 0)
                c.setopt(pycurl.TIMEOUT, 300)
                c.setopt(pycurl.MAXREDIRS, 5)
                c.setopt(pycurl.NOSIGNAL, 1)
                try:
                    c.perform()
                except (pycurl.error, KeyboardInterrupt, SystemExit, Exception) as e: 
                    logger.debug("Interrupted or Failed to download - " + url + ", with the following error - " + e.args[0])
                    if os.path.exists(DOWNLOAD_PATH + file_name):
                        os.remove(DOWNLOAD_PATH + file_name)                    
                    f.close()

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
