"""
 Create by zipee on 2018/6/10.
"""
import json

from wheel.signatures.djbec import q

from view_models.book import BookViewModel, BookCollection, _BookViewModel

__author__ = 'zipee'

from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm

@web.route('/book/search')
def search():
    """
    isbn13 由13个0到9数字组成
    isbn10 10个0到9数字组成 含有一些' - '
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = _BookViewModel.package_single(result, q)
        else:
            yushu_book.search_by_keyword(q, page)
            # result = _BookViewModel.package_collection(result, q)
        books.fill(yushu_book, q)

        # return json.dumps(result), 200, {'content-type':'application/json'}
        # return jsonify(result) 无法直接序列化对象
        return json.dumps(books, default=lambda o:o.__dict__)
    else:
        # return jsonify({'msg':'param verification failure, %s' % json.dumps(form.errors)})
        return jsonify(form.errors)