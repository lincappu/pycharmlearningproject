# !/usr/bin/env python3
# -*- coding -*-

# 练习题：
# 1.写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
# import os
#
#
# def modfify_file(file_name, old, new):
#     with open(file_name, 'r', encoding='utf-8') as read_f, open('swap', 'w', encoding='utf-8') as write_f:
#         for line in read_f:
#             if old in line:
#                 line = line.replace(old, new)
#             write_f.write(line)
#
#     os.remove(file_name)
#     os.rename('swap', file_name)
#
#
# modfify_file('test.txt', '她', '伊')


# 2.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# def check_number(msg):
#     res = {
#         'num': 0,
#         'string': 0,
#         'space': 0,
#         'other': 0,
#     }
#     for s in msg:
#         if s.isdigit():
#             res['num']+=1
#         elif s.isalpha():
#             res['string']+=1
#         elif s.isspace():
#             res['space']+=1
#         else:
#             res['other']+=1
#
#     return  res
#
# res=check_number('nihao      nifsdfs14234322343242  ffsdf!#$%^&*fsd fsfs23432')
# print(res)

# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def checklen(msg):
#     print(msg)
#     if len(msg) > 5:
#         print('ok')
#     else:
#         print('error')
#
# checklen((1,2,3,5,6,7))
# checklen({1,2,3,5,6,7})


# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def check_len(msg):
#     if len(msg) > 2 :
#         return msg[0:2]
#
#
# res=check_len(['1',2,'b'])
# print(res)

# 5.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def check1(msg):
#     return msg[::2]
# print(check1([1,2,3,4,5,6,7,8,9]))


# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。dic = {"k1": "v1v1", "k2": [11,22,33,44]}  PS:字典中的value只能是字符串或列表
# def check2(msg):
#     d={}
#     for k,v in msg.items():
#         if len(v) > 2 :
#             d[k]=v[0:2]
#     return d
#
# print(check2({'1':'asdfg','2':[1,2,3,4,56],'3':(1,2,3,4,5,6)}))



# 插入一个知识点：
# random函数
# import  random  # 导入 random random函数Ω模块
# print(random.random()) # 生成0-1.0之间的随机数
# print(random.uniform(1,10))  # 在一个指定范围的随机浮点数
# print(random.randint(1,10)) # 在一个指定范围内生成随机整数
# print(random.randrange(10.100.2)) # 在一个范围内按指定步长生成一个随机数
# print(random.choice('nihao zheshi shui ')) # 从这里面随机选一个。
# p=['python','is','powerfil','and','is','cool']
# print(random.shuffle(p)) # 将列表元素打乱
# p=[1,2,3,4,5,6,7]
# print(random.sample(p,2)) # 从列表中选取指定长度的的片段，但是原列表并不变

# 装饰器练习题
# 一：编写函数，（函数执行的时间是随机的）
# 二：编写装饰器，为函数加上统计时间的功能
# 三：编写装饰器，为函数加上认证的功能

# import  time
# import  random
#
# current_status={'user':None,'loging_status':False}
#
#
# def auth(egine='file'):
#     def timmer(func):
#         def inner(*args,**kwargs):
#              if current_status['user'] and current_status['loging_status']:
#                  res = func(*args, **kwargs)
#              if egine == 'file':
#                 name=input('name:').strip()
#                 pwd=input('password:').strip()
#                 if name == 'egon' and pwd == '123':
#                     print('login success')
#                     start_time = time.time()
#                     res = func(*args, **kwargs)
#                     stop_time = time.time()
#                     print('randtime 执行时间为%s : ' % (stop_time - start_time))
#                     return res
#         return inner
#     return  timmer
#
#
# @auth(egine='file')
# def randtime():
#     time.sleep(random.uniform(1,5))
#     print('执行完毕')
#     return 123
#
# res=randtime()
# print(res)

# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码,注意：从文件中读出字符串形式的字典，
# 可以用eval('{"name":"egon","password":"123"}')转成字典格式

# curreng_status={'user':None,'status':False}
#
#
# def auth(type='file'):
#     def wrap(func):
#         def inner(*args,**kwargs):
#             if curreng_status['user'] and curreng_status['status']:
#                 return func(*args,**kwargs)
#             if type == 'file':
#                 print('type is file')
#                 return func(*args,**kwargs)
#         return inner
#     return wrap
#
# @auth() # @wrap  index=wrap(index)
# def index():
#     print('from index function')
#     return 123
#
# index()

# 五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

# import time, random
#
# user = {'user': None, 'login_time': None, 'timeout':10.0,}
#
#
# def auth(func):
#     def inner(*args, **kwargs):
#         if user['user']:
#             timeout = time.time() - user['login_time']
#             if timeout < user['timeout']:
#                 return func(*args, **kwargs)
#         name = input('name:').strip()
#         pwd = input('pwd:').strip()
#         if name == 'egon' and pwd == '123':
#             user['user'] = name
#             user['login_time'] = time.time()
#             return func(*args, **kwargs)
#
#     return inner
#
#
# @auth
# def index():
#     time.sleep(random.uniform(1, 2))
#     print('from index')
#
#
# @auth
# def index2():
#     time.sleep(random.uniform(1,5))
#     print('fron index2')
#
#
# index()
# index2()
# print(user)


# 六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# from urllib.request import urlopen
#
#
# def pagedeown(url):
#     return urlopen(url).read()
#
#
# print(pagedeown('http://www.baidu.com'))

# 七：为题目五编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

# import os
# import urllib.request
#
# cache_file = 'cache.txt'
#
#
# def cache(func):
#     def inner(*args, **kwargs):
#         if not os.path.exists(cache_file):
#             with open(cache_file, 'w'): pass
#         if os.path.getsize(cache_file):
#             print('这时缓存文件')
#             with open(cache_file, 'rb') as f:
#                 res = f.read()
#         else:
#             res = func(*args, **kwargs)
#             with open(cache_file, 'wb') as f:
#                 f.write(res)
#         return res
#
#     return inner
#
#
# @cache
# def pagedown(url):
#     print('这是下载的文件')
#     return urlopen(url).read()
#
#
# pagedown('http://www.qq.com')

#
# 八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作#
# 九。编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017 - 07 - 21
# 11: 12:11
# f1
# run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
#
# time.strftime('%Y-%m-%d %X')
#
#
# import os
# import time
#
#
# def logger(file):
#     def deco(func):
#         if not os.path.exists(file):
#             with open(file, 'w') as f:
#                 pass
#
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             with open(file, 'a', encoding='utf-8') as f:
#                 f.write('%s %s run \n' % (time.strftime('%Y-%m-%d %X'), deco.__name__))
#                 return res
#
#         return wrapper
#
#     return deco
#
#
# @logger(file='aaaaaa.log')
# def index():
#     print('index')
#
#
# index()



# with open('access.log','a') as f:
#     f.write('aaaa404\n')
#     f.flush()
#


# import  sys
#
# with open('test','a') as f:
#     f.write(sys.argv[1])
#     f.write(sys.argv[2])





