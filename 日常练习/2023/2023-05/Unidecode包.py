#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/18 19:23
# @Project  : pycharmlearningproject
# @File     : Unidecode包.py


import sys

"""
unicode编码：
python2中的str其实就是ASCII 编码，能自动打印，sys.getdefaultencoding()能获取默认的编码，而unicode编码就是unicode编码：
python3中全部unicode编码，所有自然就包含ASCII编码，

在python3 全部unicode，所以自然就包括ascii，就自然包括str，所以python3中就只有unicode一个类型，这个类型是原始类型，可以被阅读的类型

bytes类型是编码过得机器类型



unidecode就是将unicode类型转换为ascii类型的工具
"""
import unidecode



print(sys.getdefaultencoding())

print(bytes("s",encoding="utf-8").decode())

