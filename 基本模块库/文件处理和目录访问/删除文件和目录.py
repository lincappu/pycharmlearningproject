#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/8 10:48
# @Project  : pycharmlearningproject
# @File     : 删除文件和目录.py

import  os
import shutil


在Windows系统中，删除一个正在使用的文件，将抛出异常。在Unix中，目录表中的记录被删除，但文件的存储还在.


os.remove()  只能删除文件
os.removedirs()  递归删除文件和目录
os.rmdir()   只能删除空的目录
os.unlink()  和remove() 的功能是一样的



删除全部文件和目录的方法：
for root,dirs,files in os.walk('top',topdown=False):
    for name in files:
        os.remove(os.path.join(root,name))
    for name in dirs:
        os.rmdir(os.path.join(root,name))


或者是：
os.removedirs()