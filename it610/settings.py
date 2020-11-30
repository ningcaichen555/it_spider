# Scrapy settings for it610 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import random

BOT_NAME = 'it610'

SPIDER_MODULES = ['it610.spiders']
NEWSPIDER_MODULE = 'it610.spiders'
DOWNLOAD_DELAY = 3
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'close',
    'referer': 'https://www.it610.com/'
}
UA_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]
USER_AGENT = random.choice(UA_LIST)

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# settings.py文件下添加mysql的配置信息
MY_SETTINGS = {
    "host": "39.97.186.184",
    "user": "webset_online",
    "passwd": "sswz2020",
    "db": "webset_online",
    "port": 3306,
    "charset": "utf8mb4",
    'use_unicode': True,
}
# ############ 连接redis 信息 #################
REDIS_URL = 'redis://:@127.0.0.1:6379'  # 主机名
REDIS_PORT = 6379  # 端口
# REDIS_URL = 'redis://user:pass@hostname:9001'       # 连接URL（优先于以上配置）
REDIS_PARAMS = {}  # Redis连接参数             默认：REDIS_PARAMS = {'socket_timeout': 30,'socket_connect_timeout': 30,'retry_on_timeout': True,'encoding': REDIS_ENCODING,}）
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient' # 指定连接Redis的Python模块  默认：redis.StrictRedis
REDIS_ENCODING = "utf-8"
# 自定义去重规则
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 有引擎来执行：自定义调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'  # 默认使用优先级队列（默认广度优先），其他：PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
SCHEDULER_QUEUE_KEY = '%(spider)s:requests'  # 调度器中请求存放在redis中的key
SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"  # 对保存到redis中的数据进行序列化，默认使用pickle
SCHEDULER_PERSIST = True  # 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空
SCHEDULER_FLUSH_ON_START = False  # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'  # 去重规则，在redis中保存时对应的key  chouti:dupefilter
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'  # 去重规则对应处理的类
DUPEFILTER_DEBUG = False
REDIS_START_URLS_BATCH_SIZE = 1
REDIS_START_URLS_AS_SET = False  # 把起始url放到redis的列表

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
#    'it610.middlewares.It610SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'it610.middlewares.MyProxiesSpiderMiddleware': 125,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

