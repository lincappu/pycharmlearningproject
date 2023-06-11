#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 14:39
# @Project  : pycharmlearningproject
# @File     : forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
