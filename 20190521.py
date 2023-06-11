# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
import sys
import os

# x = 1 - 2j
# print(x.imag)
# print(x.real)
#
# name='a|b|c'
# l=name. split('|',2)
# print(l)


# x = 'hello'
# print(x[1])
# print(x[0:1:1])
# print(x[0::-1])



# f = open('log', 'r+')
# print(f.name)
# print(f.closed)
# print(f.mode)
# print(f.writable())
# print(f.encoding)
# print(f.encoding)
# print(f.readable())

# f.write('123456789')
# f.close()

# f.writelines(['1\n','2\n','3\n'])
# print(f.read())
# f.close()


# log=f.read()
# print(log)

# log=f.read(4)
# print(log)
# str=f.tell()
# print(str)
#
# log2=f.read(3)
# print(log2)
#
# pos=f.seek(2,0)
# log3=f.read(2)
# print(log3)
#
# f.close()


# print(f.readline())
# print(f.readlines())
# for  line in f:
#     print(line)




# f=open('log','a')
# f.write('\n0')
# f.close()


# f=open('log','rb')
# print(f.readline())




# if len(sys.argv) != 3:
#     print('Usage cp source_file dest_file')
#     sys.exit(1)
#
# source_file,dest_file=sys.argv[1],sys.argv[2]
# with open(source_file,'rb') as read_f, open(dest_file,'wb') as dest_f:
#     for line in  read_f:
#         dest_f.write(line)
#
# with open('log','rb') as f:
#     f.seek(0,2)
#     while True:
#         line=f.readline()
#         if line:
#             print(line)



# with open('log') as s,open('new','w') as d:
#     for  line in s:
#         line=line.replace('alex','sb')
#         d.write(line)



# sum = 0
# with open('log') as f:
#     for line in f:
#         name = line.split()[0]
#         price = line.split()[1]
#         num = line.split()[2]
#         print('本次购买的商品为：%s 价钱为：%s 数量为：%s' % (name, price, num))
#         sum += int(price) * int(num)
#
#         print(sum)





import os

# product = [
#     []
#
# ]
#
# db_file = 'log'
# current_info = {}
#
# user_name =[]
#
# with open('log', 'r') as f:
#     for line in f:
#         user = line.strip().split('|')
#         user_name.append(user[0])
#
# while True:
#     print('''
#     1 登陆
#     2 注册
#     3 购物
#     ''')
#     choice = input('请输入>>:').strip()
#
#     if choice == '1':
#         tag = True
#         count = 0
#         while tag:
#             if count == 3:
#                 print('你尝试次数过多，已锁定')
#                 break
#
#             uname = input('your name>:').strip()
#             upasswd = input('your password>:').strip()
#
#             if uname in user_name:
#                 with open(db_file, 'r') as f:
#                     for line in f:
#                         line = line.strip()
#                         user_info = line.split('|')
#                         name = user_info[0]
#                         passwd = user_info[1]
#                         if uname == name and upasswd == passwd:
#                             print('登陆成功')
#                         balance =input('your balance>:').strip()
#                         balance=int(balance)
#                         current_info[uname] = balance
#                         tag = False
#                         break
#                      else:
#                         print('用户名或者密码错误')
#                         count += 1
#             else:
#                 print('用户名不存在,请重新输入！')
#
#
#
#     else:
#         print("输入非法，请重新输入")


# f=open('log','r')
#
# for index,line in enumerate(f.readlines()):
#     if index == 2:
#         print('这时第三行')
#         continue
#     print(index)
# print(line,end='')

#
# with open('log','rb') as f:
#     data=f.read()
#     print(data.decode('utf-8'))


# import  time
# with open('log',mode='rb') as f:
#     f.seek(0,2)
#     while True:
#         line = f.read()
#         if line:
#             print(line.decode('utf-8'),end='')
#         else:
#             time.sleep(0.2)




# a,b,c='hello'

# data=['mac',10000,[2016,10,12]]
# _,price,_=data
# print(price,_)




# ############函数练习题：
# import os
# def mod(filename, old, new):
#     with open(filename, 'r') as rf , open('.bak', 'w') as wf:
#         for line in rf:
#             if old in line:
#                 line=line.replace(old,new)
#             wf.write(line)
#
#     os.remove(filename)
#     os.rename('.bak',filename)
#
#
# mod('log','1','2')
#


# def check(meg):
#     res={
#         'num':0,
#         'str':0,
#         'space':0,
#         'other':0
#     }
#
#     for   i in meg:
#         if i.isdigit():
#             res['num']+=1
#         elif i.isalpha():
#             res['str']+=1
#         elif i.isspace():
#             res['space']+=1
#         else:
#             res['other']+=1
#
#     return res
#
#
# res=check('fsdfsfr3423 fsf;;[fs %^&^%$( & df]fsdfsdf')
# print(res)




# def check(*args):
#     n=len(args)
#     print(n)
#     i =0
#     while i < n:
#         if len(args[i]) > 5:
#             print(len(args[i]))
#             print(args[i])
#         i+=1
#
# n=check(['a','b','c','d','e','f'],['1','2','3'],('1',2,3,4,5,6,8,9,9))
# print(n)
#


# x=10
#
# print(globals())
# print(locals())




# 装饰器：

# import time
# from functools import wraps
#
#
# def timer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s' %(stop_time-start_time))
#         return  res
#     return inner
#
#
# @timer     #  index=timer(index)
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#     return 123
#
#
# @timer
# def  home(name):
#     time.sleep(1)
#     print('function name %s' %name)
#
#
#
#
# res=index()
# print(res)
# res1=home('egon')
# print(res1)
#




