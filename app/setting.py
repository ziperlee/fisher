"""
 Create by zipee on 2018/6/13.
"""
__author__ = 'zipee'

# flask config默认配置DEBUG 为False
# falsk config配置中所以项必须要大写，否则不读取
DEBUG = True
HOST = '127.0.0.1'
PORT = 9000
PER_PAGE = 15
BEANS_UPLOAD_ONE_BOOK = 0.5
RECENT_BOOK_COUNT = 30

# http://t.yushu.im
# 关键字搜索
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# isbn搜索
# http://t.yushu.im/v2/book/isbn/{isbn}9787111552062
# 豆瓣api
# https://api.douban.com/v2/book