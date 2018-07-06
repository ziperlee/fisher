"""
 Create by zipee on 2018/6/10.
"""
import json

from flask_login import current_user
from wheel.signatures.djbec import q

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection, _BookViewModel
from app.view_models.trade import TradeInfo

__author__ = 'zipee'

from flask import jsonify, request, render_template, flash
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
    # 若没有传入任何参数，form.validate()会返回false
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
        # return json.dumps(books, default=lambda o:o.__dict__)
    else:
        # return jsonify({'msg':'param verification failure, %s' % json.dumps(form.errors)})
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字')

    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # MVC MVT

    if current_user.is_authenticated: # 判断用户是否登录
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)

# @web.route('/test')
# def test():
#     r = {
#         'name':'lee',
#         'age':18
#     }
#     flash('hello, lee')
#     return render_template('test.html', data = r)