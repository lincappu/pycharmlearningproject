# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os
print(os.getcwd())  #
# print(os.chdir('/Users/FLS/Downloads/pycharmlearningproject/day4/'))



# print(os.getcwd())

line='this is  os.open'
message=str.encode(line)
fd=os.open('t1.log.sh',os.O_RDWR|os.O_CREAT)
os.write(fd,message)
os.close(fd)






# 使用 walk 或者下面的所有文件：
# for root,dirs,files in os.walk('/Users/FLS/Desktop/test/',):
    # for name in files:
    #     print(os.path.join(root,name))  # 文件绝对路径
    # for name in dirs:
    #     print(os.path.join(root,name))   # 目录绝对路径



