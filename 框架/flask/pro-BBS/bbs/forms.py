#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/23 15:36
# @Project  : pycharmlearningproject
# @File     : forms.py
import os
import uuid
from urllib.parse import urlparse, urljoin

from flask import Flask, abort
from flask import url_for, request, redirect, render_template, flash, session, send_from_directory
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# 表单导入
from wtforms import TextAreaField, SubmitField,StringField
from wtforms.validators import DataRequired,length


class  MessageForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),length(1,200)])
    body=TextAreaField('Message',validators=[DataRequired(),length(1,2000)])
    submit=SubmitField()