# !/usr/bin/env python3
# _*_conding:utf-8_*_

#常规的使用
import sys
sys.path.append(r'/Users/FLS/Downloads/pycharmlearningproject/practice/file')
# print(sys.path)









# l=[1,2,[3,4]]
# print(type(l[0]))
# print(type(l[1]))
# print(type(l[2]))








# 1.函数作为返回值返回
# def lazy_sum(*args):
#     def sum():
#         x=0
#         for n in args:
#             x=x+n
#         return x
#     return sum
#
# lazy_sum(1,2,3,4,5,6,7,8,9) #这时候lazy_sum 并没有执行，而是返回一个指向求和的函数的函数名sum 的内存地址。
# f=lazy_sum(1,2,3,4,5,6,7,8,9)
# print(type(f))
# print(f())  # 调用f()函数，才真正调用了 sum 函数进行求和，
# 这其实就是闭包。
#
#
# 返回一个函数列表：
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
# 输出：
# 9
# 9
# 9
# 执行过程：
# 当i=1, 执行for循环， 结果返回函数f的函数地址，存在列表fs中的第一个位置上。
# 当i=2, 由于fs列表中第一个元素所指的函数中的i是count函数的局部变量，i也指向了2；然后执行for循环， 结果返回函数f的函数地址，存在列表fs中的第二个位置上。
# 当i=3, 同理，在fs列表第一个和第二个元素所指的函数中的i变量指向了3； 然后执行for循环， 结果返回函数f的函数地址，存在列表fs中的第三个位置上。
# 所以在调用f1()的时候,函数中的i是指向3的：
#   f1():
#      return 3*3
# 同理f2(), f3()结果都为9
# 闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。即包在里面的函数（本例为f()），不要引用外部函数(本例为count())的任何循环变量
#
# 如果一定要引入循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
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
# 结果就是预期的1,4,9.
# 当i=1时，f(1)即让j指向1，
# 当i=2时，f(2)即让j指向2，此时j不是count的局部变量，不会影响到i=1是f(1)中j的指向。即函数f的参数绑定循环变量当前的值, 而不是循环变量本身。









# 单线除的结果都是 float 类型：
# print(10/3)
# print(12/2)
# print(2/1)
# 双线除的结果都是商：
# print(2//1)
# print(10//3)









# if/else、if/elif/else结构执行过程。
#
# if  :
# if :
# else:
# 这种结构后面的 if 和 else 组成一对，而不是它们三个组成一队。
# if:
# elif:
# else:
# 这种结构才是它们组成一队。
# 总结：有多余三种情况的，一定要写 eiif。









# map 函数：
# def f(x):
#     return x*x
#
# x=map(f,[1,2,3,4])
# for i  in x:
#     print(i)
#
#
# l=map(lambda x:x%2,range(7))
# for i in l:
#     print(i)

# l2=map(lambda x,y:x**y,[1,2,3],[1,2,3])
# for i  in l2:
#     print(i)
#
# l3=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,3])
# for i in l3:
#     print(i)
#
# python3中可以处理类表长度不一致的情况，但无法处理类型不一致的情况，
# l4=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2])
# for i in l4:
#     print(i)
#
# l4=map(lambda x,y:(x**y,x+y),[1,2,3],[1,2,'a'])
# for i in l4:
#     print(i)
#
# 特殊用法，做类型抓换：
# l=map(int,'1234')
# for i in l:
#     print(type(i))
#     print(i)

# 如果函数是 None，自动假定一个‘identity’函数
# l=[1,2,3]
# x=map(None,l)
# print(x)
# 但这时其实是无法调用的








# sorted函数
# 基本形式：
# sorted(iterable，key=None,reverse=False)
# iterable.sort(key[, reverse]])
# 基础用法：
# a=sorted('abfrtffsdflkjfklsdjfg')
# print(sorted(a))
#
# x=[1,2,5,4,3,4,6,7,5]
# print(sorted(x,reverse=True))

# x=[1,2,5,4,3,4,6,7,5]
# y=x[:]
# y.sort()
# print(y)

# 有 key 的情况：
# a = ['a','b','d','c','B','A']
# print(a)
# print(sorted(a)) # 默认是按 ascii 码进行排序
# print(sorted(a,key=str.lower))   #先将字符转换为小写后在比较，

# 例子：
# students = [('牛牛', 'A', 15), ('道长', 'B', 12), ('大师兄','B', 10)]
# x=sorted(students,key=lambda x:x[2])
# print(x)

