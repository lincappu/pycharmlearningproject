# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# Day 16-20 python语言进阶：
#
# 重点知识：
# 1.函数变量的查找顺序：LEGB  local  enclosing  global  build-in
#
# 2.global 声明或者定义一个全局变量
#     nonlocal 声明使用嵌套作用域的变量，嵌套作用域必须存在改变量，否则报错
# nonlocal 在函数或者在其他作用域中使用外层但非全局的变量
# 例子：
def work():
    x=0
    def new_work():
        nonlocal x
        x=x+3
        return x
    return new_work

f=work()
print(f())
print(f())
print(f())
# 用 global 同样可以实现
# 如果用闭包来实现，就不会是这个效果
def work():
    x=0
    def new_work():
        d=x+3
        return d
    return new_work

f=work()
print(f())
print(f())
print(f())
这样的话这个值是不会变化的，因为 x 的值是不会变化的












