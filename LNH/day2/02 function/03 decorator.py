# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 闭包函数：
# 定义在函数内部的函数，包含对外部作用域而不是全局作用域的引用，就是上一层函数的变量引用。

# 函数需要参数，有两种解决方案：
# 一种是直接传入参数：
# from urllib.request import  urlopen
#
# def get(url):
#     return urlopen(url).read()
#
# get('http://www.baidu.com')
#
# 另一种是包起来，将内部的函数 return出来。打破函数的层级限制。   注意作用域。
# def get(url):
#     def inner():
#         return urlopen(url).read()
#     return  inner
#
# baidu=get('http://www.baidu.com')
#
# print(baidu())
# baidu()  # 随时调用，不用再传参数了。


# 装饰器：
# 作用：
# 用来装饰他人，装饰器本身可以是任意可调用的对象，被装饰的对象可以是任意可调用对象。
# 原则:开放封闭原则，对扩展是开放的，对修改是封闭的
# 不修改被装饰对象的源代码，不修改被装饰对象的调用方式。
# 目标：在遵循1和2的原则下，为被装饰对象添加功能，


# 例子：
# 第一步：原始函数需求
# import  time
#
#
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
#
# index()

# 第二步：为原始函数添加新需求。
#
# import  time
#
#
# def inner(func):
#     star_time=time.time()
#     func()
#     stop_time=time.time()
#     print('run time is :[%s]' %(stop_time-star_time))
#
#
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
#
# inner(index)


# 第三步：上述的方式完成了新需求，但是更改了原始函数的调用方式：
# import time
#
#
# def timmer(func):
#     func= index # 最开始 index  传的是最开始的 index 的内存地址
#     def inner():
#         star_time = time.time()
#         func()
#         stop_time = time.time()
#         print('run time is :[%s]' % (stop_time - star_time))
#
#     return inner
#
#
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
#
# index = timmer(index)  # 这个 index 是 inner
# index()

#  简易写法：
# import time
#
#
# def timmer(func):
#     # func= index # 最开始 index  传的是最开始的 index 的内存地址
#     def inner():
#         star_time = time.time()
#         func()
#         stop_time = time.time()
#         print('run time is :[%s]' % (stop_time - star_time))
#
#     return inner
#
#
# @timmer  # index =timmer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# index()


# 加参数：
# import time
#
#
# def timmer(func):
#     def inner(*args,**kwargs):
#         star_time = time.time()
#         func(*args,**kwargs)
#         stop_time = time.time()
#         print('run time is :[%s]' % (stop_time - star_time))
#
#     return inner
#
#
# @timmer  # index =timmer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# @timmer
# def home(name):
#     time.sleep(1)
#     print('welcome to %s page' %(name))
#
#
# index()
# home('egon')
#
# 原始函数有返回值+函数属性转移

# import time
# from functools import  wraps
#
#
# def timmer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         star_time = time.time()
#         res=func(*args,**kwargs)
#         stop_time = time.time()
#         print('run time is :[%s]' % (stop_time - star_time))
#         return res
# inner.__doc__ = func.__doc__
# return inner
#
#
# @timmer  # index =timmer(index)
# def index():
#     '''
#     idnex function
#     :return:
#     '''
#     time.sleep(3)
#     print('welcome to index page')
#     return 123
#
# @timmer
# def home(name):
#     time.sleep(1)
#     print('welcome to %s page' %(name))
#     return  456
#
#
# res1=index()
# print(res1)
# res2=home('egon')
# print(res2)
# print(index.__doc__)




# 二。有参数装饰器
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
# @auth(egine='file') # 遇见了名字加（）先先执行函数，然后把这儿函数的返回值放在这，作为装饰器， # index=auth(egine='mysql')(index) #==#   @wrap  index=wrap(index)
# @timmer
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#     return 123
#
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
