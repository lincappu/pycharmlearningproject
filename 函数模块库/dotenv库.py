#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/24 17:41
# @Project  : pycharmlearningproject
# @File     : dotenv库.py


from dotenv import load_dotenv
from io import  StringIO
import os

'''
dotenv就是读取.env的配置文件供使用。override=True 覆盖
1、load_dotenv 并不覆盖存在的环境变量
2、dotenv_values 只是加载值，但不设置环境变量

'''



load_dotenv('./.env')
print(os.getenv("ADMIN_EMAIL"))
print(os.environ)


# 从字符流中获取值
config=StringIO("USER=foo\nEMAIL=foo@example.org")
load_dotenv(stream=config)
print(os.getenv("USER"))
print(os.getenv("EMAIL"))