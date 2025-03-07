# -*- coding: utf-8 -*-

BOT_NAME = 'skuscraper'

SPIDER_MODULES = ['skuscraper.spiders']
NEWSPIDER_MODULE = 'skuscraper.spiders'

USER_AGENT = 'Frontera-based example bot (+https://github.com/scrapinghub/frontera)'

''' Single Process and Distributed Settings '''
# SPIDER_MIDDLEWARES = {
#     'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 1000,
#     'scrapy.spidermiddleware.depth.DepthMiddleware': None,
#     'scrapy.spidermiddleware.offsite.OffsiteMiddleware': None,
#     'scrapy.spidermiddleware.referer.RefererMiddleware': None,
#     'scrapy.spidermiddleware.urllength.UrlLengthMiddleware': None
# }
#
# DOWNLOADER_MIDDLEWARES = {
#     'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
# }
#
# SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

''' Clustering Settings '''
SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'

SPIDER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 999,
    'frontera.contrib.scrapy.middlewares.seeds.file.FileSeedLoader': 1,
}
DOWNLOADER_MIDDLEWARES = {
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 999,
}


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
DOWNLOAD_DELAY = 0.0

LOG_LEVEL = 'DEBUG'

REACTOR_THREADPOOL_MAXSIZE = 32
DNS_TIMEOUT = 180

'''
For single process set this to 'config.single'
For clustering set this to 'cluster.spider
'''
FRONTERA_SETTINGS = 'cluster.spider'

HTTPERROR_ALLOW_ALL = True
