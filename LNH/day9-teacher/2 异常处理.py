#1 什么是异常：程序运行时发生错误的信号（一旦出错，就会产生一个异常，
# 如果该异常没有被应用程序处理，那么该异常才会抛出来，程序也随之终止）
# print('=====>')
# print('=====>')
# print('=====>')
# aaa
# print('=====>')
# print('=====>')
# print('=====>')


#2 异常分类
#分类一：针对语法上的异常，应该在程序执行前就解决掉
# try:
#     print('asdfasdf'
# except Exception:
#     pass

#分类二：逻辑异常，try...except
# xxx #NameError

# int('xxxxxxx') #valueError

# l=[]
# l[111111] #IndexError

# d={}
# d['a'] #keyError

# 1/0 #ZeroDivisionError:

# import os
# os.xxxxxxxxxxx #AttributeError:


#处理异常的方式：try 。。。except
# import os
# try:
#     print('===>1')
#     print('===>2')
#     l=[]
#     # l[123] #IndexError
#     print('===>3')
#     d={}
#     d['a'] #KeyError
#     # aaa
#     # os.xxxx
# # except AttributeError as x:
# #     # import os
# #     # os.xxx
# #     pass
# except IndexError as y:
#     # print(x)
#     # l[0]
#     pass
# # except Exception as z:
# #     print('Ex',z)
# else:
#     print('被检测的代码块没有发生异常时执行else的代码')
#
# print('====>4')


#
# if 异常 == AttributeError:
#     x=异常值
# elif 异常 == IndexError:
#     x = 异常值



# try:
#     print('===>1')
#     print('===>2')
#     cursor= connect(数据)
#     cursor.excute(sql)
#     cursor.excute(sql)
#     cursor.excute(sql)
#     cursor.excute(sql)
#
#     print('===>3')
#     d = {}
#
# except Exception:
#     print('异常发生时执行的代码')
#     # cursor.close()
# finally:
#     #不管程序是否出错，都会执行finally的代码
#     cursor.close()



#自定义异常
# class MySQL_CONN_ERROR(BaseException):
#     def __init__(self,value):
#         self.value=value
#
#     def __str__(self):
#         return '出错啦老铁：%s' %self.value


# if 2 > 1:
#     # raise TypeError('类型错误')
#     # raise MyException('类型错误')
#     raise MySQL_CONN_ERROR('数据库连接错误')



#断言
assert 表达式
等价于：
if not expression:
    raise AssertionError

判断一个表达式是否成立，当表达式为false的时候触发异常，
断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。

# res=[]
# if len(res) > 0:
#     res[0]
#     res[1]
# else:
#     # print('上一部分的代码有问题')
#     raise PermissionError('xxxxx')

#
# res=[]
# assert len(res) > 0
# res[0]
# res[1]








