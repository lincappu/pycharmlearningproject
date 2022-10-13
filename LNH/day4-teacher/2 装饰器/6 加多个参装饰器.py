# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 有参装饰器：
# 其实就是装饰器函数也需要函数的话，那就需要包一层，将换来的被装饰器函数变成装饰器函数。最外层的函数接收参数，并且只需写一个就可以，可以接收任意参数，然后内部就是装饰器函数，最内部的才是被装饰的对象。


import  time
from  functools import wraps

current_status = {'user': None, 'login_status': False}


def timmer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        end_time=time.time()
        print('time:%s' %(end_time-start_time))
        return res
    return inner

def auth(drive):
    def  wrap(func):
        def inner(*args, **kwargs):
            if current_status['user'] and current_status['login_status']:
                print('login success')
                res = func(*args, **kwargs)
                return res
            if drive == 'file':
                name = input('name:').strip()
                pwd = input('password:').strip()
                if name == 'egon' and pwd == '123':
                    print('login success')
                    current_status['user'] = name
                    current_status['login_status'] = True
                    res = func(*args, **kwargs)
                    return res
            elif drive == 'mysql':
                print('mysql auth')
            elif drive == 'ldpa':
                print('ldpa auth')
            else:
                print('nothing')
        return inner
    return wrap



@auth('file')
@timmer
def index(name):
    print('this is function index ')
    print(name)
    return 123

res=index('fls')
print(res)






#
#
# import time
#
# current_status = {'user': None, 'login_status': False}
#
#
# def timmer(func):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         res=func(*args,**kwargs)
#         stop_time = time.time()
#         print('randtime 执行时间为%s : ' % (stop_time - start_time))
#         return res
#     return inner
#
#
# def auth(egine='file'):
#     def wrap(func):
#         def inner(*args, **kwargs):
#             if current_status['user'] and current_status['login_status']:
#                 res = func(*args, **kwargs)
#                 return res
#             if egine == 'file':
#                 name = input('name:').strip()
#                 pwd = input('password:').strip()
#                 if name == 'egon' and pwd == '123':
#                     print('login success')
#                     current_status['user'] = name
#                     current_status['login_status'] = True
#                     res = func(*args, **kwargs)
#                     return res
#             elif egine == 'mysql':
#                 print('mysql auth')
#             elif egine == 'ldpa':
#                 print('ldpa auth')
#             else:
#                 print('nothing')
#         return inner
#     return wrap
#
#
# @auth(egine='file') # 遇见了名字加（）先执行函数，然后把这儿函数的返回值放在这，作为装饰器， # index=auth(egine='mysql')(index) #==#   @wrap  index=wrap(index)
# @timmer
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#     return 123

#
# @auth(egine='file')
# @timmer
# def home(name):
#     time.sleep(1)
#     print('welcome to %s page' %(name))
#     return 456
#
#
# res1=index()
# print(res1)
# res2=home('egon')
# print(res2)