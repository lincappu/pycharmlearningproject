# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author： fls
# Date: 20171226
# Description: 查找指定目录下包含某个关键字的文件。
# Ex:   python  greprl.py  file  pattern


import os
import sys

file = sys.argv[1]
pattern = sys.argv[2]


def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return inner


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
