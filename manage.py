"""
 Create by zipee on 2018/5/29.
"""


__author__ = 'zipee'

app = Flask(__name__)
app.config.from_object('config')
print('id={} 实例化'.format(id(app)))

from app.web import book




if __name__ == '__main__':
    print('id={} 启动'.format(id(app)))
    # 生产环境 nginx+uwsgi ，不运行自带服务器
    app.run(host=app.config['HOST'],
            debug=app.config['DEBUG'],
            port=app.config['PORT'])