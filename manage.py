"""
 Create by zipee on 2018/5/29.
"""
__author__ = 'zipee'

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    # return 'hello'
    # return '<html></html>'
    response = make_response('<html>123</html>', 301)
    headers = {
        'content-type' : 'application/json',
        'location' : 'http://www.bing.com'
    }
    response.headers = headers
    return response

# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    # 生产环境 nginx+uwsgi ，不运行自带服务器
    app.run(host=app.config['HOST'],
            debug=app.config['DEBUG'],
            port=app.config['PORT'])