# -*- coding: utf-8 -*-

BOT_NAME = 'skuscraper'

SPIDER_MODULES = ['skuscraper.spiders']
NEWSPIDER_MODULE = 'skuscraper.spiders'

USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
}

DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
}

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

ITEM_PIPELINES = {}


HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 240
RETRY_ENABLED = False
DOWNLOAD_MAXSIZE = 1*1024*1024

# auto throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_MAX_DELAY = 3.0
AUTOTHROTTLE_START_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = False

# concurrency
CONCURRENT_REQUESTS = 64
CONCURRENT_REQUESTS_PER_DOMAIN = 10
DOWNLOAD_DELAY = 2

# LOG_LEVEL = 'INFO'

REACTOR_THREADPOOL_MAXSIZE = 32
DNS_TIMEOUT = 180
FRONTERA_SETTINGS = 'skuscraper.frontera.settings'
HTTPERROR_ALLOW_ALL = True
