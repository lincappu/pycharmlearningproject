# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 类似于一个持久化对象的持久化字典，既字典文件

import  shelve

f=shelve.open(r't1.sh')  # 这个文件不能提前存在。 生成的文件编码是特定的，不能随意查看，

f['stu1_info']={'name':'egon','age':18,'hobby':{'read','drinking'}}
f['stu2_info']={'name':'gangdan','age':19,'hobby':{'1','2','3'}}

print(f['stu1_info']['name'])

f.close()