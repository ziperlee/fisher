"""
 Create by zipee on 2018/6/18.
"""
__author__ = 'zipee'

from flask import Flask, current_app

app = Flask(__name__)

# a = current_app
# pass

# with app.app_context():
#     a = current_app
#     pass

# class MyResource:
#     def __enter__(self):
#         print('connect to resource')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_tb:
#             print('process exception')
#         else:
#             print('no exception')
#         print('close resource connection')
#         return True
#     def query(self):
#         print('query resource')
#
# with MyResource() as resource:
#     resource.query()


# class Local(object):
#     # __slots__ = ('__storage__', '__ident_func__')
#
#     def __init__(self):
#         # object.__setattr__(self, '__storage__', {})
#         # object.__setattr__(self, '__ident_func__', get_ident)
#         # self.__storage__ = {}
#         self.__storage__ = {}
#
#     def __getattr__(self, key):
#         return self.__storage__[key]
#     #
#     def __setattr__(self, key, value):
#         # self.__storage__[key] = value
#         pass
#     def query(self):
#         return self.__storage__
#
# local = Local()
# local.__storage__['hah'] = 1
# print(local.query())
# print(local.hah)


from werkzeug.local import LocalStack
import threading
import time

stack = LocalStack()
stack.push(1)
print('main thread value is {}'.format(stack.top))

def work():
    print('{} value is {}'.format(threading.current_thread().name, stack.top))
    stack.push(2)
    print('{} value is {}'.format(threading.current_thread().name, stack.top))

if __name__ == '__main__':
    t = threading.Thread(target=work, name='lee')
    t.start()
    time.sleep(1)
    print('main thread value is {}'.format(stack.top))