# 一个字符串排序，排序规则：小写<大写<奇数<偶数,
# 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。
# 先看一下Boolean value 的排序：
# print(sorted([True,Flase]))===>结果[False,True]
# Boolean 的排序会将 False 排在前，True排在后

# s='9a13C85c7B24A6b' #正确的顺序应该为：abcABC135792468

# lis=sorted(s,key=lambda x:(x.isdigit(),))
# l2=(lambda x:(x.isdigit(),x.isdigit() and  int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
# print(l('9a13C85c7B24A6b'))
# 体会一下这个过程，因为 bool 类型是反着的，所以写的时候是 True在前面，

# l2=sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and  int(x)%2==0,x.isalpha() and x.isupper(),x.isalpha() and x.lower()))
# print(''.join(l2))



# 正则表达式：
# import re
# s='#sdfg45$@sdfg45$%dgf&sdfg46&hs[][,.564~kj!k122h~j`k!n1j'
# l=re.split(r'\w',s)
# print(l)
# l=re.split(r'\W',s)
# print(l)



# return函数的用法：
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         print()
#         gcd(b,a%b)
#
# print(gcd(25,10))

# def func():
#     try:
#         print(98)
#         return ('ok')  # 函数得到了一个返回值
#     finally:  # finally语句块中的语句依然会执行
#         print(98)
#
# res=func()
# print(res)







# enumerate 函数的用法：前面一个是下标，后面一个是元素。
# 普通的 for 循环实现：
# l=['ni','hao','ma']
# for i in range(len(l)):
#     print(i,l[i])


# enumerate函数实现：
# l=['ni','hao','ma']
# for index,item  in  enumerate(l):
#     print(index,item)

# 执行索引值
# l = ["这", "是", "一个", "测试"]
# for index,item in enumerate(l,1):
#     print(index,item)

# 例子：
# count=0
# for index,line in enumerate(filepath,'r'):
#     count+=1






# 列表翻转：
# list=[1,2,3,4,5,6]
# list2=list[::-1]
# print(list2)

# 三个删除操作:
# student = ['Tom', 'Jack', 'Avril']
# res=student.remove('Tom')
# print(res,student)

# s = student.pop()
# print(s)
# print(student)

# student = ['Tom', 'Jack', 'Avril']
# del student[1]
# print(student)









# 名称空间：

# 一、 查找顺序：
# 1.本函数中查找。
# 2.父函数中查找
# 3.模块命名空间---就是全局命名空间
# 4.内置名称空间

# 例子：
# info='address:'
# def father(country):
#     def son(area):
#         city='shanghai'
#         print(info +' '+ country +' '+ city+' '+ area)
#     city='beijing'
#     son('pudong')
#
# father('china')

# python 的一个特殊之处就在与赋值操作总是在最里层的作用域，赋值不会复制数据：
# 1.只是取值：
# i=1
# def func():
#     print(i)
# func()
# print(i)
# 2.赋值：
# i=1
# def func1():
#     i+=1
#     print(i)
#
# func1()
# print(i)

# 3.申明全局变量：global
# i=1
# def func2():
#     global i
#     i+=1
#     print(i)
#
# func2()
# print(i)
# 结论：在函数内部进行读值与赋值是不同的：
# 读值：变量按照查找顺序查找值，直到站到为止，找不到就报错，
# 赋值:赋值操作都是发生在函数的最内层空间，就是局部作用域，赋值只是将命名绑定到对象，这时候其实是看不到函数的外部变量的，
# 只有加上 global 才能找到函数外面的变量。但读取就不需要。

# 三、命名空间的访问：
# import copy
#
# from copy import  deepcopy
#
# g=10
#
# def foo(i,str):
#     x=10
#     print(locals())
#
# foo(1,'foo')
#
#
# if __name__ == '__main__':
#     print('这时全局变量：')
#     dicglobal=globals()
#     print(dicglobal)

'''
输出：
{'__name__': '__main__',
 '__doc__': None,
 '__package__': None,
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x109a9d668>,
 '__spec__': None,
'__annotations__': {},
'__builtins__': <module 'builtins' (built-in)>,
'__file__': '/Users/FLS/Downloads/pycharmlearningproject/practice.py',
'__cached__': None, 's': '9a13C85c7B24A6b',
'copy': <module 'copy' from '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/copy.py'>,
'deepcopy': <function deepcopy at 0x109bf4840>, 'g': 10, 'foo': <function foo at 0x109a27f28>,
'dicglobal': {...}}
总结：
1.模块的名称空间不仅包括模块级别的变量和常量，还包括所有的在模块中定义的函数和类，还有任何导入的东西
2.内置函数同样导入到了模块空间中
3.使用import 来导入，模块自身被导入，但是它保持自己的名称空间，这就是为什么要用模块名.函数的方法来调用它
使用 from import 来导入，实际上是将另一个模块中指定的函数和属性导入自己的名称空间，也就是直接不加来源就可以引用，
'''

