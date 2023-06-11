#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2022/10/18 15:27
# @Project  : pycharmlearningproject
# @File     : 对目录下文件的遍历.py


import os
import re

'''
如何快速获取一个文件夹下的所有文件，或者是目录和文件的路径集合。
1、walk(dir)的方式
os.walk(topdir,topdown=True,onerror=None,followlinks=False)
说明：
top：指定遍历目录的地址
topdown：默认为真，含义是优先遍历指定的目录地址，否则优先遍历目录下的子目录
onerror：指定一个 callable 对象，这个是当发生异常的时候，会调用
followlinke：默认为假，含义是不遍历目录下的快捷方式

返回：
os.walk 的返回值是一个可遍历的对象，每次遍历返回的是一个三元元组，可用root,dirs,files接收
root：遍历到
dirs：list 对象，存储遍历到该目录下的子目录名称
files：list 格式，存储遍历到该目录下的文件
'''
basedir = './base'

# 只是拿到所有的文件的文件名
# def findAllfile(basedir):
#     for root, ds, fs in os.walk(basedir):
#         print(root)
#         print(ds)
#         print(fs)
#         for f in fs:
#             yield f

# 拿到带完整路径的文件名
# def findAllfile(basedir):
#     for root, ds, fs in os.walk(basedir):
#         for f in fs:
#             fullname=os.path.join(root,f)
#             yield fullname


# 返回特定类型的文件的路径，
# def findAllfile(basedir):
#     for root, ds, fs in os.walk(basedir):
#         for f in fs:
#             if f.endswith('.xlsx'):
#                 fullname=os.path.join(root,f)
#                 yield fullname

# 更加复杂的可以用RE正则表示
def findAllfile(basedir):
    for root, ds, fs in os.walk(basedir):
        for f in fs:
            if re.match(r'.*\d.*',f):
                fullname=os.path.join(root,f)
                yield fullname


'''
2、os.listdir(basedir)的方式
os.listdir(basedir) 
返回：
当前目录下的目录和文件的列表
'''
# 最简单的方式
# def findlistdir():
#     for f in os.listdir(basedir):
#         print(f)
#

# 递归的方式拿到所有的文件路径
def findlistdir(basedir,filelist):
    newDir=basedir
    if os.path.isfile(basedir):
        # 如果是只返回文件名
        filelist

        filelist.append(basedir)
    elif os.path.isdir(basedir):
        for s in os.listdir(basedir):
            newDir=os.path.join(basedir,s)
            findlistdir(newDir,filelist)
    return filelist

if __name__ == '__main__':
    filelist=[]
    res=findlistdir(basedir,filelist)
    print(res)
    for f in res:
        print(f)