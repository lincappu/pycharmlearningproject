#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


# seek()的三种模式：
#     （1）f.seek(p,0)  移动当文件第p个字节处，绝对位置
#     （2）f.seek(p,1)  移动到相对于当前位置之后的p个字节
#     （3）f.seek(p,2)  移动到相对文章尾之后的p个字节
# 如果文件打开模式中没有b 则只能使用默认值0从头开始计算偏移，否则报错

# f = open('test.txt','r+',encoding='utf-8')
# print('Name if file :%s' %(f.name))

# line = f.readline()
# print('Read line is : %s' %(line))
#
# print(f.tell())
#
# i = 1
# while i<=5:
#     f.seek(0,0)
#     print(f.tell())
#     line = f.readline()
#     print('Read line is : %s' %(line))
#     print(f.tell())
#     i+=1

# with open('test.txt','w+',encoding='utf-8') as f:
#     f.write('www\n')
#     print(f.tell())

# print(f.truncate(13)) # 返回值是就是 n ，注意 \n

