#-------------------------------------------------------------------------------
# Name:        sources
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     17/04/2014
# Copyright:   (c) Ramakrishna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_source_cd(domain_url):

    try:

        if domain_url == 'http://www.bollywoodhungama.com':
            return 'BWH'
        if domain_url == 'http://bollywood.bhaskar.com':
            return 'BH'
        if domain_url == 'http://www.bollywoodlife.com':
            return 'BL'
        if domain_url == 'http://www.bollywoodmantra.com':
            return 'BM'
        if domain_url == 'http://bollyspice.com':
            return 'BOS'
        if domain_url == 'http://www.bharatstudent.com':
            return 'BS'
        if domain_url == 'http://www.bollywood.com':
            return 'BW'
        if domain_url == 'http://www.bollywood3.com':
            return 'BW3'
        if domain_url == 'http://bollywoodmixer.com':
            return 'BWM'
        if domain_url == 'http://www.dnaindia.com':
            return 'DNAI'
        if domain_url == 'http://www.etc.in':
            return 'ETC'
        if domain_url == 'http://www.filmfare.com':
            return 'FF'
        if domain_url == 'http://www.firstpost.com':
            return 'FP'
        if domain_url == 'http://failsuccess.com':
            return 'FS'
        if domain_url == 'http://www.glamsham.com':
            return 'GS'
        if domain_url == 'http://www.hindustantimes.com':
            return 'HT'
        if domain_url == 'http://ibnlive.in.com':
            return 'IBN'
        if domain_url == 'http://indianexpress.com':
            return 'IE'
        if domain_url == 'http://www.indiaglitz.com':
            return 'IG'
        if domain_url == 'http://www.indicine.com':
            return 'IN'
        if domain_url == 'http://indiatoday.intoday.in':
            return 'IT'
        if domain_url == 'http://www.koimoi.com':
            return 'KM'
        if domain_url == 'http://komalsreviews.wordpress.com':
            return 'KR'
        if domain_url == 'http://www.mid-day.com':
            return 'MD'
        if domain_url == 'http://www.mumbaimirror.com':
            return 'MM'
        if domain_url == 'http://movies.in.msn.com':
            return 'MSN'
        if domain_url == 'http://www.moviezadda.com':
            return 'MZ'
        if domain_url == 'http://movies.ndtv.com':
            return 'NDTV'
        if domain_url == 'http://www.nowrunning.com':
            return 'NR'
        if domain_url == 'http://entertainment.oneindia.in':
            return 'OI'
        if domain_url == 'http://www.planetbollywood.com':
            return 'PB'
        if domain_url == 'http://in.reuters.com':
            return 'RE'
        if domain_url == 'http://www.rediff.com':
            return 'REDIFF'
        if domain_url == 'http://www.rajeevmasand.com':
            return 'RM'
        if domain_url == 'http://www.ratemovieshere.com':
            return 'RMH'
        if domain_url == 'http://www.santabanta.com':
            return 'SB'
        if domain_url == 'http://www.smashits.com':
            return 'SH'
        if domain_url == 'http://www.sify.com':
            return 'SIFY'
        if domain_url == 'http://movies.sulekha.com':
            return 'SULEKHA'
        if domain_url == 'http://timesofindia.indiatimes.com':
            return 'TOI'
        if domain_url == 'https://in.movies.yahoo.com':
            return 'YAHOO'
        if domain_url == 'http://zeenews.india.com':
            return 'ZNI'
        else:
            return None
    except Exception as e:
        print(e.__doc__)
        print(e.args)