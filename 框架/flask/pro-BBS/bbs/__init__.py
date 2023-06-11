#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/20 19:21
# @Project  : pycharmlearningproject
# @File     : __init__.py.py

from flask import Flask, abort
from flask import url_for, request, redirect, render_template, flash, session, send_from_directory
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import sys
from flask_debugtoolbar import DebugToolbarExtension


app=Flask('bbs')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db=SQLAlchemy(app)
bootstrap=Bootstrap(app)
moment=Moment(app)
toolbar=DebugToolbarExtension(app)

# 放在末尾导入，是为了避免循环导入
from bbs import views,commands,errors