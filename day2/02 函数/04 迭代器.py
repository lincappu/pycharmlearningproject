# !/usr/bin/env python3
# _*_coding _*_

# 什么是迭代器：
# 迭代是一个重复的过程，每次结果都是上次的结果来的。
# 针对没有索引的数据类型，必须有一种不依赖索引的取值方式，

# 可迭代对象：只要对象有__iter__方法就是可迭代对象。
# 目前所学的所有类型都是可迭代对象。
# 迭代器对象：既要有__iter__对象，也要有__next__方法。
# 可迭代度对象
# 'hello'.__iter__()  'hello'.__
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

# 对于文件来说，就不用那部分的转换。
#
# import  os
# with open('test.txt','r',encoding='utf-8') as f:
#     print(f.__next__(),end='')
#     print(f.__next__(),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')


# dic = {'a': 1, 'b': 2, 'c': 3}
# dic_iter = dic.__iter__()
# while True:
#     try:
#         print(next(dic_iter))
#     except StopIteration:
#         break

# 迭代器的作用就就不依赖索引循环取值，利用数据类型本身的方法，并且是数据类型本身的属性。这个屏蔽了数据类型。
# 所有的取值方法都是一样的

# for 循环会将自动将可迭代对象转换为迭代器对象。
# l=[1,2,3,4,5,6,7,8,9] #
# for i in l:
#     print(i)



# 迭代器的优点：
# 1.提供一种统一的取值方式，
# 2.更加节省内存空间。 next的时候才会去一次值。
#
# 缺点：
# 一次取值，只能往后不能往前取。且没法取特定的值。


# 如果有个很大的对象，最好变成一个迭代器对象，这样可以以一次一次的取值。


# 判断是不是可迭代对象：
# from collections import  Iterable,Iterator
# print(isinstance('hellp',Iterable))
# print(isinstance('hellp',Iterator))

# 迭代器的应用形式：生成器。
# 生成器就是迭代器。


# 只要函数内部出现 yield 关键字。那该么在调用该函数，将不会立即执行该函数，会得到一个结果，该结果就是生成器对象。

#
# def func():
#     print('a')
#     yield 1
#     print('b')
#     yield 2
#     print('c')
#     yield 3
#
#
# f=func()
# print(f)
# g=next(f)
# print(g)
# print(f.__next__())

# yield功能
# 1.提供一种自定义迭代器的方法。
# 2.可以返回多次值。
# 3.将函数暂停住，将 yield 的值作为返回值返回回来。
# 流程：是先停住，执行下面的代码，又到 yield 后将 yield 后面的值职位返回值返回

# 自定义的 range 功能，
# def my_range(start,stop,step):
#     while start < stop:
#         yield start
#         start+=step
#
#
# for i in my_range(1,1000,2):
#     print(i)


# 实现tailf 的功能：
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
# g=grep('404',tail('access.log'))
# for line in g:
#     print(line)





# yield 的表达式形式，多次往函数里面传值
# def eater(name):
#     food_list=[]
#     print('%s 开始吃' %(name))
#     while True:
#         food=yield food_list   # 赋值和返回值。
#         print('%s eat %s ' %(name,food))
#         food_list.append(food)
#
#
# g=eater('alex') #  函数并没有执行。
#
# next(g)==g.send(None)
#
# try:
#     g.send(None)
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
#





















