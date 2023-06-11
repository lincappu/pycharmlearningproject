#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/20 18:53
# @Project  : pycharmlearningproject
# @File     : __init__.py.py

'''
应用工厂模式：
    以flask为例：
    正常的情况下是在app.py里定义一个global的app实例，所有import的都是共享这个实例的 
    在工厂模式中，在__init__.py 创建app，这样谁导入这个包，就创建一个实例，各自实例之间相互独立，

'''


import os
import sys
from flask  import Flask

def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True) # instance_relative_config是指在实例文件夹中查找config文件，所以后面就不用改了

    app.config.from_mapping(
        DEBUG=False,
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        print('创建instance文件失败！')
        sys.exit(1)

    return app



