# from functools import   wraps
# import  time
#
# statu={'name':None,'status':False}
#
# def timmer(func):
#     func=index
# @wraps(func)
# def inner(*args,**kwargs):
#     start_time=time.time()
#     res=func(*args,**kwargs)
#     stop_time=time.time()
#     print('time :%s' %(stop_time-start_time) )
#     return res
# return inner
#
# def auth(egine):
#     def wrap(func):
#         @wraps(func)
#         def inner(*args,**kargs):
#             if statu['name'] and statu['status']:
#                 res=func(*args,**kargs)
#                 return res
#
#             if egine=='file':
#                 name=input('your name>:').strip()
#                 passwd=input('your password:>').strip()
#                 if name == 'egon' and passwd == '123':
#                     print('login successful')
#                     statu['name']=name
#                     statu['status']=True
#                     res=func()
#                     return res
#             elif  egine=='db':
#                 res=func()
#                 return res
#                 print('auth pass db')
#             else:
#                 print('other')
#         return  inner
#     return wrap
#
# @auth('db')
# @timmer
# def index():
#      time.sleep(3)
#      print('function index')
#      return  123
#
# res=index()
# print(res)
#
#







# import  os
# import time
#
# from  functools import  wraps
#
# def logger(file):
#     def wrap(func):
#         if not os.path.exists(file):
#             with open('file','w'):
#                 pass
#         def inner(*args,**kwargs):
#             res=func(*args,**kwargs)
#             with open(file,'a',) as f:
#                 f.write('%s function run %s ' %(time.strftime('%Y-%m-%d %X'),func.__name__))
#             return res
#         return inner
#     return wrap
#
#
# @logger(file='log')
# def index():
#     print('function index')
#     return 123
#
#
# index()
#



# from collections import  Iterable,Iterator
# print(isinstance('hello',Iterable))
# print(isinstance('hello',Iterator))
# l='hello'.__iter__()
# print(isinstance(l,Iterator))
#

#
# def myrange(start,stop,step):
#     while start < stop:
#         yield start
#         start+=step
#
# g=myrange(1,100,10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for i  in myrange(1,10,1):
#     print(i)




# tail -f accesss.log | grep '404'
# import  time
# def tail(file):
#     with open(file,'rb') as f:
#         f.seek(0,2)
#         while True:
#             line = f.readline()
#             if line:
#                 yield  line
#             else:
#                 time.sleep(0.2)
#
# def grep(pattern,lines):
#     for line in lines:
#         line=line.decode('utf-8')
#         if pattern in line:
#             yield line
#
#
# g=grep('404',tail('log'))
# for line in g:
#     print(line,end='')






# 复制代码
# 题目一：
# def init(func):
#     def wrapper(*args,**kwargs):
#         g=func(*args,**kwargs)
#         next(g)
#         return g
#     return wrapper
#
# @init
# def eater(name):
#     print('%s 准备开始吃饭啦' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         print('%s 吃了 %s' % (name,food))
#         food_list.append(food)
#
# g=eater('
# egon')
# g.send('蒸羊羔')




# dic={'name':'fls','age':12}
# str=str(dic)
#
#
# with open('log','w') as f:
#     f.write(str)
#
# with open('log','r') as f:
#     line=f.readline()
#     print(line,type(line))
#     print(line['name'])

import pickle
import json

# d = dict(name='fls', age=4322)

# print(pickle.dumps(d))
#
# with open('log','wb') as f:
#     pickle.dump(d,f)

# with  open('log','rb') as f:
#     line=pickle.load(f)
#     print(line,type(line))
#


# json.dumps(d)
# with open('log','wb')  as f:
#     json.dump(d,f)


# # l=[]
# l = [1,2,3,4,5,6,7,12,32,43,47]
# def search(l,n):
#     if  not len(l):
#         print('not exist')
#         return  False
#
#     mid=len(l)//2
#
#     if l[mid]==n:
#         print('found it %s' %l.index(n))
#         return   True
#     if n > l[mid]:
#         return search(l[mid:],n)
#     else:
#         return search(l[:mid],n)
#
#
#
#
# search(l,3)


# l = [1, 2, 3, 4, 5, 6, 7, 12, 32, 43, 47]
#
#
# def search(l, n):
#     start = 0
#     stop = len(l)
#
#     while start < stop:
#         mid = (start + stop) // 2
#         if l[mid] == n:
#             print('found it',l.index(n))
#         if l[mid] > n:
#             stop = mid - 1
#         else:
#             start = mid + 1
#     return False
#
#
# search(l, 6)


# func=lambda x,y,z:x*y*z
#
# print(func(1,4,6))




# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }

# l=sorted(salaries,key=lambda x:salaries[x],reverse=True)
# print(l)

# students = [
#     {'name':'zhangsan','age':17},
#     {'name':'lisi','age':19},
#     {'name':'wanger','age':15}
# ]
#
#
# print(sorted(students,key=lambda x:x['age'],reverse=True))
#



# import  math
#
# print(divmod(100,9))
#
# print(math.floor(5.5/2))



#
#
# print(round(123.434234,2))
# print(round(123.434234,-2))
# print(round(123.434234))



# print(sum((1,2,3,4))) sum 传入的参数必须是可迭代对象。


# print(int(12.432))
#
# print(int('-12'))
# print(int('21',8))]


# v= memoryview(b'fls')
# print(v[1])
# print(v[1:2])
# print(bytes(v[1:2]))


# print(chr(99))
# print(ord('a'))

# print(bin(324324))
#
# print(tuple('12345'))


# a=list(range(100))    #  slice 返回的是一个切片对象，并不是一个切片函数，是一个构造函数。
# x=slice(1,100,10)
# print(a[x])



# x=[1,2,3,0]
# y=[4,5,6]
# xy=zip(x,y)
# print(type(xy))
# print(list(xy))
#
#
# print(id(x))
#
#
# print('\033[0;31;0m nihao\033[0m')





# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())



# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
#
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())


# eval 执行表达式： 自动有返回值，不能执行语句
# exec 执行语句：  没有返回值，
# 表达式和语句区别


# print(eval('1*3+4'))
# print(exec('for i in range(19)'))




# info=[]
# with open('log','r') as f:
#     for line in f:
#         name,sex,age,salary=line.split()
#         info.append({'name':name,'sex':sex,'age':age,'salary':salary})
#     print(info)

