# !/usr/bin/env python3
# -*- coding:utf-8 -*-
#

# 函数在定义阶段只检查语法，执行的时候才会检查逻辑.

# 调用函数的过程中，遇到return 就结束函数的执行，并且把 return 值作为返回值返回，函数体内可以有多个函数值，但是只能执行一个。
# 返回值可以是任意类型的值
# 0个返回值:null类型
# 一个返回值：就是值本身类型
# 多个返回值： 元组类型。
# def a():
#     pass
#
#
# def b():
#     return 1
#
#
# def c():
#     return 1, 2, 3
#
#
# res1 = a()
# res2 = b()
# res3 = c()
# print(res1, type(res1), '\n', res2, type(res2), '\n', res3, type(res3), )
#

# 函数的调用方式：
# 直接调用，放在表达式中，另外一个函数的参数。
# 函数的返回值本身就是个变量


# 函数的参数
# 形参：位置参数，默认参数     经常变的定义为位置参数，经常不变的定义为默认参数。
# 实参：位置参数，关键字参数
# 他们两只没有一对一关系

# def max(x, y=10):
#     if x > y:
#         return x
#     if x < y:
#         return y
#
#
# res = max(x=10, y=43)
# print(res)

# 默认参数：只在定义的时候赋值一次，后续不再修改这个值。默认参数的值是不可变类型，并且要放在形参的最后。
# x = 'male'
# def reg(name, age, sex=x):
#     print(name, age, sex)
#
# x = 'female'
# reg('alex', 18)
# 结果：alex 18 male  结论：默认参数只在定义的时候赋值了，后续的变化与他没有关系



# 可变长参数：就是实参个数不固定，导致形参个数也不确定，这时就不能在定义的时候定义参数的个数，处理方式。
# * 针对溢出位置实参
# ** 针对溢出关键字实参

# * 负责接收多出来的位置实参数，然后复制给 args。args 只是个变量名，可以随意起。
# def func(x, y, z, *args):
#     print(x, y, z, '\n', args)


# func(1,2,3,4,5,6)
# func(1, 2, 3, *[4, 5, 6])  # * 直接打散翻译成位置参数 == func（1，2，3，4，5，6）
# func(*[1,2,3,4,5,6]) == func(1,2,3,4,5,6)
# func([1,2,3,4,5,6])   # x=[1,2,3,4,5,6]


# 针对按照关键字定义的  **kwargs
# def foo(x,y,**kwargs):  # ** 接收多余的实参，然后写成字典的形式复制给 kwargs
#     print(x,y,kwargs)

# foo(y=2,x=1,z=3,a=1,B=2)
# foo(1,2,3,z=3,a=1,B=2) # 只能给两个不给关键字的实参，
# 同理：
# foo(1,2,**{'a':1,'b':2,'z':3})  按关键字打算，foo（x=1,y=2,a=1,b=2,z=3）


# 注意：
# def home(name,age,sex):
#     print(name,age,sex)
#
#
# def wrapper(*args,**kwargs):
#     print(args)
#     print(kwargs)
    # home(*args,**kwargs) # home(1,2,3,4,5,6,7,a=1,b=2,c=3)
#
# wrapper(1,2,3,4,5,6,7,a=1,b=2,c=3) # args=(1,2,3,4,5,6,7) kwargs={'a':1,'b':2,'c':3}

# 总结：
# 1.*args **kwargs：目的就是接收任意类型、个数的参数。
# 2.实参的个数要以内部函数的个数为准，外部函数接收的参数原封不动的交给内部函数




# 命名关键字参数
# 形参中在* 后定义的参数，称为命名关键字参数。
# 特性： 传值时，必须按照关键字传值
# def foo(x,y=2,*args,a=1,b,):  # 这a=1不是默认值参数，这时命名关键字参数，
#     print(args)
#     print(x,y,a,b)
#
# foo(1,2,3,4,5,a=3,b=4)

# 形式参数排序：位置参数  默认参数  *args   命令关键字参数 **kwargs





