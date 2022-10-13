# !/usr/bin/env python3
# _*_coding:utf-8_*_

__all__=['foo']

print('from m.py')


m=10

def foo():
    m=10
    print('from foo',)

def bar():
    print('from bar')


print(__name__)