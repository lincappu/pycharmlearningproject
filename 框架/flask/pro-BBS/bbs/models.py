#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/2/23 15:34
# @Project  : pycharmlearningproject
# @File     : models.py


import datetime
from . import db

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)