
'''描述：
filter()
函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回
True或False，最后将返回True的元素放到新列表中。

语法：
以下是filter()方法的语法:

filter(function, iterable)
参数：
function - - 判断函数。
iterable - - 可迭代对象。
返回值：列表。

实例：
以下展示了使用
filter
函数的实例：

过滤出列表中的所有奇数：
# !/usr/bin/python
# -*- coding: UTF-8 -*-

def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
输出结果 ：

[1, 3, 5, 7, 9]

2.过滤出1~100中平方根是整数的数：

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1, 101))
print(newlist)
输出结果 ：
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


# 注意：
# 上述是在 Python2的方法，在 python3中，返回的是一个filter 类，filter类实现了__iter__和__next__方法,
# 可以看成是一个迭代器, \有惰性运算的特性, 相对python2提升了性能, 可以节约内存
# 这时候取值方法：
def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for  item  in  newlist:  # 这取出来是字符串。
    print(item)


# 这样取出来的是字符串格式的，这里有问题问题要注意下，上面执行完后，下面取出来的是空值，因为迭代器已经取完了，
# 要想再取值，需要重新迭代
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l1 = [item for item in newlist]
print(l1)