# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# exception 类：

# 1.语法异常：
# 2.逻辑异常：必须要执行后才能知道。
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         continue
#     except (ValueError,TypeError):
#         print('请输入整数')


# raise  NameError('there')

# raise 重新发起一个空异常：
import  os
# try:
#     openfile=open('test.log','r')
#     filecontent=openfile.readlines()
# except IOError:
#     print('file not exists')
#     # if not os.path.exists('test.log'):
#     #     raise
# except:
#     print('process exception')



# assert语句触发异常，

# def testassert(x):
#     assert x < 1,'这时返回的值'
#
# testassert(2)


# try
#     可能出发异常的语句块
# except (异常类型)：
#     捕获异常并附加的数据
# except:
#     指定异常类型，捕获除上面以外的异常
# else:
#     没有出现异常时，执行 else 的语句

#
# try:
#     openfile=open('test.log','r')
#     filecontent=openfile.readlines()
# except IOError:
#     print('file not exists')
# except:
#     print('process exception')
# else:
#     print('read file down')



# try的嵌套：
# try:
#     try:
#         openfile=open('tett.log','r')
#         filecontent=openfile.readlines()
#     except IOError:
#         print('file not exitsts')
# except:
#     print('process exception')
#
# else:
#     print('read file down')


# try  finally语句
# try:
#     with open('test.log','r') as f:
#         content=f.readlines()
# finally:
#     f.close()


# try和 exception、finally 连用
# try:
#     openfile=open('test.log','r')
#     content=openfile.readlines()
#     print(content)
# except IOError:
#     print('file not exitsts')
# finally:
#     openfile.close()   # 如果这个文件不存在，close 这个语句是不生效的。
#     print('文件已关闭')



# with as 异常触发自动关闭资源：
import os
# def testwhith(filename):
#     try:
#         with open('t1.log','r') as f:
#             f.read()
#             print(2/0)
#     except :
#         print('file closed:', f.closed)
#
# testwhith('t1.log')


# as 获取异常信息，用于以后分析：
# try:
#     try:
#         openfile=open('test.log','r')
#         filecontent=openfile.read()
#     except  (IOError,ValueError) as info:
#         print(info)
# except:
#         print('process exception')
# else:
#         print('read file down ')