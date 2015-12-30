# -*- coding: utf-8 -*-

# Scrapy settings for etsy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'etsy'

SPIDER_MODULES = ['etsy.spiders']
NEWSPIDER_MODULE = 'etsy.spiders'
LOG_ENABLED = False

DEPTH_PRIORITY = 1 
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
AUTOTHROTTLE_MAX_DELAY = 60.0
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'etsy (+http://www.yourdomain.com)'
