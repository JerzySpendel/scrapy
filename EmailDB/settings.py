# Scrapy settings for EmailDB project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Google'
ITEM_PIPELINES = ['EmailDB.pipelines.dobreprogramyPipeline']
SPIDER_MODULES = ['EmailDB.spiders']
NEWSPIDER_MODULE = 'EmailDB.spiders'
RETRY_TIMES = 4
CONCURRENT_REQUESTS = 32
CONCURRENT_ITEMS = 1000
DOWNLOAD_TIMEOUT = 10
DOWNLOAD_DELAY = 0.001
meta={'dont_redirect': True}
REDIRECT_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 123,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'EmailDB (+http://www.yourdomain.com)'
