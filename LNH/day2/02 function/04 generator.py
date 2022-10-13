# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 什么是迭代器：
# 迭代是一个重复的过程，每次结果都是基于上次的结果来的，
# 针对没有索引的数据类型，必须有一种不依赖索引的取值方式，

# 可迭代对象：只要对象有__iter__方法就是可迭代对象。
# 目前所学的所有类型都是可迭代对象。数值类型不是
# 迭代器对象：既要有__iter__对象，也要有__next__方法。
# 可迭代度对象
# 'hello'.__iter__()
# [1,2].__iter__()
# (1,2).__iter__()
# {'a':1}.items()
# {1,2,3}.__iter__()
# 迭代器对象：
# open('a.txt','w').__next__()
# 结论：迭代器对象一定是可迭代对象，但是可迭代对象不一定时迭代器对象。

# 这时对于字典
# dic = {'a': 1, 'b': 2, 'c': 3}
# dic_iter = dic.__iter__()  # 通过这种方法把可迭代对象变成了迭代器对象，关键是__next__属性，要取值。
# print(dic is dic_iter)  # False,只有文件这种属性，因为他已经是迭代器对象。
# print(dic_iter.__next__())
# print(next(dic_iter))
# print(next(dic_iter))

# 对于文件来说，就不用那部分的转换。但是为了格式统一，还是有__iter__方法
#
import  os
# with open('test.txt','r',encoding='utf-8') as f:
#     print(f.__next__(),end='')
#     print(f.__next__(),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
# 由此可以看出 f.__iter__ == next(f)

# dic = {'a': 1, 'b': 2, 'c': 3}
# dic_iter = dic.__iter__()
# while True:
#     try:
#         print(next(dic_iter))
#     except StopIteration:
#         break

# 迭代器的作用就就不依赖索引循环取值，利用数据类型本身的方法，这个就屏蔽了数据类型。所有的取值方法都是一样的

# for 循环会将自动将可迭代对象转换为迭代器对象，并且遇到报错自动停止
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)



# 迭代器的优点：
# 1.提供一种统一的取值方式，
# 2.更加节省内存空间。 next的时候才会去一次值，而不是将值一次性全部取出。
#
# 缺点：
# 一次取值，只能往后不能往前取。且没法取特定的值。


# 如果有个很大的对象，最好变成一个迭代器对象，这样可以以一次一次的取值。


# 判断是不是可迭代对象和迭代器
#
# print(isinstance('hellp',Iterable))
# print(isinstance('hellp',Iterator))
# string='hello'
# s=string.__iter__()
# print(isinstance(s,Iterator))






# 迭代器的应用形式：生成器,生成器就是迭代器。

# 只要函数内部出现 yield 关键字。那该么在调用该函数，将不会立即执行该函数，会得到一个结果，该结果就是生成器对象。

# def func():
#     print('a')
#     yield 1
#     print('b')
#     yield 2
#     print('c')
#     yield 3
#
# func()  # 执行函数只是将函数装换为迭代器对象。
# f=func()
# print(f)
# g=next(f)
# print(g)
# print(f.__next__())
#
# yield功能
# 1.提供一种自定义迭代器的方法。把函数做成迭代器的方法。
# 2.可以返回多次值。
# 3.将函数暂停住，将 yield 的值作为返回值返回回来。
# 流程：是先停住，执行下面的代码，又到 yield 后将 yield 后面的值职位返回值返回 可以返回多个值。 对比 return 的功能，return 只能执行一次。

# 自定义的 range 功能，
# def my_range(start,stop,step):
#     while start < stop:
#         yield start
#         start+=step
#
#
# for i in my_range(1,1000,2):
#     print(i)





#  yield 的表达式形式，多次往函数里面传值
# def eater(name):
#     food_list=[]
#     print('%s 开始吃' %(name))
#     while True:
#         food=yield food_list   #  复制是传进来的值， 返回值是 yield 后面的值。
#         print('%s eat %s ' %(name,food))
#         food_list.append(food)


# g=eater('alex') #  函数并没有执行，只是转换为了迭代器对象，
#函数真正开始执行 的时候：
# g.send('石头')   # 在调用 next 之前，如果要 send，则必须 send 一个 Node，效果next(g)==g.send(None)
# next(g)
# print(g.send('1'))


# try:
#     g.send(None)  # 生成器第一次必须 send一个 None.
#     g.send('骨头')
#     print(g.send('shitou'))
#     print(g.send('shitou'))
#     print(g.send('shitou'))
#     g.close()   # 遇见 close 就停止了，下面的就不能 send 了，然后重新初始化，
#     g.send('shitou')
#     g.send('shitou')
#     g.send('shitou')
# except StopIteration:
#     exit(1)



# 代码赏析：循环取值

# 1.用 for 循环实现：
# def func():
#    for i in range(10):
#         print('1')
#         return i


# print(func())
# 这两种方式都可以，但是为了格式统一，有返回值的类型，统一用参数接收
# res=func()
# print(res)
#
# f=func()
# print(type(func))
# print(type(func()))   # 只要是函数加()都是在在运行函数。
# print(type(f))
# print(id(func))
# print(id(func()))
# print(id(f))
# print(f.__next__())
# res=next(f)
# print(res)
#
# 主要的思想：
#     如果用 return 做，由于 return 只能返回一次值，然后就结束了，所以他不可能进行多次取值，也没有所谓的生成器的概念。他返回的是第一个数值



# 2.用生成器实现：
# 通过for 循环来创建生成器，
# l=[i for i in range(10)]
# print(l)

# 通过 yield 关键字来创建生成器：
# def func():
#     for i in range(19):
#         yield i
#
# f=func()   #这个 f就是迭代器对象，和 func 是同一个。然后就可以循环取值。
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(f)
# print(func())
# print(f.__next__())
#


#  yield from   在python3中提供一种可以直接把可迭代对象中的每一个数据作为生成器的结果进行返回
# lst = ['卫龙','老冰棍','北冰洋','牛羊配']
# def func():
#     lst = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
#     yield from lst
# g = func()
# for i in g:
#     print(i)

#  有个小坑,yield from 是将列表中的每一个元素返回,所以 如果写两个yield from 并不会产生交替的效果

# def func():
#     lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
#     lst2 = ['馒头','花卷','豆包','大饼']
#     yield from lst1
#     yield from lst2
# g = func()
# for i in g:
#     print(i)
#

