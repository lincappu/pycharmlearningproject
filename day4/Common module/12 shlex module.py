# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  shlex

# 标准形式
# s='ls -l | grep pdf'
# print(shlex.split(s))  # ['ls', '-l', '|', 'grep', 'pdf']

# 牵扯到转义字符
# s='ls -l  | grep \"wo shi shui\"'
# print(shlex.split(s))  # [['ls', '-l', '|', 'grep', 'wo shi shui']
# print(shlex.split(s))  # ['ls', '-l', '|', 'grep', 'wo shi shui']


s='ls -l | grep pdf'

obj=shlex.shlex(s)

print(obj.get_token())
print(obj.get_token())
