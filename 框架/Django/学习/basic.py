# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  django

from django.contrib.auth.models import User


# print(django.get_version())

user=User.objects.create_user('test','test@qq.com','renhe2020')
user.last_name='Lennon'
user.save()