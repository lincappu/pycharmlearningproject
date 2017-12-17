#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 打开
# 打开文件的原理
# 1、由应用程序向操作系统发起系统调用open(...)
# 2、操作系统打开该文件，并返回一个文件句柄给应用程序
# 3、应用程序将文件句柄赋值给变量f
# 注意：
# 1.打开一个文件对应两部分，一个 python 管理的文件句柄，一个是文件操作系统打开的文件。（默认）
# 打开文件的编码是以操作系统的编码操作为准的，除非open（）时指定文件编码类型。
# 2.资源回收
# def f  是回收应用资源，python 解释器自动回收的
# f.close 回收操作系统的资源，这个是需要我们手动操作的。
# 3.python只能将字符串写入到文本文件。要将数值数据存储到文本本件中，必须先试用函数str()将其转换为字符串格式
# f = open('test.txt', mode='r')
# data = f.read()
# print(data)
# print(f.name)
# print(f.tell())
# print(f.readlines(),end='') # 取消 print 的换行符，默认 readline 后面有一个换行符

# 可以使用 try/finally 语句来保证能关闭文件
# f = open('test.txt',mode='r',encoding='utf-8')
# try:
# print(f.read())
# finally:
#     f.close()

# 上下文管理，这样就不用使用 f.close 来手动关闭文件
# with open('test.txt',mode='r',encoding='utf-8') as f:
#     print(f.read())

#  在python2中 常用type（f） 查看 file类型。



# 文件打开模式:
## mode:
# 默认是只读模式
# 模 式     描述
# r   以读方式打开文件，可读取文件信息。
# rb  以二进制格式打开一个文件只读
# w   以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容；如果文件不存在则创建
# a   以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
# r+  以读写方式打开文件，可对文件进行读和写操作。指针放在文件开头
# w+  消除文件内容，然后以读写方式打开文件。
# wb+  消除文件内容，然后以读写方式打开文件。二进制格式的读写
# a+  以读写方式打开文件，并把文件指针移到文件尾。
# b   以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。

# 常见的操作方法:
# 自身属性
# f.close()
# f.name
# f.seek(0) #将文件位置定位到第一行，第一个字节。
# f.tell() #返回文件读的位置，注意加上换行符的个数


# 读：
# f.read(4) #默认是读全部内容，n表示读多少个字节。
# f.read(6) #这个是接上次的继续读
# f.readable() # 文件是否可读
# f.readline(n) #一次读一行，或者 n bytes
# f.readlines() #读取全部的文件内容,一行显示。


# 遍历文件:

# 读了 n 行
# f = open('test.txt', 'r', encoding='utf-8')
# for i in range(8):
# print(i)
# print(f.readline(),end='')



# 读了全部
# for line in f.readlines():
#     print(line,end='')
#

#  读了全部
# for index,line in enumerate(f.readlines()):
#     if index == 2:
#         print('这时第三行')
#         continue
#     print(index)
# print(line,end='')

# 读了全部
# for line in f:
#     print(line,end='')

# 只读了前三行
# count = 0
# for line in f:
#     if count == 2:
#         print('这时第三行')
#     count += 1
#     print(line, end='')

# f.close()

# 写：
# f=open('test.txt',mode='w',encoding='utf-8')
# f.write('111\n')
# f.write('222\n')
# f.write('333\n')
# f.writelines(['444\n','555\n','666\n'])
# print(f.writable())

# a 追加写模式,不存在则创建，存在则追加
# f=open('test.txt','a',encoding='utf8')
# f.write('777\n')
# f.writelines(['888\n','999\n'])
# print(f.writable())
# print(f.readable())
#
# 关闭
