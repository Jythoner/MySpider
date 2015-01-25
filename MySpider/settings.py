# -*- coding: utf-8 -*-

# Scrapy settings for MySpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'MySpider'

SPIDER_MODULES = ['MySpider.spiders']
NEWSPIDER_MODULE = 'MySpider.spiders'
ITEM_PIPELINES = ['MySpider.pipelines.MySQLStorePipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MySpider (+http://www.yourdomain.com)'
