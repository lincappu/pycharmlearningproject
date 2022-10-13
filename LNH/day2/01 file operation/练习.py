# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# import  time
# with open('test.txt',mode='rb') as f:
#     f.seek(0,2)
#     while True:
#         line = f.read()
#         if line:
#             print(line.decode('utf-8'),end='')
#         else:
#             time.sleep(0.2)


# 1. 使用文件的 b 模式编写一个 scp 工具。
# import sys
#
# if len(sys.argv) != 3:
#     print('Usage: cp soure_file  target_file')
#     sys.exit()
#
# s_file, d_file = sys.argv[1], sys.argv[2]
# with open(s_file, 'rb') as s, open(d_file, 'wb') as d:
#     for line in s:
#         print(line)
#         d.write(line)
#
# print(sys.argv)

# 2.不同的读方式
# 文件的读取及修改方式，是全部还是一行一样的
# 全部：
# import os
# with open('test.txt') as read_f, open('test.txt.swap', 'w') as write_f:
#     data = read_f.read()
#     data = data.replace('你好', '你们好')
#
#     write_f.write(data)
#
# os.remove('test.txt')
# os.rename('test.txt.swap', 'test.txt')

# 一行一行的读进内存
# import os
# with open('test.txt') as read_f, open('test.txt.swap', 'w') as write_f:
#     for line in read_f:
#         line = line.replace('你好','你们好')
#         write_f.write(line)
#
# os.remove('test.txt')
# os.rename('test.txt.swap','test.txt')

# with open('log','a') as f:
#     f.write('woshihaoah')
