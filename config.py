"""
 Create by zipee on 2018/6/9.
"""
__author__ = 'zipee'

# flask config默认配置DEBUG 为False
# falsk config配置中所以项必须要大写，否则不读取
DEBUG = False
HOST = '192.168.190.1'
PORT = 9000

# http://t.yushu.im
# 关键字搜索
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# isbn搜索
# http://t.yushu.im/v2/book/isbn/{isbn}9787111552062
# 豆瓣api
# https://api.douban.com/v2/book