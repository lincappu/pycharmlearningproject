#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/5/28 15:01
# @Project  : pycharmlearningproject
# @File     : fakes.py

from  faker  import Faker

from extensions import db
from models import Admin,Category,Post,Comment,Link

fake=Faker()


def fake_admin():
    admin=Admin(
        username='admin',
        blog_title="Bluelog",
        blog_sub_title='this is my bluelog',
        name="fls",
        about="这是我自己编写的bluelog项目"
    )
    admin.password="helloflask"
    db.session.add(admin)
    db.session.commit()

def fake_category(count=10):
    category=Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category=Category(name=fake.word)







