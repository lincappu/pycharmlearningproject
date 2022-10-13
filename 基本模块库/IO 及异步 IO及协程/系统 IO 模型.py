# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import io


# 系统 io：
# IOBase 是基类：
# io 模块有三种io模型：
# 文本 io     TextIOBase   StringIO
# 二进制 io   BufferedIOBase
# 原始 io    RawIOBase
# 内存中的流： stdin  stdout stderr




# --------文本流，主要包括文件和内存文本流


#   路径
# window下路径是\   但是\是转义符,所以需要转义,所以在window上 os.path.join('demo', 'exercise') 结果是'demo\\exercise'
# linux下就是/  并且不需要转义

#缓冲区 buffering=   open()的时候指定的参数，文本模式必须指定，二进制模式可以不指定。

# readline 默认会加个空行，然后 print也会加个空行，
with open('1.log','r',encoding='utf-8') as f:
    # for line in f:
    #     print(line,end='')


    # print(f.readlines())  #  结果是是列表
    # lines=f.readlines()
    # for l in lines:
    #     print(l,end='')

    # readline 判断文件结束的访问 就是判断是一个空行，文中的空行不是真正的空行，最少有一个换行符

    # while True:
    #     line=f.readline()
    #     if line:  # if line !=''
    #         print(line,end='')
    #     else:
    #         break

    pass




# print('ss',end='')  去掉 print 这个空行。
# print('aa')

#  f.flush() 在没有 f.close()之前将数据刷到磁盘上的方法。


# f.writelines 写入字符串列表，不会给每行加个换行符，
# f = open('a.txt', 'r')
# n = open('b.txt','w+')
# n.writelines(f.readlines())





# 指针相关： seek 和 tell 两个方法

# with as  上下文管理器，
# 带__enter__()和__exit__()方法就是上下文管理器，作用就是为了如果关闭的操作出现问题导致没有关闭，使用 with as 能保证无论操作语句结果如何，最后都能关闭文件。

# fileinput 模块，一次读取多个文件
# llinecache 模块 指定文件中的某一行
# fnmatch  匹配指定文件名模式的文件


# tempfile模块。 TemporaryFile()这个方法生成的临时文件没有文件名，不要进行寻找。


# 内存中的文本流stringIO
# s=io.StringIO('nihao')
# print(s.read())



# -------二进制IO流------
''''
文件就是  rb 模式
内存就是 bytesIO
'''
# b=io.BytesIO(b'sss')
# print(b.read())







# ------原始 IO 流-  RawIOBase-------
'''
原始 I/O（也称为 非缓冲 I/O）通常用作二进制和文本流的低级构建块。用户代码直接操作原始流的用法非常罕见。不过，可以通过在禁用缓冲的情况下以二进制模式打开文件来创建原始流：

f = open("myfile.jpg", "rb", buffering=0)

'''







# -------总结
''''

抽象基类           继承       抽象方法                          Mixin方法和属性

IOBase                    fileno, seek, 和 truncate        close, closed, __enter__, __exit__, flush, isatty, __iter__, __next__, readable, readline, readlines, seekable, tell, writable 和 writelines


RawIOBase        IOBase     readinto 和 write                继承 IOBase 方法, read, 和 readall

BufferedIOBase   IOBase     detach, read, read1, 和 write    继承 IOBase 方法, readinto, 和 readinto1

TextIOBase      IOBase      detach, read, readline, 和 write  继承 IOBase 方法, encoding, errors, 和 newlines

'''



# 如何一次性读取很大的文件:  核心思想：就是分批读
#1. f.read(2048)  # 每次读一部分
#2  readline   一行一行读
#3.  最 pythonic的方法就是生成文件句柄fp，把 fp 当做一个生成器，用 for 循环遍历
# with open('1.log','r',encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# 4. yield生成器读取大文件，用 next（）方法来读
def read():
    with open('1.log','r',encoding='utf-8') as f:
        while True:
            block=f.read(30)
            if block:
                yield block
            else:
                return
a=read()
print(next(a))