# 四、locals是只读的，但 globas 不是
# def func1():
#     x=123456
#     x=543
#     print(locals())
#     locals()['x']=123
#     print(locals())
#     print(x)
#
#
# func1()
# print('')
# y=654321
# globals()['y']=6789
# print(globals())
# print(y)

# 五、nolocal 在函数外层，但不是全局
# def f1():
#     x=1
#     def f2():
#         nonlocal  x
#         x+=1
#         print(x)
#
#     print(x)
#     return f2
#
#
# # f=f1()
# # f()
#
# f1()()


# 经典的例子：
# 1.经典的例子
# def scope_test():
#     def do_local():
#         spam='local spam'
#     def do_nolocal():
#         nonlocal spam
#         spam='nonlocal spam'
#     def do_global():
#         global  spam
#         spam='global spam'
#
#     spam='test spam'
#
#     do_local()
#     print(spam)
#
#     do_nolocal()
#     print(spam)
#
#     do_global()
#     print(spam)
#
# scope_test()
# print(spam)

# 2.函数f1定义的 global 变量只能在函数 f2内引用，但是要在f2内修改，必须也要在 f2中 global 这个变量.
# def f1():
#     global x
#     x=10
#     def f2():
#         # print(x)   # 如果下面有global 或者 nonlocal 不能再前面进行 print 这是其实就相当于先引用后定义
#         global x  # 这个地方不能是 nonlocal 因为 f1其实没有 x 这个变量。
#         x+=10
#         print(x)
#     f2()
#
# f1()









# python的 json 模块：序列化模块
# 最简单的写法：
import  json
# dic={'name':'egon','password':'123','age':19}
# res=json.dumps(dic)
# print(res,type(res))

# resto=json.loads(res)
# print(resto,type(resto))
# print(resto['name'])

# json.dump(dic,open('file/user.json','w',encoding='utf-8'),indent=5)
# res=json.load(open('file/user.json','r',encoding='utf-8'))
# print(res,type(res))



# 详解：
# json 就是 js对象标记，轻量级的数据交换格式，json 就是python 里面的字典格式，
# 提供了四个方法：dump dumps load loads，  pickle 也是提供了这四个方法
# 1.dump dumps 序列化方法：序列化：其实就是将数据写到文件中。
# dump 是操作文件的，dumps 是序列化字符串的。
import json

# x='nihao'
# print(x,type(x))
# res=json.dumps(x)
# print(x,type(x))  # 这个 str 不是python 的 str 而是，json 的 str，注意分清。

#写入文件的时候必须是 str 类型，不能是其他类型。
# Python            | JSON          |
# +===================+===============+
# | dict              | object        |
# +-------------------+---------------+
# | list, tuple       | array         |
# +-------------------+---------------+
# | str               | string        |
# +-------------------+---------------+
# | int, float        | number        |
# +-------------------+---------------+
# | True              | true          |
# +-------------------+---------------+
# | False             | false         |
# +-------------------+---------------+
# | None              | null




# pythonde repr() str()函数：
# python 有办法将任意值转化为字符串，将他传入 str（）repr（）函数即可。
'''
函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式（如果没有等价的
语法，则会发生SyntaxError 异常） 某对象没有适于人阅读的解释形式的话， str() 会返回与repr()
等同的值。很多类型，诸如数值或链表、字典这样的结构，针对各函数都有着统一的解读方式。字符串和浮点数，有着独特的解读方式。

str 其实就相当于 python 的 print
repr 就相当于  python 的变量本身，始终在外层加上个引号。
'''
# s='hello world'
# print(str(s))
# print(repr(s))
#
# print(str(5/5))
# print(str(5.0/3))
# print(repr(5/5))
# print(repr(5.0/3))

# x=10*2.34
# y=200*30
# print('x: '+repr(x)+' and y: '+repr(y))

# 和 eval的配合使用：
# obj='nihao'
# print(obj==eval(repr(obj)))  #True
# print(obj==eval(str(obj)))   # false 相当于：eval(obj)，这时就变了一个变量，而不是一个字符串
# 所以 repr 比较适合和 eval 配合使用，而 str 则不行，

