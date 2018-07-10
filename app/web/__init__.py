"""
 Create by zipee on 2018/6/10.
"""
__author__ = 'zipee'

from flask import Blueprint, render_template

web = Blueprint('web', __name__)
# print('web={} 实例化'.format(id(web)))

@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404

# 视图函数导入注册
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
