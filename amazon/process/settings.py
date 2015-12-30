# -*- coding: utf-8 -*-

# Scrapy settings for process project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'process'

SPIDER_MODULES = ['process.spiders']
NEWSPIDER_MODULE = 'process.spiders'
DOWNLOADER_STATS = False
LOG_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'process (+http://www.yourdomain.com)'
