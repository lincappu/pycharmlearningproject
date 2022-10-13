# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import inspect
import sys


''':param
inspect模块主要提供了四种用处：
(1).对是否是模块，框架，函数等进行类型检查。
(2).获取源码
(3).获取类或函数的参数的信息
(4).解析堆栈
'''

__all__ = ['str','Cat']

str='inspect'

def foo(x):
	pass


class Cat:
	def __init__(self,age=18,name='kitty'):
		self.name = name
		self._age=age
	def sayHi(self):
		print(self.name,' say hi')

cat=Cat()


print(cat.sayHi)  # 实例的 方法是绑定的
print(Cat.sayHi)  # 类的方式是没有绑定的


# 自省或者是反射

# 1、获取对象的 属性或者方法
print(cat.name)
print(dir(cat))
hasattr(cat, 'name')
setattr(cat, 'name')
delattr(cat, 'name')


# 2、访问对象的元数据
print(Cat.__doc__)

# types 模块定义全部的 python 内置内省,inspect 模块封装检查类型的方法,同时检查对象是否有对象变量/方法/类/实例/生成器