# 可变类型：
# print(str('[1,2,3]'))  # 这时候这个就不变成了列表类型
# print(repr('[1,2,3]'))  # 这个还是字符串类型。

# repr 和``功能其实是一样的：
# tmp=100
# print('nihao'+repr(tmp))
# print('nihao'+`tmp`)   # python3.6 已经不支持``了，使用 repr 代替。

# a='nihao'
# print(len(str(a)))
# print(len(repr(a)))










# urllib.request的 urlopen 函数
# 用法  urlopen(url, data=None, proxies=None)  返回的是 httpresponse 对象。
# 参数 url 表示远程数据的路径，一般是 http 或者 ftp 路径。
# 参数 data 表示以 get 或者 post 方式提交到 url 的数据。
# 参数 proxies 表示用于代理的设置。
# urlopen 返回一个类文件对象，它提供了如下方法：
# read() , readline() , readlines()，fileno()和close()： 这些方法的使用与文件对象完全一样。
# info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息。
# getcode()：返回Http状态码，如果是http请求，200表示请求成功完成;404表示网址未找到。
# geturl()：返回请求的url地址。

# import urllib.request
# content=urllib.request.urlopen(r'http://www.baidu.com ')
# print(content.info())
# print(content.getcode())
# print(content.geturl())
# print(content.read().decode('utf-8'))
# content.close()











# pprint 模块的使用：
# pprint模块 提供了打印出任何python数据结构类和方法。
# 模块方法：
# 1.class pprint.PrettyPrinter(indent=1,width=80,depth=None, stream=None)
#    创建一个PrettyPrinter对象
#     indent --- 缩进，width --- 一行最大宽度，
#     depth --- 打印的深度，这个主要是针对一些可递归的对象，如果超出指定depth，其余的用"..."代替。
#                  eg: a=[1,2,[3,4,],5]  a的深度就是2; b=[1,2,[3,4,[5,6]],7,8] b的深度就是3
#     stream ---指输出流对象，如果stream=None，那么输出流对象默认是sys.stdout
# 2.pprint.pformat(object,indent=1,width=80, depth=None)
#    返回格式化的对象字符串
# 3.pprint.pprint(object,stream=None,indent=1, width=80, depth=None)
#   输出格式的对象字符串到指定的stream,最后以换行符结束。
# 4.pprint.isreadable(object)
#    判断对象object的字符串对象是否可读
# 5.pprint.isrecursive(object)
#    判断对象是否需要递归的表示
#    eg: pprint.isrecursive(a)  --->False
#         pprint.isrecursive([1,2,3])-->True
# 6.pprint.saferepr(object)
#    返回一个对象字符串，对象中的子对象如果是可递归的，都被替换成<Recursionontypename withid=number>.这种形式。

import  pprint

# data = [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
#         (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
#              'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'
#              }),
#         ]
# 1.美化打印
# pprint.pprint(data)
# 输出：
# [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
#  (2,
#   {'e': 'E',  # python 支持
#    'f': 'F',
#    'g': 'G',
#    'h': 'H',
#    'i': 'I',
#    'j': 'J',
#    'k': 'K',
#    'l': 'L'})]
# pprint()格式化一个对象，并把它写至一个数据流，这个数据流作为参数传入（或者是默认的sys.stdout）
# 注意为什么第二个字典中会显示一竖列，因为pprint打印支持8个对象以上的竖列打印

# 2.格式化：pformat
# pdata=pprint.pformat(data)
# print(pdata)
# 其实就是讲数据格式化但是不输出。

# 3.限制深度:
# pprint.pprint(data,depth=2)

# 4.限制宽度：格式化文件的默认输出宽度是80列
# pprint.pprint(data,width=5)
# pprint.pprint(data,width=200)

# 练习：
# import sys
# print(sys.path)
# pprint.pprint(sys.path,indent=4)












# logging 模块：

# 1.简单打印日志信息到终端：
# import  logging

# print(logging.debug('debug'))
# print(logging.info('info'))
# print(logging.warning('warning'))
# print(logging.error('error'))
# print(logging.critical('critical'))
# 两个问题需要注意：
# 1.默认的 logger，root
# 2.默认的级别，warning