# with open('log','r') as f1:
#     item=(line.split() for line in f1)
#     info=[{'name':name,'sex':sex,'age':age,'salary':salary}  for name,sex,age,salary in item]
#     print(info)
#



# with open('log','r') as f:
#     item=(line.split() for line in f )
#     info =[{'name':name,'sex':sex,'age':age,'salary':salary} for name,sex,age,salary in item]
#     print(info)
#
# print(max(info,key=lambda x:x['salary']))
# print(min(info,key=lambda x:x['age']))
#
#
#
#
# # info_new=map(lambda item:{'name':item['name'].capitalize(),
# #                           'sex':item['sex'],
# #                           'age':item['age'],
# #                           'salary':item['salary']
# #                          },info)
# # print(info_new)
# # print(list(info_new))
# #
#
#
# info_new=filter(lambda item:item['name'].startswith('a'),info)
# print(info_new)
# print(list(info_new))
#
#
# print(map(lambda x:x-1,range(5)))



# def fib(a,b,stop):
#     if a > stop:
#         return
#     print(a,end=' ')
#     fib(b,a+b,stop)
#
# print()
# fib(0,1,1000)


#########常用模块##########

####logging 日志模块：
import logging
#
#
# logging.basicConfig(
#     level=10,
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename='log'
#
# )
#
#
# logging.info('info')
# logging.warning('warning')
# logging.debug('debug')
# logging.error('error')
# logging.critical('critical')





# logger=logging.getLogger(__file__)
#
# h1=logging.FileHandler('log1')
# h2=logging.FileHandler('log2')
# h3=logging.StreamHandler()
#
# f1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# f2=logging.Formatter('%(asctime)s :  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# f3=logging.Formatter('%(name)s %(message)s',)
#
# h1.setFormatter(f1)
# h2.setFormatter(f2)
# h3.setFormatter(f3)
#
# logger.addHandler(h1)
# logger.addHandler(h2)
# logger.addHandler(h3)
# logger.setLevel(10)
#
# logger.debug('debug')





# logger和 handler 同时设置了 level时，如何生效。
# import logging
# from  logging.handlers import RotatingFileHandler
#
# form=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# ch=logging.StreamHandler()
#
# r=logging.handlers.RotatingFileHandler
#
#
#
# ch.setFormatter(form)
# ch.setLevel(10)
# # ch.setLevel(20)
#
#
#
# l1=logging.getLogger('root')
# # l1.setLevel(20)
# l1.setLevel(10)
# l1.addHandler(ch)
#
# l1.debug('l1 debug')






#
# """
# logging 字典配置：
# """
#
# import os
# import logging.config
#
# # 定义三种日志输出格式 开始
#
# standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
#                   '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
#
# simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#
# id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
#
# # 定义日志输出格式 结束
#
# logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
#
# logfile_name = 'all2.log'  # log文件名
#
# # 如果不存在定义的日志目录就创建一个
# if not os.path.isdir(logfile_dir):
#     os.mkdir(logfile_dir)
#
# # log文件的全路径
# logfile_path = os.path.join(logfile_dir, logfile_name)
#
# # log配置字典
# LOGGING_DIC = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': standard_format
#         },
#         'simple': {
#             'format': simple_format
#         },
#     },
#     'filters': {},
#     'handlers': {
#         #打印到终端的日志
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',  # 打印到屏幕
#             'formatter': 'simple'
#         },
#         #打印到文件的日志,收集info及以上的日志
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
#             'formatter': 'standard',
#             'filename': logfile_path,  # 日志文件
#             'maxBytes': 1024*1024*5,  # 日志大小 5M
#             'backupCount': 5,
#             'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
#         },
#     },
#     'loggers': {
#         #logging.getLogger(__name__)拿到的logger配置
#         '': {
#             'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
#             'level': 'DEBUG',
#             'propagate': True,  # 向上（更高level的logger）传递
#         },
#         'collect': {
#             'handlers': ['console', 'collect'],
#             'level': 'INFO',
#         },
#     },
# }
#
#
# def load_my_logging_cfg():
#     logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
#     logger = logging.getLogger(__name__)  # 生成一个log实例
#     logger.info('It works!')  # 记录该文件的运行状态
#
# if __name__ == '__main__':
#     load_my_logging_cfg()
#
#

# # 调用:
#
# # logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，但是拿着该名字去loggers里找key名时却发现找不到，
# # 于是默认使用key=''的配置
#
# logger=logging.getLogger(__name__)
# collect_logger=logging.getLogger('collect')




##### RE 模块###
import time
#
# print(time.time())
# print(type(time.time()))
# print(time.strftime('%Y-%m-%d'))
# print(time.localtime())
# print(time.gmtime())
#
# print(time.mktime(time.localtime()))
#
# print(time.asctime())
#
# print(time.ctime())
# print(time.ctime(time.time()))

# print(time.clock())
# time.sleep(2)
# print(time.clock())

import datetime
#
# print(datetime.datetime.now())
# print(datetime.date.strftime())
#

# import  calendar


# print(calendar.firstweekday())
#
# print(calendar.year(2017))
#
# print(calendar.calendar(2019))




import random

l = ['1', '2', 'a', 'b', 'c']
# print(random.random())
# print(random.randint(1,10))
# print(random.randrange(1,11))
# print(random.choice(['1','2','3','6']))
# print(random.choices(['a','b']))

# print(dir(random))
#
# print(random.uniform(1,2.5))
#
# print(random.getstate)
# print(random.getrandbits(3))


# print(random.shuffle(l))
# print(random.sample(l,2))



####随机验证码
# def make_code(n):
#     res=''
#     for i in range(n):
#         s1=chr(random.randint(65,90))
#         s2=str(random.randint(0,9))
#         res+=random.choice([s1,s2])
#         print(res)
#     return res
#
# print(make_code(9))




####os模块
# print(os.getcwd())
# print(os.chdir('/Users/FLS/test'))
# print(os.getcwd())
#
# print(os.curdir)

# print(os.mkdir('os'))
# print(os.rmdir('os'))
# print(os.makedirs('a/b'))
# print(os.removedirs('a/b'))
# print(os.listdir())

