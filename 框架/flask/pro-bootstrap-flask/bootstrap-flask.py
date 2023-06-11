#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/24 16:27
# @Project  : pycharmlearningproject
# @File     : bootstrap-flask.py


'''
https://bootstrap-flask.readthedocs.io/en/stable/basic/   官网

bootstrap-flask是为了替换flask-bootstrap，因为使用方法是一样的，所以两个插件不能同时存在，同时不再提供内置基模板，所以需要自己写基模板
flask-bootstrap 只支持到boot3
bootstrap-flask支持boot4 和boot5

两者之间的主要区别：
    去掉了内置的基模板，换来更大的灵活性，提供了资源引用代码生成函数
    支持Bootstrap 4
    标准化的Jinja2语法
    提供了更多方便的宏，比如简单的分页导航部件、导航链接等
    宏的功能更加丰富，比如分页导航支持传入URL片段
    统一的宏命名，即“render_*”，更符合直觉

常用的宏：
导航栏：  render_nav_item
'''


from flask import Flask, abort
from flask import url_for, request, redirect, render_template, flash, session, send_from_directory
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# 表单导入
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_bootstrap import  Bootstrap4

app=Flask(__name__)
bootstrap=Bootstrap4(app)


app.secret_key = 'dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Lexin2022@127.0.0.1:3306/world"


app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'

# set default icon title of table actions
app.config['BOOTSTRAP_TABLE_VIEW_TITLE'] = 'Read'
app.config['BOOTSTRAP_TABLE_EDIT_TITLE'] = 'Update'
app.config['BOOTSTRAP_TABLE_DELETE_TITLE'] = 'Remove'
app.config['BOOTSTRAP_TABLE_NEW_TITLE'] = 'Create'

@app.route('/nav',methods=['POST','GET'])
def test_nav():
    return render_template('nav-bs4.html')

@app.route('/index')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run()