"""
 Create by zipee on 2018/5/29.
"""
from app import create_app

__author__ = 'zipee'

app = create_app()

if __name__ == '__main__':
    # 生产环境 nginx+uwsgi ，不运行自带服务器
    app.run(host=app.config['HOST'],
            debug=app.config['DEBUG'],
            port=app.config['PORT'])