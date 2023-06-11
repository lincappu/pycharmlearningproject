#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/20 19:33
# @Project  : pycharmlearningproject
# @File     : settings.py.py

import os


dev_db="mysql://root:Lexin2022@127.0.0.1:3306/world"
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)