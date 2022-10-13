# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 1.函数对象的特性：

# 函数是第一类对象:
# 1.函数可以被引用
# def foo():
#     print('form foo')
#
# f=foo  # 而不是 foo（）
# print(f) # 就是内存地址
# f()

# 2.可以做为参数传递
# def wra(x):
#     print(x)
#     x()
#
# wra(foo)

# 3.返回值可以是函数
# def wra():
#     return foo

# f=wra()
# print(f())

# 4.可以作为容器类型的元素
# l=[foo,1,3]
# l[0]()
# 看做作业


# 嵌套函数
# 上面的1和2就是嵌套函数
# 函数的嵌套调用  嵌套定义

# def f1():
#     def f2():
#         def f3():
#             print('f3')
#         f3()
#     f2()
# f1()
# 内部定义的函数只能在内部调用，函数的层级


# 名称空间于作用域:

# 文件级别的名称空间:全局名称空间
# 局部名称空间：函数的内部名称空间，只在函数内部能看见，调用完成后既回收，外部是看不到的
# 内置名称空间：内置的名字与值的绑定关系
# 查找顺序：内部  全局  内置，要看你代码的位置。

# 作用域
# 查看作用域：
# globals()： 全局和内置
# locals() ： 内部
# 在全局看: globals()  == locals()


# 函数对象打破函数的层级显示
# x=1000
# def f1():
#     def f2():
#         print(x)
#
#     return f2
#
# f=f1()
# f()  实际上就是执行的 f2()

# x=123456
# def func():
#     x=123
#     f()
#
# func()




# global  直接到全局找
# nonlocal  向上层找，不是第一次在全局找。

# x = 1
# def f1():
#     global x
#     x = 10
#
#
# f1()
# print(x)


#闭包函数：定义在内部的函数，特点是：包含对外部作用域的而不是全局作用域名字的引用，
# x = 1
# def f1():
#     x=2
#     def f2():
#         nonlocal x    在函数内部整个函数内部生效，修改的是本层函数的上层函数的值。
#         x=1111
#     f2()
#     print(x)
#
# f1()




# def func1():
#     name="alex"
#     def func2():
#         print(name)
#     func2()
#     print(func2.__closure__)  # 返回的不是 None 就是闭包函数。
#
# func1()

#  在外部调用内部函数
# def func1():
#     name="alex"
#     def func2():
#         print(name)
#         def func3():
#             print(name)
#         return  func3
#     return  func2
#
#
# func1() # 调用func1，只执行func1 的内容
# func1()()  # 调用了 func  func2
# func1()()()  # 调用了 func  func2   func3

# pyhton 规定，如果在内部函数中访问了外层函数的变量，那么这个变量将不会消亡，而是将会常驻内存中，也就就是
#   使用闭包函数，可以保证外层函数的中变量一直保存在内存中，


#










