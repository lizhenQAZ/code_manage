# -*- coding: utf-8 -*-

# Scrapy settings for myspider_douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myspider_douban'

SPIDER_MODULES = ['myspider_douban.spiders']
NEWSPIDER_MODULE = 'myspider_douban.spiders'

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 2.0.40607) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; DFO-MPO Internet Explorer 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; iebar; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.40607) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; NOKTURNAL KICKS ASS) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.41115) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ENGINE; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT)) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) ",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1); ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ESB{F40811EE-DF17-4BC9-8785-B362ABF34098}; .NET CLR 1.1.4322) ",
]
PROXY_LIST = [
    # {"ip_port": "121.199.1.230:16816", "user_passwd": "morganna_mode_g:ggc22qxp"},
    {"ip_port": "106.39.179.9:80"},
    {"ip_port": "175.16.14.214:80"},
    {"ip_port": "112.13.93.43:8088"},
    {"ip_port": "120.204.74.100:80"},
    {"ip_port": "122.72.18.61:80"},
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'myspider_douban (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myspider_douban.middlewares.MyspiderDoubanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'myspider_douban.middlewares.MyCustomDownloaderMiddleware': 543,
   'myspider_douban.middlewares.RandomUserAgentMiddleware': 543,
   'myspider_douban.middlewares.RandomProxy': 544,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myspider_douban.pipelines.MyspiderDoubanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
