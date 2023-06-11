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

#



# 读：
# with open('test.txt','r',encoding='utf-8') as f:

# f.read(4) #默认是读全部内容，n表示读多少个字节。
# f.read(6) #这个是接上次的继续读
# f.readable() # 文件是否可读
# f.readline(n) #一次读一行，或者 一行的n bytes
# f.readlines() #读取全部的文件内容,以列表的形式显示。

# 遍历文件:

# 读了 n 行
# f = open('test.txt', 'r', encoding='utf-8')
# for i in range(8):
# print(i)
# print(f.readline(),end='')


# 读了全部，但是是一行一行的显示
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

# 这个是逐行读
# for line in f:
#     print(line,end='')

# 逐行读
# count = 0
# for line in f:
#     if count == 2:
#         print('这时第三行')
#     count += 1
#     print(line, end='')

# f.close()


# 一行一行读的三种方法：
# 第一种：
# f = open("foo.txt")  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# while line:
#     print
#     line,  # 后面跟 ',' 将忽略换行符
#     print(line, end = '')　      # 在 Python 3 中使用
    # line = f.readline()
#
# f.close()
#
# 第二种：
# for line in open("foo.txt"):
#     print line,
#
# 第三种：
# f = open("c:\\11.txt","r")
# lines = f.readlines()      #读取全部内容 ，并以列表方式返回
# for line in lines
#     print line
#
# 一次性读所有文件的方法：
# file_object = open('thefile.txt')
# try:
#      all_the_text = file_object.read()
# finally:
#      file_object.close()



# 写： 写模式是不能进行读操作的。
# f=open('test.txt',mode='w',encoding='utf-8')
# f.write('111\n')
# f.write('222\n')
# f.write('333\n')
# f.writelines(['444\n','555\n','666\n'])
# print(f.writable())


# a 追加写模式,不存在则创建，存在则追加
# f=open('test.txt','a',encoding='utf8')
# f.write('777\n')
# writelines  列表形式的多行一次性写入
# f.writelines(['888\n','999\n'])

# print(f.writable())
#

# 二进制文件的读取：
# 二进制文件和文本文件的区别：
# 文本文件取出来的都是字符串类型的数据，字符类型的数据就需要考虑当时是按什么存进去的就要以什么方式的编码取出来，所以就是需要制定字符编码。mode='rt'
# 而二进制文件都是按照 bytes 类型读的，不需要按照制定类型。也不能制定，会报错。

# with open('bz.jpg','rb') as f:
#     print(f.read())
#     print(f.read().decode('utf-8'))  # 这步就不能进行操作，因为只有原来是字符串类型的 encode 成 bytes 类型，才能进行 decode，原来是二进制
#                                        类型的则不能进行转码。
# 用二进制方式可以打开文本文件： 可以读出来，但是是最原始的格式，没有经过最原始的转码,这是对汉字来说是的，对于字符来说，你看到的直接就是他本身。
# with open('test.txt','rb') as f:      # 由于 python3默认字符串就是 unicode 类型，所以 bytes 类型是 encode 成 bytes 类型。
#     data=f.read()
#     print(data)
# 字符类型的数据编码后也可以使用 decode 重新编码，这样你就可以看见，但这只针对字符类型，对于二进制类型就没有这种效果。
# with open('test.txt','rb') as f:
#     data=f.read()
#     print(data.decode('utf-8')) # 这步是 decode的操作，因为他原来就就是 unicode 类型的。

# 以 bytes 类型操作文件，
# with open('d.txt','wb') as f:
#     data=f.write(b'\xe4\xbd\xa0\xe5\xa5\xbd\n')
#     print(data)

# 读写模式  r+  一定是先读后写，涉及到游标的问题，读完后，才会在末尾开始写，不然会从开头写。无论读了多少，只要有这个读的操作，写入的时候都是在末尾写入
# with open('log','r+',encoding='utf-8') as f:
#     msg=f.read(1)
#     print(msg)
#     f.write('r+')

# 写读模式  w+  这个是先写入，也就是先清空这个文件，然后在读取，但这时候游标已经在末尾了，所以读取的肯定是空，
# with open('log','w+',encoding='utf-8') as f:
#     f.write('r+')
#     msg=f.read(1)
#     print(msg)

# 追加模式： a+  a+b  这个肯定是读不到数据的，游标直接挪到末尾进行写入。
# with open('log','a+',encoding='utf-8') as f:
#     f.write('r+')
#     msg=f.read(1)
#     print(msg)


# 其他操作：
# 自身属性：f.name
# 文件打开模式为文本代表读取3个字符，为 b 模式代表读取3个字节。光标移动都是以字节为单位。
# seek  偏移设置该文件的当前位置，参数是可选的，第一个参数是 offsets，第二个参数有三种移动方式 0 1 2，0 是绝对定位，定位到开头，1，是相对定位当前位置，2定位于文件末尾。1、2必须在b模式下，但无论哪种模式下都是以字节为单位。
# f.seek(offfset,whence=0) #将文件位置定位到第一行，第一个字节。
# with open('log','r+b') as f:
#     f.seek(3,0)
#     print(f.tell())
#     msg=f.read()
#     print(msg)

# truncate 是截断文件，就是将后面的内容全部删除，不能以 w w+代开，只能以 r+ a+ a 打开。
# with open('log','r+b') as f:
#     print(f.tell())
#     msg=f.read(5)
#     print(msg)
#     f.truncate(8)   # 从 0 为坐标，n 位置处截断。

# f.tell() #返回文件读的位置，注意加上换行符的个数,是从 0 开始的，英文是一个字符，中文是 3 个字符。
# with open('log','r+',encoding='utf-8') as f:
#     msg=f.read(3)
#     print(f.tell())
#     print(msg)
# 上面这三个只有在文本模式下才是字符，其余都是字节

# f.flush() # 写一行刷新一行，直接刷到硬盘上


# f.cose()



# import  os
#
# with open('log','r',encoding='utf-8') as f1,open('log1','w',encoding='utf-8') as f2:
#     for line in f1:
#         newline=line.replace('a','1111')    # replace 不是在原来的行上操作。
#         f2.write(newline)
# os.remove('log')
# os.rename('log1','log')











