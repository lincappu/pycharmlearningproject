#    有参装饰器的修订
# 1.参数
# 2.返回值
# 3.函数基本信息。

# import  time
# from  functools import  wraps
#
# def timmer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         end_time=time.time()
#         print('run time is :[%s]' % (end_time - start_time))
#         return res
#     inner.__doc__=
#     return inner
#
# @timmer   # index=timmer(index)
# def index(name):
#     time.sleep(1)
#     print('functiion index')
#     print(name)
#     return  123
#
#
# res=index('fls')
# print(res)
#





#
# import time
# from functools import wraps
#
# def timmer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is :[%s]' %(stop_time-start_time))
#         return res
#
#     return inner
#
# @timmer
# def index():
#     '''
#     index function
#     :return:
#     '''
#     time.sleep(3)
#     print('welcome to index page')
#     return 123
#
# @timmer #home=timmer(home) #home=inner
# def home(name):
#     time.sleep(2)
#     print('welcome %s to home page' %name)
#     return 456
#
# # res=index() # res=inner()
# # print(res)
# #
# # res=home('egon') #inner('egon')
# # print(res)
#
# # print(index.__doc__)
# print(help(index))

