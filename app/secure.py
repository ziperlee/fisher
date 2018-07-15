"""
 Create by zipee on 2018/6/13.
"""
__author__ = 'zipee'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lee:1qaz!QAZ@192.168.0.108:3306/fisher'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lee:1qaz!QAZ@127.0.0.1:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 消息闪现必须 作为用重置密码的token
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89f9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1473042956@qq.com' # 发送者为个人，可以注册企业电子邮箱
MAIL_PASSWORD = 'hefyernkjhrbgggc' # 非qq邮箱密码
