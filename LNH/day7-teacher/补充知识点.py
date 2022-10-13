# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 用方法来访问类属性：将类属性限制在类中使用
# class CLanguage:
#     #构造函数
#     def __init__(self,name):
#         self.name = name
#     #设置 name 属性值的函数
#     def setname(self,name):
#         self.name = name
#     #访问nema属性值的函数
#     def getname(self):
#         return self.name
#     #删除name属性值的函数
#     def delname(self):
#         self.name="xxx"
# clang = CLanguage("C语言中文网")
# #获取name属性值
# print(clang.getname())
# #设置name属性值
# clang.setname("Python教程")
# print(clang.getname())
# #删除name属性值
# clang.delname()
# print(clang.getname())

# 通过 property 函数来实现用直接用属性来调方法,通过方法来操作属性
# 属性名=property(fget=None, fset=None, fdel=None, doc=None)
# fget -- 获取属性值的函数
# fset -- 设置属性值的函数
# fdel -- 删除属性值函数
# doc -- 属性描述信息

# class CLanguage:
#     #构造函数
#     def __init__(self,n):
#         self.__name = n
#     #设置 name 属性值的函数
#     def setname(self,n):
#         self.__name = n
#     #访问nema属性值的函数
#     def getname(self):
#         return self.__name
#     #删除name属性值的函数
#     def delname(self):
#         self.__name="xxx"
#     #为name 属性配置 property() 函数
#     name = property(getname, setname, delname, '指明出处')
# #调取说明文档的 2 种方式
# #print(CLanguage.name.__doc__)
# help(CLanguage.name)
# clang = CLanguage("C语言中文网")
# # #调用 getname() 方法
# print(clang.name)
# # #调用 setname() 方法
# # clang.name="Python教程"
# # print(clang.name)
# # #调用 delname() 方法
# # del clang.name
# # print(clang.name)





# 为实例对象动态添加方法：且只能为实例对象添加实例方法
# class CLanguage:
#     pass
# #下面定义了一个实例方法
# def info(self):
#     print("正在调用实例方法")
# #下面定义了一个类方法
# @classmethod
# def info2(cls):
#     print("正在调用类方法")
# #下面定义个静态方法
# @staticmethod
# def info3():
#     print("正在调用静态方法")
# #类可以动态添加以上 3 种方法，会影响所有实例对象
# CLanguage.info = info
# CLanguage.info2 = info2
# CLanguage.info3 = info3
# clang = CLanguage()
# #如今，clang 具有以上 3 种方法
# clang.info()
# clang.info2()
# clang.info3()
# #类实例对象只能动态添加实例方法，不会影响其它实例对象
# clang1 = CLanguage()
# clang1.info = info
# #必须手动为 self 传值
# clang1.info(clang1)
#
#
# 在CLanguage类中指定了_slots__属性，这意味着，该类的实例对象仅限于动态添加
# class CLanguage:
#     __slots__ = ('name','add','info')
#
# 对于动态添加的方法，__slots__限制的是其方法名，并不限制参数的个数。








# 枚举类：
from  enum  import  Enum

class Color(Enum):
    red=1
    green=2
    blue=3































