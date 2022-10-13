# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# fractions模块
# fractions模块提供了分数类型的支持。
#
# Fraction类
# 该类是fractions模块的核心，它继承了numbers.Rational类并且实现了该类所有的方法。


# 构造函数并不复杂：
# class fractions.Fraction(numerator=0, denominator=1)
# class fractions.Fraction(int|float|str|Decimal|Fraction)



from  fractions import  Fraction

下面是各种的 fraction 实例：
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)




限制分母
fractions.Fraction.limit_denominator(max_denominator=1000000)
有时候将浮点数或者Decimal作为Fraction实例的初始化数据可能会遇到舍入误差的问题，如上面调用Fraction(1.1)时不返回Fraction(11, 10)的例子。这时Fraction类提供了一个实例方法limit_denominator()用于减小这种误差。这个方法本来是为了通过限制分母来得到一个近似值，但是在出现舍入误差的时候反倒使得结果更加精确了，如下面的例子：

>>> from fractions import Fraction
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> Fraction(1.1).limit_denominator()
Fraction(11, 10)
将Fraction用于算术运算、关系运算和其他多种操作
上面提到，Fraction类继承了numbers.Rational类并且实现了该类所有的方法。所以Fraction类事实上通过重载很多特殊函数，使得其实例可以直接用于多种算术运算。

不仅支持算术运算，Fraction类同时也支持关系运算、pickle模块、copy模块和哈希值的计算。

>>> from fractions import Fraction
>>> x = Fraction(1, 2)
>>> y = Fraction(1, 3)
>>> x + y
Fraction(5, 6)
>>> x - y
Fraction(1, 6)
>>> x * y
Fraction(1, 6)
>>> x / y
Fraction(3, 2)
>>> x ** 2
Fraction(1, 4)
>>> -x
Fraction(-1, 2)
>>> abs(x)
Fraction(1, 2)
>>> round(x)
0
>>> import math
>>> math.floor(x)
0
>>> math.ceil(x)
1
>>> x == y
False
>>> x > y
True
其他函数
fractions.Fraction.from_float(flt)
fractions.Fraction.from_decimal(dec)

在Python3.2之前，Fraction类不支持通过将浮点数和Decimal传入构造方法来获得实例。而是提供了上面两个类方法，通过调用类方法的方式来产生实例，目前版本（Python 3.6.1）这两个类方法仍然存在。

fractions.gcd(a, b)

用于计算最大公约数。这个函数在Python3.5之后就废弃了，官方建议使用math.gcd()。

