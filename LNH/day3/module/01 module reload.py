# !/usr/bin/env python3
# _*_coding:utf-8_*_

import  sys,importlib
print(sys.modules)
importlib.reload(模块名)
# 这种重载方式不建议使用，因为需要在所有的程序中都执行一遍这个代码
# 最好的重载方式，还是重新启动系统。