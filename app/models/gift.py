"""
 Create by zipee on 2018/7/5
"""
__author__ = 'zipee'


from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship
from flask import current_app
from collections import namedtuple

from app.spider.yushu_book import YuShuBook


EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        # 根据传入的一组isbn，到Wish表中计算出某个礼物
        # 的Wish心愿数量
        # 一个数量吗？
        # 一组数量
        # 条件表达式
        # mysql in
        # isbn wish的数量
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        # count_list[0][1]
        # 对象
        # 字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    # class A:
    #     count
    #     isbn

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物，具体
    # 类代表礼物这个事物，它是抽象，不是具体的“一个”
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数
        # first() all()
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift

        # @classmethod
        # def get_wish_counts(self, isbn_list):
        #     count_list = db.session.query(func.count(Wish.id), Wish.isbn). \
        #         filter(Wish.launched == False, Wish.isbn.in_(isbn_list),
        #                Wish.status == 1).group_by(Wish.isbn).all()
        #     count_list = [EachGiftWishCount(w[0], w[1]) for w in count_list]
        #     return count_list
