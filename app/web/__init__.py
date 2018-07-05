"""
 Create by zipee on 2018/6/10.
"""
__author__ = 'zipee'

from flask import Blueprint


web = Blueprint('web', __name__)
# print('web={} 实例化'.format(id(web)))

# 视图函数导入注册
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
