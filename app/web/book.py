"""
 Create by zipee on 2018/6/10.
"""
import json

from wheel.signatures.djbec import q

__author__ = 'zipee'

from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm

@web.route('/search/book')
def search():
    """
    isbn13 由13个0到9数字组成
    isbn10 10个0到9数字组成 含有一些' - '
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            result = yushu_book.search_by_isbn(q)
        else:
            result = yushu_book.search_by_keyword(q, page)

        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    else:
        # return jsonify({'msg':'param verification failure, %s' % json.dumps(form.errors)})
        return jsonify(form.errors)