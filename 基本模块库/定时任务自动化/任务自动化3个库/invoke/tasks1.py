#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/28 14:50
# @Project  : pycharmlearningproject
# @File     : tasks1.py

from invoke import task

@task
def hello(c):
    print('helloworld')

@task(help={'name': 'A param for test'})
def greet(c, name):
    """
    A test for shell command.
    Second line.
    """
    c.run(f"echo {name}加油!")