# print(os.remove('downloaded_data.txt'))

# print(os.rename('test.log','testnew.log'))
# print(os.stat('testnew.log'))
# print(os.sep)
# print(os.linesep)
# print(os.pathsep)
# print(os.name)
# print(os.system('ls -la'))
# print(os.environ)
# print(os.path.abspath('testnew.log'))
# print(os.path.split('/Users/FLS/test/testnew.log'))
# print(os.path.dirname('/Users/FLS/test/testnew.log'))
# print(os.path.basename('/Users/FLS/test/testnew.log'))
# print(os.path.split('/Users/FLS/test/testnew.log'))
# print(os.path.exists('/Users/FLS/test/testnew.log'))
# print(os.path.isfile('/Users/FLS/test/testnew.log'))
# print(os.path.isdir('/Users/FLS/test/testnew.log'))
# print(os.path.isabs('/Users/FLS/test/testnew.log'))
# print(os.path.join('/Users/FLS/test/','testnew.log'))
# print(os.path.getatime('/Users/FLS/test/testnew.log'))
# print(os.path.getmtime('/Users/FLS/test/testnew.log'))




####sys模块
# print(sys.argv)
# print(sys.modules)
# print(sys.path)
# print(sys.version)


# print('[%%-%ds]'%50) #[%-50s]
# print(('[%%-%ds]' %50) %'#')
# print(('[%%-%ds]' %50) %'##')
# print(('[%%-%ds]' %50) %'###')

# print('%s%%' %(100))
# print('[%%-%ds]' %50)
# print(('[%%-%ds]' %50) %'#')


####打印进度条
# import os
# import sys
#
# def progress(percent,width=50):
#     if percent > 1:
#         percent=1
#
#     show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
#     print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True)
#
#
# data_size=10250
# recv_size=0
# while recv_size < data_size:
#     time.sleep(0.1) #模拟数据的传输延迟
#     recv_size+=1024 #每次收1024
#
#     percent=recv_size/data_size #接收的比例
#     progress(percent,width=70) #进度条的宽度70


# import  shutil
#
# ret=shutil.make_archive('test','gztar','/Users/FLS/test/alpha-user')
#
# import  os
# print(os.getcwd())
# print(os.listdir())
# print(os.)




import zipfile
# import os
#
# print(os.chdir('/Users/FLS/test/'))
#
# z=zipfile.ZipFile('test.zip','w')
# z.write('1')
# z.write('2')
# z.write('3')
# z.close()


# z=zipfile.ZipFile('test.zip','r')
# z.extractall(path='.')
# z.close()



# import  tarfile

# t=tarfile.open('test.tar','w')
# t.add('a')
# t.add('b')
# t.add('c')
# t.close()


# t=tarfile.open('test.tar','r')
# t.extractall(path='.')
# t.close()



# import os

# print(os.chdir('/Users/FLS/test/'))
#
#
# import  shelve
#
# f=shelve.open(r'shelve.tst')
# f['stu']={'name':'fls','age':18,'hobby':['eat','drink']}
# print(f['stu']['hobby'])
# f.close()






# import  configparser
#
#
# config=configparser.ConfigParser()
# config.read('log')


# res=config.sections()
# print(res)
#
# option=config.options('section1')
# print(option)
#
# item_list=config.items('section1')
# print(item_list)

# val=config.get('section1','user')
# print(val)

# val=config.getint('section1','age')
# print(val)
# print(type(val))

# config.remove_section('section2')
#
# config.write(open('log','w'))
#




import hashlib
#
# m=hashlib.md5()
#
#
# m.update('hello'.encode('utf-8'))
# print(m.hexdigest())
#
#
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())



#
# h=hashlib.sha256('nihao'.encode('utf-8'))
# h.update('12345'.encode('utf-8'))
# print(h.hexdigest())



#
# import hmac
#
# h=hmac.new('nihao'.encode('utf-8'))
# h.update('wp'.encode('utf-8'))
# h.update('12345'.encode('utf-8'))
# print(h.hexdigest())




import re

# print(re.findall(r'\w','fsdf fsdf '))
# print(re.findall(r'\W','fsdfd fdsf  '))
# print(re.findall(r'\s','fsdf '))
# print(re.findall(r'\S','fsdf fsdf fd \n \t'))
#
# print(re.findall(r'\d',))

# .  除了换行符外的所有字符
# *  0或者多个字符
# +  1 或者多个字符
# ？ 0或者 1 个前面重复的字符



# class Dog:
#     counter=0
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#         Dog.counter+=1  #  类的属性，就用   类名.属性  调用
#
#
#
# a=Dog('wangcai','tugou')
#
# print(a.__dict__['name'])
# print(a.name)
# print(a.counter)
# print(a.__class__)
# print(a.__str__())
# print(a.__module__)




# 圆的周长和面积
# from  math import  pi
#
# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return  self.r**2*pi
#     def perimeter(self):
#         return self.r*2*pi
#
#
#
# c=circle(5)
# print(c.area())
# print(c.perimeter())



# 异常处理:
# 语法异常：无法屏蔽，在语法检查的时候就报出来了。还没有执行。
# 逻辑异常：程序运行时报错。





# s1='hello'
# try:
#     print(int(s1))
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
#
# finally:
#     print('无论是否报错，都将执行这句')
# else:
#     print('没有异常，才会执行')
#
# try:
#     raise TypeError('类型错误')
# except Exception as e:
#     print(e)


# 自定义异常：
#

#
# try:
#     raise EvaException('类型错误')
# except EvaException as e:
#     print(e)


# 断言：使用断言就不用在用 if-else 来做判断，如果有异常会自动报错，不会执行下面的语句。
# l=[]
# assert  len(l) > 0
# print(l[0])



# 反射当前模块成员：
# import  sys
#
# a=1111
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#
# this_module=sys.modules[__name__]
#
# print(hasattr(this_module,'a'))
# print(getattr(this_module,'a'))
#
#
# print(getattr(this_module,'f1'))
# getattr(this_module,'f1')()





