# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  cProfile
import  re

'''
cProfile自python2.5以来就是标准版Python解释器默认的性能分析器。
其他版本的python，比如PyPy里没有cProfile的。
cProfile是一种确定性分析器，只测量CPU时间，并不关心内存消耗和其他与内存相关联的信息。
'''

print(cProfile.run('re.compile("aaa")'))