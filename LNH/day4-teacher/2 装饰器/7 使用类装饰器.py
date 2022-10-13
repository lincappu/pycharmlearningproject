# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 1.常规写法的装饰器
#
# def cache(func):
#     data={}
#     def wrapper(*args,**kwargs):
#         key=key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
#         if key in data:
#           result = data.get(key)
#           print('cached')
#         else:
#             result=func(*args,**kwargs)
#             data[key]=result
#             print(data)
#             print('calculated')
#         return result
#     return wrapper
#
#
# @cache
# def rectangle_area(length, width):
#   return length * width
#
# a=rectangle_area(2,3)
# print(a)
#
#
# b=rectangle_area(2,3)
# print(b)



# 2  用类来编写 cache

# 类都是可调用对象，但是类的对象是否是可调用对象取决于是否定义__call__方法
class Cache:
    def __init__(self,func):
        self.func=func
        self.data={}

    def __call__(self, *args, **kwargs):   #
        func=self.func
        data=self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            self.data[key] = result
            print('calculated')
        return result
#
#
# @Cache   # 装饰的直接是函数， rectangle_area=Cache(rectangle_area)
# def rectangle_area(length, width):
#   return length * width
#
# a=rectangle_area(2, 3)
# print(a)


# 3 装饰器装饰器类的方法
# 用函数写的装饰器来装饰类的方法

#
# class Rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width
#   @cache   #  用函数装饰器是正常的，并且在调用方法的时候触发。
#   def area(self):
#     return self.length * self.width
#
#
#
# r = Rectangle(2, 3)
# print(r.area())


# 但是如果直接换成Cache类会报错，这个错误的原因是area被装饰后变成了类的一个属性，而不是方法。
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  @Cache  # 类装饰器来装饰
  def area(self):
    return self.length * self.width
r = Rectangle(2, 3)
r.area()











