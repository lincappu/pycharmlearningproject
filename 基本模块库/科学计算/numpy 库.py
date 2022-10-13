# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author

import numpy as np
from  numpy import pi
from  numpy import  random
print(np.vander)

# array函数
# array=[0,1,2,3,4,5,6]
# print(array)

# 1、创建数组的方式
# a=np.array([1,2,3,4]) #传入的参数一定要类型，列表，不能只传参数
# a=np.array([1.2,2.,3,4]) #传入的参数一定要类型，列表，不能只传参数
# print(a.dtype)

# ab=np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(ab)

# 占位函数数组
# zeros 填充 0
# ones 填充  1
# empty  填充随机数  float64 类型
# print(np.empty([2,3]))
# print(np.arange(1,10,2))  # 返回的数组 不是列表

# linspace函数： 接受有很多个数的数组
# print(np.linspace(1,2*pi))

# 生成随机数
# print(np.random.random(2,3))





# 2、打印数组
# print(np.arange(24).reshape(2,3,4))




# 3、基本操作
# 数组上的算术运算符会应用到 元素 级别
# @ 矩阵乘积
# +-*%/  += -=都是按元素运算
#
# axis参数： 指定沿哪个轴操作 0 列  1 行
# b=np.arange(12).reshape(3,4)
# print(b)
# print(b.sum(axis=0))
# print(b.sum(axis=1))
# print(b.min(axis=1))
# print(b.max(axis=1))
# print(b.cumsum(axis=1))


# 4、通函数
# b = np.arange(12).reshape(3, 4)
# print(b.all())


# 5、索引、切片、迭代
# 针对一维数组，和列表操作是一样的
# 多维数组，每个轴都有一个索引，
# b[0:2,3]  第一个代表是行号，第二个是列
b=np.array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
# print(b[2,3])
# print(b[0:4,1])
# print(b[-1])

# ... 代表中间剩余的多个轴，


# 迭代是针对第一个轴完成的：
for row in b


    print(row)

for row in b.flat:  # 针对每个元素
    print(row)


# 6、视图和拷贝
# 1.完全不复制   可变对象传递的是引用
# 2.视图既浅拷贝  不同的数组共享相同的数据
# 3.深拷贝 完全拷贝   copy() fa
#

# 7、线性代数


