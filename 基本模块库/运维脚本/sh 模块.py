# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
import sh
from sh import  rsync
from sh import Command

'''
sh 是用来代替 subprocess 模块的，能够更方面的和 shell 交互，
本质是用将系统的命令动态映射到 python 函数，表面上执行的是 shell命令，实际上是执行在 ptyhon 函数，以 Python的方式来写 shell 脚本。

1. sh.Command() ，26个项目使用
2. sh.ErrorReturnCode() ，22个项目使用
3. sh.ErrorReturnCode_1() ，13个项目使用
4. sh.git() ，12个项目使用
5. sh.rm() ，12个项目使用
6. sh.which() ，5个项目使用
7. sh.tar() ，5个项目使用
8. sh.cp() ，5个项目使用
'''

# 1、Command 一个可执行命令，然后用 install 带参数。
pip=sh.Command('/usr/local/bin/pip3')
res=pip.install('sh')
print(res.stdout)

