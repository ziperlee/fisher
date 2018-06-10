"""
 Create by zipee on 2018/6/10.
"""
__author__ = 'zipee'

from flask import jsonify
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from manage import app

print('id={}注册路由'.format(id(app)))
@app.route('/search/book/<q>/<page>')
def search(q, page):
    """
    isbn13 由13个0到9数字组成
    isbn10 10个0到9数字组成 含有一些' - '
    """
    isbn_or_key = is_isbn_or_key(q)
    yushu_book = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushu_book.search_by_isbn(q)
    else:
        result = yushu_book.search_by_keyword(q, page)

    # return json.dumps(result), 200, {'content-type':'application/json'}
    return jsonify(result)