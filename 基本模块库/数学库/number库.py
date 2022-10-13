# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from numbers import Number


此模块中所定义的类型都不可被实例化。


class numbers.Number
数字的层次结构的基础。如果你只想确认参数 x 是不是数字而不关心其类型，则使用``isinstance(x, Number)``

a=1
print(isinstance(a,Number))
