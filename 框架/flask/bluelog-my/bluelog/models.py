#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 14:48
# @Project  : pycharmlearningproject
# @File     : models.py



from flask_login  import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from extensions  import db


class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

    @property
    def password(self):
        raise  AttributeError("password 属性不能被访问")

    @property.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)