# 单例模式四中实现方式：
# 1、使用模块
# python 的模块天然就是单例。所有的模块.py文件在编译成pyc后，再次执行的时候会直接执行 pyc，而不是再执行 py 文件了

# 2、使用__new__关键字
# class singleton():
#     __instance=None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance=super(singleton, cls).__new__(cls,*args,*kwargs)
#         return cls.__instance
#
# class myclass(singleton):
#     a=1
#
#
# c=myclass()
# b=myclass()
#
#
# print(id(c))
# print(id(b))


# 3、使用装饰器：

# from functools import  wraps
#
# def singleton(cls):
#     instance={}
#
#     @wraps(cls)
#     def getinstance(*args,**kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args,**kwargs)
#             return instance[cls]
#     return getinstance
#
#
# @singleton
# class myclass():
#     a=1
#
#
# b=myclass
# c=myclass
# print(id(b))
# print(id(c))





#####subprocess  执行子命令：
# obj1= subprocess.Popen('ls -la',shell=True,
#                       stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
#
# obj2= subprocess.Popen('grep  log',shell=True,
#                        stdin=obj1.stdout,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)
#
# stdout_res=obj2.stdout.read()
# stderr_res=obj2.stderr.read()
#
# print(stdout_res.decode('utf-8'))   # 收到的数据都是 bytes 类型，都要解码
# print(stderr_res.decode('utf-8'))





import socket
import subprocess
import os
import sys
import struct

# tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#
# tcp.bind(('127.0.0.1',8081))
#
# tcp.listen(5)
#
# while True:
#     print('开始监听：')
#     conn,client_addr=tcp.accept()
#     print('客户端信息：%s' %(client_addr))
#     while True:
#
#         cmd=conn.recv(1024)
#
#         if len(cmd) ==0:
#             break
#
#         # cmd=cmd.decode('utf-8')
#
#         obj= subprocess.Popen(cmd.decode('utf-8'),shell=True,
#                               stdout=subprocess.PIPE,
#                               stderr=subprocess.PIPE)
#
#         stdout_res=obj.stdout.read()
#         stderr_res=obj.stderr.read()
#
#
#         print('')



######## str 和 bytes 类型的转换。
#
#
# # bytes object
#  2  b = b"example"
#  3
#  4  # str object
#  5  s = "example"
#  6
#  7  # str to bytes
#  8  bytes(s, encoding = "utf8")
#  9
# 10  # bytes to str
# 11  str(b, encoding = "utf-8")
# 12
# 13  # an alternative method
# 14  # str to bytes
# 15  str.encode(s)   # 字符串转bytes
# 16
# 17  # bytes to str   # bytes转字符串
# 18  bytes.decode(b)
# 复制代码


######struct 函数的应用

#
# import struct
# #
# b=struct.pack('i',89)
# print(struct.unpack('i',b)[0])






############# 并发、进程######
from  multiprocessing import Process
import time
import os
#
# # # 1、
# def a(name,sex):
#     print('%s  %s 在工作  %s %s' %(name,sex,os.getpid(),os.getppid()))
#     time.sleep(3)
#     print('%s  %s工作完成' %(name,sex))
#
# if __name__ == '__main__':
#     p=Process(target=a,name='test',args=('egon',),kwargs={'sex':'male'})
#     p.start()
#     print(p.pid)
#     time.sleep(2)  # 这个很有意思，通过设置这个时间来决定子进程的运行时间
#     print(p.terminate())  # 如果子进程还启动了子子进程，那么杀掉子进程后，子子进程就会编程孤儿进程，所以不建议终止进程
#     print(p.is_alive())
#     print(p.name)
#     print('主进程 %s' %(os.getpid()))

# 2、
# class b(Process):
#     def __init__(self,name):
#         super(b, self).__init__()
#         self.name=name
#
#     def run(self):  #
#         print('%s 在工作' %self.name)
#         time.sleep(3)
#         print('%s 工作完成' %self.name)
#         print(p.is_alive())
#
# if __name__ == '__main__':
#     p=b('egon')
#     p.start()   # p.start 会出发 run 方法的执行，所以上面必须有一个 run 方法
#     print('主进程')
#     print(p.is_alive())



# 并发版本的 tcp socket版本：
# from multiprocessing import Process
# import  socket
#
# def talk(conn,addr):
#     while True:
#         try:
#             data=conn.recv(1024)
#             if not data:
#                 continue
#             conn.send(data.upper())
#         except Exception:
#             break
#     conn.close()
#
#
# def server():
#     ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     ss.bind(('127.0.0.1',8088))
#     ss.listen(5)  # 最大同时处理的的并发数，过多的会挂起
#     while True:
#         conn,addr=ss.accept()
#         print('客户端 %s %s'%(addr[0],addr[1]))
#         p=Process(target=talk,args=(conn,addr))
#         p.start()
#     ss.close()
#
#
# if __name__ == '__main__':
#     server()

# 客户端：
# import socket
# ss=socket.socket()
# ss.connect(('127.0.0.1',8088))
#
# while True:
#     msg=input('==>:').strip()
#     if not msg: continue
#     ss.send(msg.encode('utf-8'))
#     data=ss.recv(1024)
#     print(data.decode('utf-8'))



from multiprocessing import process
# import time,random
# import os
#
# def task():
#     print('%s %s' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p=Process(target=task)
#     p.start()
#     print(p.pid)  #  这个就是子进程的 id
#     print('zhu',os.getpid(),os.getppid())



####### pool 进程池
# 1、同步
# from  multiprocessing  import  Process,Pool
# import  time,os,random
#
# def work(n):
#     print('子进程开始执行: %s' %(os.getpid()))
#     time.sleep(random.randint(1,2))
#     return n*3
#
# if __name__ == '__main__':
#     p=Pool(2)   # print(os.cpu_count())
#     res_l=[]
#     for i in range(10):
#         res=p.apply(work,args=(i,))
#         print(res)
#         res_l.append(res)
#     for j in res_l:
#         print(j)

