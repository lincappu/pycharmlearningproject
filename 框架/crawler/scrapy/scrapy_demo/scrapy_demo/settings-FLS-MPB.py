# -*- coding: utf-8 -*-

# Scrapy settings.py for scrapy_demo project
#
# For simplicity, this file contains only settings.py considered important or
# commonly used. You can find more settings.py consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_demo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings.py and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_demo.middlewares.ScrapyDemoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy_demo.middlewares.ScrapyDemoDownloaderMiddleware': 543,
    #  'scrapy_demo.middlewares.ProxyMiddleware': 500,
    #  'scrapy_demo.middlewares.UAMiddleware': 501,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': 6023,
    'scrapy_jsonrpc.webservice.WebService': 500,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy_demo.pipelines.ScrapyDemoPipeline': 300,  # 后面的数字是优先级，0-1000 越低优先级越高
    'scrapy_demo.pipelines.JsonWriterPipeline': 800,
    # 'scrapy_demo.pipelines.MysqlPipeline': 900,
    # 'scrapy_demo.pipelines.MysqlbulkPipeline': 910,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# FEED_EXPORTERS = {
#     'json': 'scrapy_demo.customconfigs.CustomJsonLinesItemExporter',
# }


FEED_EXPORT_ENCODING = 'utf-8'



# FEED_EXPORTERS_BASE = {
#     'json': 'scrapy.exporters.JsonItemExporter',
#     'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
#     'jl': 'scrapy.exporters.JsonLinesItemExporter',
#     'csv': 'scrapy.exporters.CsvItemExporter',
#     'xml': 'scrapy.exporters.XmlItemExporter',
#     'marshal': 'scrapy.exporters.MarshalItemExporter',
#     'pickle': 'scrapy.exporters.PickleItemExporter',
# }
#
# FEED_STORAGES_BASE = {
#     '': 'scrapy.extensions.feedexport.FileFeedStorage',
#     'file': 'scrapy.extensions.feedexport.FileFeedStorage',
#     'stdout': 'scrapy.extensions.feedexport.StdoutFeedStorage',
#     's3': 'scrapy.extensions.feedexport.S3FeedStorage',
#     'ftp': 'scrapy.extensions.feedexport.FTPFeedStorage',
# }




MYSQL_HOST = '35.236.152.207'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'iCourt12345'
MYSQL_PORT = 3306
MYSQL_DB = 'scrapy_demo'
CHARSET = 'utf8'

PROXIES = ['https://60.191.11.237:3128']

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 4.2.1; 2013022 MIUI/JHACNBL30.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "AndroidDownloadManager",
    "Apache-HttpClient/UNAVAILABLE (java 1.4)",
    "Dalvik/1.6.0 (Linux; U; Android 4.3; SM-N7508V Build/JLS36C)",
    "Android50-AndroidPhone-8000-76-0-Statistics-wifi",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.4; MI 3 MIUI/V7.2.1.0.KXCCNDA)",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo A3800-d Build/LenovoA3800-d)",
    "Lite 1.0 ( http://litesuits.com )",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC T528t Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4)",
]

# 日志设置：
LOG_ENABLED = True
LOG_ENCODING = "utf-8"
LOG_LEVEL = 'INFO'
LOG_FILE = "spider.log.sh"
LOG_STDOUT = True
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

# email配置
MAIL_HOST = 'smtp.exmail.qq.com'
MAIL_PORT = 25
MAIL_USER = "monitor@icourt.cc"
MAIL_FROM = "monitor@icourt.cc"
MAIL_PASS = "6bH9KPQoKD"
MAIL_TLS = False
MAIL_SSL = False

JSONRPC_ENABLED = True
JSONRPC_PORT = 6080
JSONRPC_LOGFILE = 'jsonrpc.log.sh'

