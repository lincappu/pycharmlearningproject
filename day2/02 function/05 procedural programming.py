# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author： fls
# Date: 20171226
# Description: 查找指定目录下包含某个关键字的文件。
# Ex:   python  greprl.py  file  pattern


'''
面向过程的编程思想，解决问题的步骤
'''

# 实现grep -rl 'root'  /etc的功能

# Python的遍历文件

# import  os
#
# g=os.walk(r'/Users/FLS/Downloads/pycharmlearningproject/day2/02 function/a')
# for dirname,_,files in g:
#     for file in files:
#         abs_file_path='%s/%s' %(dirname,file)
#         print(abs_file_path)


# import os
# import sys
#
# file = sys.argv[1]
# pattern = sys.argv[2]
#
#
# def init(func):
#     def inner(*args, **kwargs):
#         g = func(*args, **kwargs)
#         next(g)
#         return g
#
#     return inner


def search(abs_file_path, target):
    g = os.walk(abs_file_path)
    for dirname, _, files in g:
        for file in files:
            abs_file_path = '%s/%s' % (dirname, file)
            target.send(abs_file_path)

@init
def openner(target):
    while True:
        abs_file_path = yield
        with open(abs_file_path, 'rb') as f:
            for line in f:
                res = target.send((line, abs_file_path))
                if res: break


@init
def grep(pattern):
    tag = False
    pattern = pattern.encode('utf-8')
    while True:
        line, abs_file_path = yield tag
        tag = False
        if pattern in line:
            print(abs_file_path)
            tag = True


search(file, openner(grep(pattern)))