# 2、异步
# from  multiprocessing  import  Process,Pool
# import  time,os,random
#
# def work(n):
#     print('子进程开始执行: %s' %(os.getpid()))
#     time.sleep(random.randint(1,2))
#     return n*3
#
# if __name__ == '__main__':
#     p=Pool(2)   # print(os.cpu_count())
#     res_l=[]
#     for i in range(10):
#         res=p.apply_async(work,args=(i,))
#         # print(res.get())    # 如果这个时候打印结果，就会变成同步执行，
#         res_l.append(res)
#
#     # 下面两部一定不能少，且顺序不能乱。
#     p.close()   # 关闭进程池
#     p.join()    # 等待子进程结束
#
#     for j in res_l: # 异步 res_l 拿到的是multiprocessing.pool.ApplyResult 对象
#         print(j.get())
#     print('主')


#######concurrent.futures 进程池
# 同步、异步合一
# from concurrent.futures import  ProcessPoolExecutor,ThreadPoolExecutor,Executor
# import  os,time,random
#
#
# def work(n):
#     print('子进程开始执行: %s' %(os.getpid()))
#     time.sleep(random.randint(1,2))
#     return n*3
#
# if __name__ == '__main__':
#     p=ProcessPoolExecutor(4)  # print(os.cpu_count())
#     res_l=[]
#     for i in range(10):
#         res=p.submit(work,i)
#         res_l.append(res)
#         # res=p.submit(work,i).result()  # 同步的方式提交，凡是立即要看结果的都会变成同步的方式。
#         # print(res)
#         # res_l.append(res)
#     p.shutdown(wait=True)
#     for j in res_l:
#         print(j.result())
#     print('主')


###########守护进程的概念:
# 1、当子进程和主进程的生命周期是一致的时候要把子进程设置为守护进程。
# 2、主进程在执行完最后一行后，主进程执行结束
# 3、主进程在等所有非守护进程执行完毕后才会死掉
# 4、主进程执行结束后守护进程同样也立即执行结束。
# 5、守护进程内不能再子进程。
# from   multiprocessing import  Process
# import  time
#
# def foo():
#     print('foo 开始执行')
#     time.sleep(3)
#     print('foo 执行完毕')
#
# def task():
#     print('task 开始执行')
#     time.sleep(3)
#     print('task执行结束')
#     # s=Process(target=foo)
#     # s.start()
#
#
# if __name__ == '__main__':
#     p1=Process(target=task)
#     p2=Process(target=foo)
#     p1.daemon=True
#     p1.start()
#     p2.start()
#     # p.join()  # 守护进程和 join 这个函数没有太大关系，两个不是一类东西
#     print('这是主进程')
#


######进程同步问题（锁）
# # 1、什么是共享，用文件系统演示
# from  multiprocessing import Process,Lock
#
# import  os,time
#
#
# def work(lock):
#     lock.acquire()
#     print('%s 在运行'%(os.getpid()))
#     time.sleep(2)
#     print('%s is done' %(os.getpid()))
#     lock.release()
# if __name__ == '__main__':
#     lock=Lock()
#     for i in range(4):
#         p=Process(target=work,args=(lock,))   # lock 一定要传给子进程，因为只能有一把锁，所有的子进程都必须共享一把锁。
#                                              # 这把锁一定要在父进程提前造好。然后传给子进程。
#         p.start()

# IPC通信实现方式：队列、管道。
#####队列：
# 队列有两种行是：一是普通队列。二是线程安全队列。

# 普通队里的实现方式：
# from queue import Queue
# q=Queue(3)
# print(q.empty())
# print(q.qsize())
# q.put('a')
# q.put_nowait('b')
# q.put('c')
# print(q.full())
# print(q.get())
# print(q.full())




# import queue
# import time
# from multiprocessing import Process
#
# def proc1(q):
#     while True:
#         val=q.get()
#         print('proc1==>',val)
# def proc2(q):
#     while True:
#         val=q.get()
#         print('proc2==>',val)
#
# if __name__ == '__main__':
#     q=queue.Queue(10)
#
#
#     for i in range(10):
#         q.put(i)
#     p1=Process(target=proc1,args=(q,))
#     p2=Process(target=proc2,args=(q,))
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()


###### 上下文队列
# from  multiprocessing import Process,Queue
# # 队列实际上使用管道+锁实现的
# q=Queue(3)
#
# q.put('a')
# q.put(1)
# q.put('b')
# # q.put     #超过队列长度会处于等待状态
# # q.put_nowait('c')  # 直接报错
#
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())  # 超过队列长度会处于等待状态
# print(q.get_nowait())  # 直接报错
#


# from multiprocessing import Process,Queue
# def func(q):
#     q.put([42,None,"hello"])    #把一个列表放入一个队列中
#
# if __name__=="__main__":
#     q1=Queue()        #定义一个队列
#     p1=Process(target=func,args=(q1,))      #实例化一个进程
#     p1.start()  #启动进程
#     print(q1.get())     #从队列中取出一个项目，并打印
#     p1.join()   #阻塞进程








###管道：

# from multiprocessing import Queue,Process,Pipe
# def proc1(pipe):
#     pipe.send('hello')
#     print('proc1:',pipe.recv())
#
# def proc2(pipe):
#     print('proc2:',pipe.recv())
#     pipe.send('too')
#
# if __name__ == '__main__':
#     p=Pipe()
#     p1=Process(target=proc1,args=(p[0],))
#     p2=Process(target=proc2,args=(p[1],))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()


###进程的内训空间是独立的
# from time import sleep,ctime
# from multiprocessing import Process
#
# i=100
# def proc1():
#     global i
#     count=1
#     while True:
#         print ('proc1 >>',i)
#         i=i+2
#         sleep(1)
#         if count==5:
#             break
#         count=count+1
#
# def proc2():
#     global i
#     count=1
#     while True:
#         print ('proc2 >>>>>>>>',i)
#         i=i-3
#         sleep(1)
#         if count==5:
#             break
#         count=count+1
#
# print ("start")
# p1=Process(target=proc1)
# p2=Process(target=proc2)
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# print ("end")


