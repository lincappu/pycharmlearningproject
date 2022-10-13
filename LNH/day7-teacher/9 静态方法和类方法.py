# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 特性 property
# 特性是一种特殊的属性，访问它时会执行一段函数然后返回值
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     @property
#     def perimeter(self):
#         return math.pi * self.radius * 2
#
#
#
# c1=Circle(5)
# print(c1.area)
# print(c1.perimeter)

# c1.area=3  # 不能被赋值



# 静态方法：

# class T:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def static_test(a,b):   #  如果是类方法，这个地方第一个传的参数必须是 self。
#         print('static method %s %s' %(a,b))
#
#
# t=T()
#
# t.static_test(1,2)



import  time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    # @staticmethod
    def now(): #用Date.now()的形式去产生实例,该实例用的是当前时间
        t=time.localtime() #获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday) #新建实例并且返回
    # @staticmethod
    def tomorrow(): #用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

a=Date('1987',11,27) #自己定义时间
b=Date.now() #采用当前时间
c=Date.tomorrow() #采用明天的时间

# print(a.year,a.month,a.day)
# print(b.year,b.month,b.day)
# print(c.year,c.month,c.day)







# 类方法：

# class A:
#     x=1
#     @classmethod
#     def test(cls):
#         print(cls,cls.x)
#
# class B(A):
#     x=2
# B.test()





#__str__定义在类内部，必须返回一个字符串类型，
#什么时候会出发它的执行呢？打印由这个类产生的对象时，会触发执行

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '<name:%s,age:%s>' %(self.name,self.age)
#
# p1=People('egon',18)
# print(p1)
# str(p1) #----->p1.__str__()


import time
# class Date:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#
#     @staticmethod
#     def now():
#         t=time.localtime()
#         return Date(t.tm_year,t.tm_mon,t.tm_mday)
#
# class EuroDate(Date):
#     def __str__(self):
#         return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)


# 正常的情况：
# e=EuroDate(2019,2,20)
# e.now()
# print(e)

# 例外的情况：
# e=EuroDate.now()
# print(e)   # <__main__.Date object at 0x10dccd198>  这时候是 e 其实 Date 类



# 如何改变：
# import  time
#
#
# class Data:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#
#     @classmethod
#     def  now(cls):
#         t=time.localtime()
#         return cls(t.tm_year,t.tm_mon,t.tm_mday)
#
#
# class EuroData(Data):
#     def  __str__(self):
#         return 'year:%s month:%s day:%s' % (self.year, self.month, self.day)
#
# e=EuroData.now()
# print(e)


































