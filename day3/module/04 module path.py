# !/usr/bin/env python3
# _*_coding:utf-8_*_

#
# 查找顺序：内存已加载的模块，内置模块，sys.path 路径中模块。



# print(sys.path)


# 这个是在解释器中执行的结果：
'''
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', \
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', \
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', \
'/usr/local/lib/python3.6/site-packages'
'''


# 这个是 pycharm 执行的结果：
'''
/usr/local/bin/python3.6
"/Users/FLS/Downloads/pycharmlearningproject/day3/module/04 module path.py"
['/Users/FLS/Downloads/pycharmlearningproject/day3/module',
'/Users/FLS/Downloads/pycharmlearningproject',
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
'/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',
'/usr/local/lib/python3.6/site-packages']
'''



# 添加新的模块方法：
# 1.放在 sys.path 路径下
# 2.导入：
# import  sys
# sys.path.append(r'/Users/FLS/Downloads/pycharmlearningproject/day3/module/module')
# print(sys.path)
# import  spam

# 3.通过 from 导入：
from module import spam
