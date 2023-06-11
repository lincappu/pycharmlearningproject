#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/4/20 14:27
# @Project  : pycharmlearningproject
# @File     : 在python代码中调用python脚本.py


import os
import  importlib

'''
在python代码中调用python脚本的方法示例：

'''



# 1、 导入的方式
'''
import导入的方式，然后在b文件代码中执行a中的方法
'''

# 2、os.system()的方式： 相当于在shell环境中执行脚本
# os.system('python3  b.py')


# 3、 os.popen()的方式，比system的好处就是可以收集脚本执行的输出，
output=os.popen('python b.py')
print(output.read())

# 4、__import__的方式：
#  c.py 要和dir目录在同一级，否则需要sys.path.append()进行添加
link_a=__import__(dir.a)
link_b=__import__(dir.b)

# 5、importlib的方式：
lib_a=importlib.import_module('dir.a')  #  目录和文件

# 6、subprocess 就是调用shell来执行
import subprocess
p=subprocess.Popen('python a.py',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT )
for line in p:
    print(line)