# 2.灵活配置日志级别、内容、位置：
# import  logging
#
# logging.basicConfig(
#     format='%(asctime)s %(name)s %(module)s [%(filename)s:%(lineno)s]  %(levelname)s ：%(message)s',
#     filename='file/access.log',
#     filemode='a',
#     datefmt='%Y/%m/%d% %H:%m:%S',
#     level=logging.DEBUG
# )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 3.logging 对象：logger filter handler formatter
import  logging
#
# logger=logging.getLogger()
#
# logger1=logging.getLogger('mylogger')
# logger1.setLevel(logging.DEBUG)
# logger1和 logger2绑定的是同一个logger，name才是唯一的，
# logger2=logging.getLogger('mylogger')
# logger2.setLevel(logging.INFO)
#
# logger3=logging.getLogger('mylogger.child1')
# logger3.setLevel(logging.DEBUG)
#
# logger4=logging.getLogger('mylogger.child1.child2')
# logger4.setLevel(logging.DEBUG)

# logger5=logging.getLogger('mylogger.child1.child2.child3')
# logger5.setLevel(logging.DEBUG)
#
#
# h1=logging.StreamHandler()
# h2=logging.FileHandler('file/test.logs')
#
#
# logger.addHandler(h1)
# logger.addHandler(h2)
#
#
# logger1.addHandler(h1)
# logger1.addHandler(h2)
#
# logger2.addHandler(h1)
# logger2.addHandler(h2)
#
# logger3.addHandler(h1)
# logger3.addHandler(h2)
#
# logger4.addHandler(h1)
# logger4.addHandler(h2)
#
# logger5.addHandler(h1)
# logger5.addHandler(h2)
#
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
#python默认的 logger，注意级别。


# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')
# 这两个是其实显示的结果是一样的。
# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')
#
#
# logger3.debug('logger3 debug message')
# logger3.info('logger3 info message')
# logger3.warning('logger3 warning message')
# logger3.error('logger3 error message')
# logger3.critical('logger3 critical message')
# # 首先本身有一遍，然后发给 child1，然后发给父亲 mylogger，这个有两遍
#
#
# logger4.debug('logger4 debug message')
# logger4.info('logger4 info message')
# logger4.warning('logger4 warning message')
# logger4.error('logger4 error message')
# logger4.critical('logger4 critical message')
# # 四遍
#
#
# logger5.debug('logger5 debug message')
# logger5.info('logger5 info message')
# logger5.warning('logger5 warning message')
# logger5.error('logger5 error message')
# logger5.critical('logger5 critical message')
# # 五遍

# 第二个例子：完整的例子：
# import  logging
# '''
# critical 50
# error 40
# warning 30
# info 20
# debug 10
#        0
# '''

# 1.生成 logger 对象，
# logger=logging.getLogger(__file__)

# 2.filter对象，这个基本不用

# 3.创建handler 对象，接受logger 对象传来的日志，然后打印
# h1=logging.FileHandler('file/t1.log')
# h2=logging.FileHandler('file/t2.log')
# h3=logging.StreamHandler()
#
# 4.创建formatter 对象，控制 handler 的输出格式
# f1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p',)
# f2=logging.Formatter('%(asctime)s :  %(message)s',datefmt='%Y-%m-%d %H:%M:%S %p',)
# f3=logging.Formatter('%(name)s %(message)s',)

# 5.为 handler 绑定 formatter对象
# h1.setFormatter(f1)
# h2.setFormatter(f2)
# h3.setFormatter(f3)

# 6.将 handler 绑定给 logger 对象
# logger.addHandler(h1)
# logger.addHandler(h2)
# logger.addHandler(h3)
# logger.setLevel(logging.DEBUG)

# 测试
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')


# 官网学习：
# import logging

# 1.cli 写法
# logging.warn('watch out')

# 2.简单的配置文件
# logging.basicConfig(
#     filename='file/lianxi.log',
#     filemode='a',
#     level=logging.DEBUG
# )
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# 3.有多个模块在不同的文件中调用同一个 logger
# import  logging
# from pyfile import mylib
#
# def func():
#     logging.basicConfig(
#         filename='file/lianxi.log',
#         filemode='a',
#         level=logging.DEBUG
#     )
#     logging.info('第一个模块')
#     mylib.do_something()
#     logging.error('还是第一个模块')
#
#
#
# if __name__ == '__main__':
#     func()


# 4.多次调用同一个name 的 logger 会产生多个实例，但是引用的通一个 logger 对象，意思就是引用不同的实例名会对这个加载所有的配置。
# 5.级别的继承：如果一个logger 对象的 level 没有显式的定义，他会去找父节点，知道找到 root。


# 6.使用fileconfig（）配置logging 模块：
# import logging
# import  logging.config
#
# logging.config.fileConfig('file/logging.conf')
#
# logger=logging.getLogger('mylogger')
#
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')










