# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  time

# print(time.time())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.asctime())

# 三者之间的关系：
# 首先获取各自的形式的时间：
# 时间戳：
# time.time()

# 结构化时间：
# time.localtime()
# time.gmtime()

# 字符串时间：
# time.asctime()
# time.ctime()

# 转换关系：
print(time.localtime(time.time()))
print(time.gmtime(time.time()))


print(time.mktime(time.localtime()))


print(time.strftime('%Y-%m-%d %H%M%S',time.localtime()))

print(time.strftime(time.asctime()))