IMAGES_STORE = os.path.join(os.path.dirname(__file__), 'images')

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'it610.pipelines.SaveImagePipeline': 1,
    'it610.pipelines.UploadImagePipeline': 2,
    'it610.pipelines.ItSpiderPipeline': 3,
    'scrapy_redis.pipelines.RedisPipeline': 400
}
# LOG_LEVEL = 'INFO'
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
IPPOOL = [
    "113.194.23.211:9999",
    "175.42.129.252:9999",
    "163.204.94.195:9999",
    "171.35.162.155:9999",
    "123.55.101.154:9999",
    "115.221.242.120:9999",
    "60.168.81.179:1133",
    "114.239.172.212:9999",
    "27.191.25.112:42969",
    "49.86.180.94:9999",
    "183.166.20.170:9999",
    "175.43.35.37:9999",
    "171.35.161.92:9999",
    "175.44.108.58:9999",
    "1.198.72.68:9999",
    "123.149.136.144:9999",
    "144.255.49.9:9999",
    "175.42.122.229:9999",
    "49.89.86.160:9999",
    "121.233.207.15:48258",
    "121.226.214.76:9999",
    "1.197.203.187:9999",
    "183.166.139.156:9999",
    "123.169.118.214:9999",
    "36.248.132.125:9999",
    "175.44.109.122:9999",
    "113.194.22.81:9999",
    "223.242.225.112:9999",
    "123.163.115.250:9999",
    "114.239.3.149:9999",
    "218.89.152.253:29888",
    "223.242.225.237:9999",
    "120.83.106.69:9999",
    "175.42.129.196:9999",
    "187.110.224.122:3130",
    "175.42.128.27:9999",
    "175.42.158.124:9999",
    "1.199.31.111:9999",
    "58.22.177.139:9999",
    "123.55.98.81:9999",
    "114.239.1.85:9999",
    "1.199.31.112:9999",
    "114.104.134.248:8888",
    "49.86.181.108:9999",
    "49.86.183.202:9999",
    "220.176.168.225:42679",
    "175.43.151.3:9999",
    "171.35.173.224:9999",
    "182.107.12.61:9000",
    "119.119.117.145:9000",
    "182.34.36.50:9999",
    "171.35.160.18:9999",
    "123.55.114.219:9999",
    "115.221.246.200:9999",
    "115.53.52.185:9999",
    "175.44.108.168:9999",
    "123.180.210.80:23772",
    "182.46.98.54:9999",
    "114.239.210.92:9999",
    "171.35.175.6:9999",
    "112.111.77.102:9999",
    "49.89.84.134:9999",
    "187.188.194.212:3128",
    "1.197.204.79:9999",
    "123.55.98.106:9999",
    "123.55.102.106:9999",
    "114.239.110.154:9999",
    "58.52.118.168:36196",
    "117.91.250.56:9999",
    "113.121.42.72:9999",
    "171.35.213.163:9999",
    "115.218.7.11:9000",
    "110.243.28.195:9999",
    "123.55.98.225:9999",
    "36.250.156.184:9999",
    "175.42.122.161:9999",
    "117.67.140.195:40429",
    "117.91.255.71:9999",
    "121.233.226.175:9999",
    "114.102.0.153:9999",
    "118.212.104.49:9999",
    "123.163.115.121:9999",
    "119.191.105.40:9000",
    "1.198.72.169:9999",
    "110.243.22.76:9999",
    "123.149.141.44:9999",
    "111.126.82.5:50637",
    "1.198.72.217:9999",
    "175.42.122.87:9999",
    "115.218.7.252:9000",
    "113.121.94.172:9999",
    "175.43.131.128:9999",
    "175.43.34.19:9999",
    "110.243.6.32:9999",
    "114.99.103.190:38193",
    "182.46.122.162:9999",
    "182.87.44.72:9000",
    "110.87.249.195:8888",
    "171.35.172.132:9999",
    "175.42.129.19:9999",
    "114.239.145.243:9999",
    "175.43.178.4:9999",
    "59.63.121.110:31592",
    "106.42.217.61:9999",
    "175.42.122.252:9999",
    "163.125.220.251:8118",
    "223.243.172.77:9999",
    "117.69.169.25:9999",
    "117.64.224.98:1133",
    "171.11.179.184:9999",
    "117.95.232.205:9999",
    "175.42.158.19:9999",
    "114.100.171.179:9999",
    "175.43.58.35:9999",
    "1.196.177.151:9999",
    "175.42.123.7:9999",
    "171.35.171.252:9999",
    "182.46.101.43:9999",
    "123.101.207.111:9999",
    "113.75.136.82:31306",
    "123.160.68.252:9999",
    "163.204.95.44:9999",
    "171.35.160.93:9999",
    "1.197.204.188:9999",
    "112.111.217.29:9999",
    "175.42.129.179:9999",
    "183.166.97.137:9999",
    "123.163.116.128:9999",
    "163.204.94.22:9999",
    "123.169.125.224:9999",
    "112.111.77.51:9999",
    "113.194.30.19:9999",
    "113.195.156.176:9999",
    "119.41.202.146:40885",
    "114.104.139.241:9999",
    "113.194.148.78:9999",
    "118.24.127.144:1080",
    "123.163.116.121:9999",
    "113.194.22.49:9999",
    "171.11.179.89:9999",
    "175.155.140.214:1133",
    "175.42.158.2:9999",
    "175.42.68.33:9999",
    "60.169.95.109:1133",
    "175.43.34.2:9999",
    "175.44.109.236:9999",
    "117.91.253.8:9999",
    "117.63.132.161:38219",
    "175.42.158.249:9999",
    "123.55.114.37:9999",
    "123.169.102.43:9999",
    "115.211.189.193:9999",
    "123.180.209.255:26309",
    "42.177.137.67:49211",
    "123.169.38.177:9999",
    "171.80.186.10:45910",
    "183.166.132.63:9999",
    "111.126.81.27:30858",
    "1.196.177.192:9999",
    "113.195.169.244:9999",
    "101.18.120.36:9999",
    "171.35.220.114:9999",
    "36.59.244.168:20859",
    "223.242.224.156:9999",
    "123.169.120.124:9999",
    "113.124.86.215:9999",
    "39.84.122.216:9999",
    "49.89.85.6:9999",
    "117.92.119.38:24829",
    "183.166.162.192:9999",
    "60.167.23.76:1133",
    "117.69.12.166:9999",
    "113.121.22.186:9999",
    "49.89.87.202:9999",
    "123.169.34.161:9999",
    "115.221.245.130:9999",
    "117.69.51.118:48155",
    "175.155.139.215:1133",
    "171.35.172.138:9999",
    "113.195.224.85:9999",
    "183.166.103.158:9999",
    "171.35.211.185:9999",
    "117.69.179.3:9999",
    "121.233.207.144:9999",
    "27.188.195.115:45971",
    "112.240.177.237:9000",
    "106.110.200.118:9999",
    "183.166.139.62:9999",
    "106.42.195.211:43184",
    "120.83.107.136:9999",
    "223.241.59.205:9999",
    "114.99.7.36:1133",
    "110.243.24.164:9999",
    "117.67.140.120:34105",
    "49.86.181.138:9999",
    "113.195.153.69:9999",
    "49.87.210.58:9999",
    "49.86.180.219:9999",
    "121.207.94.49:41575",
    "113.121.47.41:9999",
    "171.35.162.165:9999",
    "120.83.109.122:9999",
    "112.66.248.206:39370",
    "1.199.31.176:9999",
    "183.166.132.99:9999",
    "106.42.45.215:9999",
    "182.86.191.129:21574",
    "27.220.51.189:9000",
    "123.169.103.84:9999",
    "123.169.113.39:9999",
    "221.199.65.179:32043",
    "183.166.132.188:9999",
    "115.218.5.218:9000",
    "114.234.82.145:9000",
    "182.34.35.77:9999",
    "175.42.129.161:9999",
    "115.235.41.170:9000",
    "171.13.4.31:9999",
    "125.123.154.170:28619",
    "36.76.155.60:8080",
    "113.121.65.60:9999",
    "101.75.162.213:9999",
    "117.87.177.39:9000",
    "123.55.98.203:9999",
    "171.15.65.223:9999",
    "111.126.80.180:39049",
    "113.195.169.163:9999",
    "115.221.247.150:9999",
    "117.69.169.55:9999",
    "114.106.217.246:45015",
    "60.167.20.140:1133",
    "1.199.31.218:9999",
    "123.169.114.143:9999",
    "183.166.139.234:9999",
    "113.121.76.249:9999",
    "111.126.87.242:33089",
    "113.120.143.16:8888",
    "115.218.3.190:9000",
    "36.249.49.29:9999",
    "123.163.118.37:9999",
    "36.248.132.62:9999",
    "103.47.93.229:51618",
    "117.68.195.92:1133",
    "113.13.160.51:8888",
    "175.146.97.240:9999",
    "123.101.231.46:9999",
    "113.195.170.32:9999",
    "59.63.102.89:53574",
    "175.42.158.112:9999",
    "115.218.4.122:9000",
    "123.169.96.163:9999",
    "182.34.37.9:9999",
    "115.221.242.146:9999",
    "1.198.73.55:9999",
    "123.53.236.198:40143",
    "114.238.31.2:9999",
    "115.221.243.248:9999",
    "182.34.101.172:9999",
    "123.54.46.140:9999",
    "175.43.143.221:9999",
    "1.199.31.174:9999",
    "171.35.221.172:9999",
    "123.101.141.72:42106",
    "36.74.129.117:8080",
    "180.120.212.99:8888",
    "171.35.172.229:9999",
    "115.62.45.34:9999",
    "117.95.232.148:9999",
    "60.169.241.229:9999",
    "60.179.177.208:40378",
    "123.169.34.69:9999",
    "120.83.101.229:9999",
    "58.253.158.29:9999",
    "182.34.27.198:9999",
    "119.108.167.191:9000",
    "182.34.17.135:9999",
    "49.86.176.186:9999",
    "175.43.154.13:9999",
    "114.99.23.192:1133",
    "171.220.168.94:28341",
    "58.253.159.158:9999",
    "171.11.29.110:9999",
    "101.26.55.28:9999",
    "183.166.133.27:9999",
    "27.220.122.222:24854",
    "117.95.199.104:9999",
    "183.166.139.237:9999",
    "123.163.27.61:9999",
    "114.239.0.121:9999",
    "183.166.162.52:9999",
    "123.149.137.59:9999",
    "125.87.99.69:20314",
    "175.43.151.144:9999",
    "119.4.12.129:1133",
    "117.95.162.115:9999",
    "171.35.215.243:9999",
    "183.166.97.179:9999",
    "123.169.120.117:9999",
    "60.187.33.133:44314",
    "120.83.99.155:9999",
]
