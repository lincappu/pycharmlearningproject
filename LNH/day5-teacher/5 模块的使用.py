#第一部分：import

#导入模块，只会在第一次导入时执行源文件的代码
#如果模块已经加载到内存了，下一次导入直接引用内存中导入的结果
# import spam #m1=111111
# import spam #m2=m1
# import spam
# import spam
# import spam
# import spam

# import sys,spam
# print('spam' in sys.modules)
# print(sys.modules)


#import 导入文件都做了哪些事？
#1 以源文件为准产生一个名称空间
#2 以刚刚产生的名称空间为准，执行源文件的代码
#3 会在当前文件中定义一个名字，这个名字就是模块名，用来引用模块中的名字
# import spam
# # money=0
# # def read1():
# #     print('from ------>')
# # read1()
# # spam.read1()
# # spam.read2()
#
#
# money=1000000000
# spam.change()
# # print(money)
# spam.read1()


#为模块起别名
# import spam as sm
#
# print(sm.money)



# engine_type='mysql'
# if engine_type == 'mysql':
#     import mysql as engine
# elif engine_type == 'oracle':
#     import oracle as engine
#
# engine.parse()



#在一行导入多个模块
import spam,time




##第一部分：from...import...

# from spam import money,read1,read2,change
# money=1
# print(money)
# read1()
# def read1():
#     print('==32222=>?')
#
# read1()
#
# read2()
#
# change()
# print(money)


# from spam import *
# print(money)
# print(read1)
# print(read2)
# print(change)

# from spam import * # * 对应模块spam内的__all__属性
# # print(money)
# # print(read1)
# print(read2)

# from spam import money,read1,read2,change
#
# import importlib
#
# importlib.reload()


import spam





模块文件名如果包含空格，或者以数字开头的模块文件名，在导入时候会报错。
发现可以用‘_import__‘方法。把__import__的返回值当做模块使用就能完美解决此类问题。
abc = __import__("12-12 abc")









