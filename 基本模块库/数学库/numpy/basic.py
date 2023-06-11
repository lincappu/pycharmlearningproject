#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2022/11/26 12:04
# @Project  : pycharmlearningproject
# @File     : basic.py

import numpy as np

my_array=np.array([1,2,3,4,5])
print(my_array)

print(my_array.shape)  #查看形状 

all_zeros= np.zeros((5))
print(all_zeros)

all_ones=np.ones((2))
print(all_ones)

# 加减乘除是元素的加减乘除，

# 矩阵乘积
# a.dot(b)