##### 共享数据的方式
# from multiprocessing import Manager, Process, Lock
#
# def work(d,lock):
#     with lock:
#         print('count is: %s', d['count'])
#         d['count'] -= 1
#
#
# if __name__ == '__main__':
#     lock=Lock()
#     with Manager() as m:
#         dic = m.dict({'count': 10})
#         p_l = []
#         for i in range(10):
#             p = Process(target=work,args=(dic,lock))
#             p_l.append(p)
#             p.start()
#         for p in p_l:
#             p.join()
#         print(dic)




# from multiprocessing import Process,Pipe
# def fun(conn):
#     conn.send(['a',2])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn,child_conn=Pipe()
#     p1=Process(target=fun,args=(child_conn,))
#     p1.start()
#     print(parent_conn.recv())
#     p1.join()
#
#



#########生产者、消费者模型
#
# from multiprocessing import Process, Queue, JoinableQueue
# import time
# import random
#
#
# def produer(name, food, q):
#     for i in range(3):
#         res = '%s %s' % (food, i)
#         time.sleep(random.randint(1, 3))
#         q.put(res)
#         print('%s 生产了%s' % (name, food))
#
#
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         if res is None: break
#         time.sleep(random.randint(1, 3))
#         print('%s 吃了 %s' %(name, res))
#         q.task_done()
#
# if __name__ == '__main__':
#     q = JoinableQueue()
#     p1 = Process(target=produer, args=('elax', '土', q))
#     p2 = Process(target=produer, args=('egon', '苹果', q))
#     p3 = Process(target=produer, args=('elax', '香蕉', q))
#
#     c1 = Process(target=consumer, args=('1', q))
#     c2 = Process(target=consumer, args=('2', q))
#     c3 = Process(target=consumer, args=('3', q))
#     c1.daemon = True
#     c2.daemon = True
#     c3.daemon = True
#
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     c1.start()
#     c2.start()
#     c3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     q.join()
#     print('主')


#######线程的概念

# 开线程的两种方法：
# from threading import Thread, Lock
from multiprocessing import process
import os
#
# n = 100
#
#
# def task(name):
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.1)
#     n = temp - 1
#     lock.release()

# 沙面这这种写法和下面这种写法的区别，线程的时候，所有的线程共享进程的数据空间
# n-=1


# if __name__ == '__main__':
#     t_l=[]
#     lock=Lock()
#     for i in range(100):
#         t=Thread(target=task,args=('egon',))
#         t_l.append(t)
#         t.start()
#     for l in t_l:
#         l.join()
#     print('zhu',n)



# from threading import Thread
# class task(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         time.sleep(2)
#         print('%s speaking' %self.name)
#
# if __name__ == '__main__':
#     t=task('egon')
#     t.start()
#     print('zhu')


# from threading import Thread
# import time
#
# def my_counter():
#     i = 0
#     for _ in range(100000000):
#         i = i + 1
#     return True
#
# def main():
#     thread_array = {}
#     start_time = time.time()
#     for tid in range(2):
#         t = Thread(target=my_counter)
#         t.start()
#         t.join()
#     end_time = time.time()
#     print("Total time: {}".format(end_time - start_time))
#
# if __name__ == '__main__':
#     main()


# 死锁雨递归锁
# from threading import Thread,Lock
# import time
# class Mythread(Thread):
#     def run(self):
#         global num
#         time.sleep(3)
#
#         if mutex.acquire(1):
#             num += 1
#             msg = self.name + 'se num to' + str(num)
#             print(msg)
#             mutex.acquire()
#             mutex.release()
#             mutex.release()
# num = 0
# mutex = Lock()
# def test():
#     for i in range(5):
#         t = Mythread()
#         t.start()
#
# if __name__ == '__main__':
#     test()




# import threading
#
# lock = threading.RLock()
#
# ret = lock.acquire()
# print(ret)
# ret = lock.acquire(timeout=3)
# print(ret)
# ret = lock.acquire(True)
# print(ret)
# ret = lock.acquire(False)
# print(ret)
#
# lock.release()
# lock.release()
# lock.release()
# lock.release()



###信号量机制
# 信号量和进程池的区别：
# 使用信号量首先所有的线程是都造出来，只是限制执行，
# from threading import Thread,Semaphore,current_thread
# import threading
# import time
#
#
# def func():
#     if sm.acquire():
#         print('%s get sm' %threading.current_thread().getName())
#         time.sleep(3)
#         sm.release()
# if __name__ == '__main__':
#     sm=Semaphore(5)
#     for i in range(30):
#         t=Thread(target=func)
#         t.start()

#### 事件
# from threading import Thread,Event
# import threading
# import time,random
# def conn_mysql():
#     count=1
#     while not event.is_set():
#         if count > 3:
#             raise TimeoutError('链接超时')
#         print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
#         event.wait(0.5)
#         count+=1
#     print('<%s>链接成功' %threading.current_thread().getName())
#
#
# def check_mysql():
#     print('\033[45m[%s]正在检查mysql\033[0m' %threading.current_thread().getName())
#     time.sleep(random.randint(2,4))
#     event.set()
#
#
# if __name__ == '__main__':
#     event=Event()
#     conn1=Thread(target=conn_mysql)
#     conn2=Thread(target=conn_mysql)
#     check=Thread(target=check_mysql)
#
#     conn1.start()
#     conn2.start()
#     check.start()


# import threading, time
# import random
#
# def light():
#     if not event.isSet():
#         event.set()  # wait就不阻塞 #绿灯状态
#     count = 0
#     i = 0
#     while True:
#         if count < 10:
#             print("---green light on ---")
#         elif count < 13:
#             print("---yellow light on ---")
#         elif count < 20:
#             if event.isSet():
#                 event.clear()
#             print("---red light on ---")
#         else:
#             count = 0
#             event.set()  # 打开绿灯
#         time.sleep(1)
#         count += 1
#         i += 1
#         if (i > 20):
#             break
#
# def car(n):
#     i = 0
#     while 1:
#         time.sleep(random.randrange(3))
#         if event.isSet():  # 如果是绿灯
#             print("car [%s] is running.." % n)
#         else:
#             print("car [%s] is waiting for the red light.." % n)
#         if (i > 10):
#             break
#         else:
#             i += 1
#
# if __name__ == '__main__':
#     event = threading.Event()
#     Light = threading.Thread(target=light)
#     Light.start()
#     for i in range(3):
#         t = threading.Thread(target=car, args=(i,))
#         t.start()
#





