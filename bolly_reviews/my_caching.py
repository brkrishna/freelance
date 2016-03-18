#-------------------------------------------------------------------------------
# Name:        my_caching
# Purpose:
#
# Author:      sbit25
#
# Created:     19/04/2014
# Copyright:   (c) sbit25 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, requests
from hashlib import sha1

CACHE_DIR = os.path.join(os.path.dirname(__file__), 'cache')

def url_to_filename(source_cd, url):
    """ Make a URL into a file name, using SHA1 hashes. """

    # use a sha1 hash to convert the url into a unique filename
    url = url.encode('utf-8')
    hash_file = sha1(url).hexdigest() + '.html'
    return os.path.join(CACHE_DIR + '\\' + source_cd + '\\', hash_file)


def store_local(source_cd, url, content):
    """ Save a local copy of the file. """

    # If the cache directory does not exist, make one.
    if not os.path.isdir(CACHE_DIR + '\\' + source_cd):
        os.makedirs(CACHE_DIR + '\\' + source_cd)

    # Save to disk.
    local_path = url_to_filename(source_cd, url)
    with open(local_path, 'wb') as f:
        f.write(content)


def load_local(source_cd, url):
    """ Read a local copy of a URL. """
    local_path = url_to_filename(source_cd, url)
    if not os.path.exists(local_path):
        return None

    with open(local_path, 'rb') as f:
        return f.read()


def get_content(source_cd, url):
    """ Wrap requests.get() """
    content = load_local(source_cd, url)
    if content is None:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            store_local(source_cd, url, content)
        else:
            return None
    return content