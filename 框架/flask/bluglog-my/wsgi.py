#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/6/26 19:05
# @Project  : pycharmlearningproject
# @File     : wsgi.py


import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
if os.path.exists(dotenv_path):
    dotenv.load_dotenv(dotenv_path)

# 工厂函数
from bluglog import create_app
app=create_app()