### 定时器
# from threading import Timer
# def hello():
#     print('hello world')
#
# t=Timer(5,hello)
# t.start()



# from threading import Timer
# import random,time
#
# class Code:
#     def __init__(self):
#         self.make_cache()
#
#     def make_cache(self,interval=5):
#         self.cache=self.make_code()
#         print(self.cache)
#         self.t=Timer(interval,self.make_cache)
#         self.t.start()
#
#     def make_code(self,n=4):
#         res=''
#         for i in range(n):
#             s1=str(random.randint(0,9))
#             s2=chr(random.randint(65,90))
#             res+=random.choice([s1,s2])
#         return res
#
#     def check(self):
#         while True:
#             inp=input('>>: ').strip()
#             if inp.upper() ==  self.cache:
#                 print('验证成功',end='\n')
#                 self.t.cancel()
#                 break
#
#
# if __name__ == '__main__':
#     obj=Code()
#     obj.check()


####  线程 QUEUE
# import  queue
#
# q=queue.Queue()
#
# q.put('1')
# q.put('2')
# q.put('3')
#
# print(q.get())
# print(q.get())
# print(q.get())
#
#
# q=queue.LifoQueue()
# q.put('1')
# q.put('2')
# q.put('3')
#
# print(q.get())
# print(q.get())
# print(q.get())
#
#
# q=queue.PriorityQueue()
#
# q.put(10,'a')
# q.put(20,'b')
# q.put(30,'c')
#
# print(q.get())
# print(q.get())
# print(q.get())



#########paramiko模块的使用
# import  paramiko
#
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='172.26.31.231',port=22,username='root',password='iCourt12345')
# stdin,stdout,stderr= ssh.exec_command('ls -la')
# result=stdout.read()
# print(result.decode('utf-8'))
# ssh.close()


# 封装 transport

# import  paramiko
#
# transport=paramiko.Transport('172.26.31.231',22)
# transport.connect(username='root',password='iCourt12345')
# ssh=paramiko.SSHClient()
# ssh._transport=transport
# stdin, stdout, stderr = ssh.exec_command('ls -la')
# print(stdout.read().decode('utf-8'))
# transport.close()

### 实现 ftp 的功能
# import  paramiko
# transport=paramiko.Transport('172.26.31.231',22)
# transport.connect(username='root',password='iCourt12345')
# sftp=paramiko.SFTPClient.from_transport(transport)
#
# sftp.put('/Users/FLS/test/zxh2.log','/tmp/zxh2.log')
#
#
# sftp.get('/root/heartbeat-6.3.2-x86_64.rpm','/Users/FLS/test/heartbeat-6.3.2-x86_64.rpm')
#
# transport.close()



# !/usr/bin/python3
# _*_ coding: UTF-8 _*_





##### python 数据库操作：


# import   pymysql
#
#
# db =pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='xinlin',db='poll',charset='utf8')
#
# cursor=db.cursor()
#
#
# sql1='''
#     create table IF not exists user(
#     userid int(11) PRIMARY KEY ,
#     username VARCHAR(20)
#     )
# '''
#
# sql2='''
#     select * from user
# '''

# try:
#     cursor.execute(sql1)
#     for i in range(0,10):
#         cursor.execute("insert into USER (userid,username) VALUES ('%d','%s')" %(int(i),'name'+str(i)))
#     db.commit()
# except:
#     db.rollback()




# cursor.execute(sql2)
#
# res=cursor.fetchone()
# print(res)
# res=cursor.fetchone()
# print(res)
# res=cursor.fetchmany(5)
# print(res)
# # res=cursor.fetchall()
# # print(res)
#
# num=cursor.rowcount
# print(num
#
# print(cursor.rownumber)

#
# cursor.execute(sql2)
#
# res=cursor.fetchall()
# for row in res:
#     print('nameid=%s,namename=%s' %row)

# try:
#
#     cursor.execute('insert into user(userid,username) values(11,"name11")')
#     cursor.execute('update user set username="name91" where userid=9')
#     cursor.execute('delete from user where userid=3')
#     db.commit()
#
# except Exception as e:
#
#     print(e)
#     db.rollback()

#
# cursor.execute(sql2)
# res=cursor.fetchall()
# print(res)
#
#
# cursor.close()
#
# db.close()


### 银行转账的例子：

import pymysql
import sys


# class transferMoney():
#     def __init__(self, conn):
#         self.conn = conn
#
#     def check_id(self, soruce_id):
#         cursor=self.conn.cursor()
#         try:
#             sql="select * from tr_money where acctid=%s"  %soruce_id
#             cursor.excute(sql)
#             print('check acctid sql'+sql)
#             result=cursor.fetchall()
#             if result !=1:
#                 raise Exception('账号不存在%s' %soruce_id)
#         finally:
#             cursor.close()
#
#     def check_money(self,source_id,money):
#         cursor=self.conn.cursor()
#         try:
#             sql="select * from tr_money where acctid=%s and money>%s" %(source_id,money)
#             cursor.excute(sql)
#             print('check acctid sql'+sql)
#             result=cursor.fetchall()
#             if result !=1:
#                 raise Exception('账户余额不足%s' %source_id)
#         finally:
#             cursor.close()

# https://www.jb51.net/article/124705.htm







# from django import templates
# t=templates.Template('my name is {{name}}')
# c=templates.Context({'name':'fls'})
# print(t.render(c))

class CLanguage() :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    def __init__(self,name,add):
        #下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name,"网址为：",add)
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)

