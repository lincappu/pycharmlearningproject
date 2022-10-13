# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 一.首先，凡是类中的方法或者函数，默认都是绑定给对象使用的，
# 1.正常情况：
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk(self): # 这个方法，
#         pass
#
# p=Person('egon',18)
# print(p.talk)   # <bound method Person.talk of <__main__.Person object at 0x107aca5c0>>

# 2.去掉 self 的情况
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk():  # 这个叫做函数
#         pass
#
# p=Person('egon',18)
# print(p.talk)  #  <bound method Person.talk of <__main__.Person object at 0x10a403588>>

# 表明：不管类中的方法还是函数，默认都是绑定给对象使用的，好处就是不用手动传参，

# 3.类名和对象名调用方法的区别:
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk():  # 这个叫做函数
#         pass
#
# p=Person('egon',18)
# print(Person.talk)  # <function Person.talk at 0x1052f56a8>
# print(p.talk)  # <bound method Person.talk of <__main__.Person object at 0x1052f15c0>>

# 结论：正常情况下，如果有类名调用方法，talk 方法就是一个普通的函数，既然是函数就不会有自动传值这一说。


# 4.通过类名和对象名执行方法的结果：
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk(self):  # 这个叫做方法
#         print('传入的参数是：%s' %(self))
#
# p=Person('egon',18)
# # Person.talk()  # 报错
# p.talk()
# Person.talk(3432) # 这才是正确的，这个参数必须要传

# 结论：正常情况下，类中方法是需要一个参数的，当通过类名去调用的时候是不会自动传入参数的，而通过对象名去调用的是会自动传入一个参数的，就是对象本身

# 5.相反的情况：
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk():  # 这个叫做函数
#         pass
#
# p=Person('egon',18)
# Person.talk()  # 正常，
# p.talk()  # 报错
# 结论：talk 这时候一个函数，而且没有参数，但是这个函数是绑定给对象 p 了，所以对象 p 在执行函数的时候自动传入了一个参数，self 就报错。



# 结论：
# 1.凡是类中方法和函数，都是默认自动绑定给对象使用的
# 2.实例名.方法 调用时会有自动传惨的功能，传进去的是对象本身
# 3.如果类要想调用绑定方法，就必须遵循函数的参数原则，有几个参数，就必须传几个参数。
# 4.实例名无法使用函数，因为调用实例名会自动传入一个参数，无


# 二、类的绑定方法：
# 1.通过 classmethod将方法绑定到类上，而不是对象上。
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @classmethod
#     def talk(self):
#         pass
#
# p=Person('egon',18)
# print(Person.talk)  # <bound method Person.talk of <class '__main__.Person'>>
# print(p.talk)  # <bound method Person.talk of <class '__main__.Person'>>
#
# Person.talk()
# p.talk()

# 结论：通过 classmethod将方法绑定到类上时，特殊的在于当使用对象名调用的时候，也会自动将类名传进入，所以不报错。

# 2.没有参数时：
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @classmethod
#     def talk():
#         pass

# p=Person('egon',18)
# print(Person.talk)  # <bound method Person.talk of <class '__main__.Person'>>
# print(p.talk)  # <bound method Person.talk of <class '__main__.Person'>>
#
# Person.talk()  # 报错
# p.talk() # 报错

# 结论：当将方法绑定到类名上时，无论是对象还是类名调用都会传对象名，但是这个方法其实是个函数没有参数，所以会报错。


# 三、类的非绑定方法：
# 1.使用 staticmethod将方法解除绑定，
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @staticmethod
#     def talk():
#         pass
#
# p=Person('egon',18)
# print(Person.talk)  # <function Person.talk at 0x1031e56a8>
# print(p.talk)   # <function Person.talk at 0x1031e56a8>
#
# Person.talk()  # 正确
# p.talk()   # 正确

# 结论：当是非绑定方法时，就是普通函数，不会自动传参。




# 练习：
# import settings.py
# import uuid
# import pickle
# import os
#
#
# class Mysql():
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.id = self.create_id()
#
#     def save(self):
#         if self.check:
#             raise PermissionError('对象已存在')
#         file_path = (r'%s%s%s' % (settings.py.DB_PATH, os.sep, self.id))
#         pickle.dump(self, open(file_path, 'wb'))
#
#     @property
#     def check(self):
#         tag = False
#         files = os.listdir(settings.py.DB_PATH)
#         for file in files:
#             file_abspath = r'%s%s%s' % (settings.py.DB_PATH, os.sep, file)
#             obj = pickle.load(open(file_abspath, 'rb'))
#             if self.host == obj.host and self.port == obj.port:
#                 tag = True
#         return tag
#
#     @staticmethod
#     def create_id():
#         return uuid.uuid1()
#
#     @staticmethod
#     def get_obj_by_id(id):
#         file_path = r'%s%s%s' % (settings.py.DB_PATH, os.sep, id)
#         return pickle.load(open(file_path, 'rb'))
#
#     @classmethod
#     def by_conf(cls):
#         return cls(settings.py.HOST, settings.py.PORT)
#
#
# conn = Mysql('192.168.1.1', '3306')
# print(conn.id)
# conn.save(
# res=conn.get_obj_by_id('1d2aa97e-fbec-11e7-9111-acbc32a4b6d5')
# print(res.host,res.port)

# conn.save()

# conn1 = Mysql.by_conf()     #  调用方式一致
# print(conn1)

# obj = Mysql.get_obj_by_id('1d2aa97e-fbec-11e7-9111-acbc32a4b6d5')
# print(obj.host)
# print(obj.port)
