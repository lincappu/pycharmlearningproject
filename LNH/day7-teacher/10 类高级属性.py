# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# isinstance和issubclass
# isinstance(obj, cls)
# 检查是否obj是否是类cls的对象


# class Foo(object):
#     pass
#
# obj = Foo()
# print(isinstance(obj, Foo))



# issubclass(sub, super)
# 检查sub类是否是super类的派生类，其实就是检查是不是就是子类

# class Foo(object):
#     pass
#
# class Bar(Foo):
#     pass
#
# print(issubclass(Bar, Foo))




# 2、反射，自省
# 通过字符串的方式操作函数的相关属性，python 的一切都是对象，都可以用来反射。
# hasattr()
# getattr()
# setattr()
# delattr()


# class Foo:
#     f = '类的静态变量'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say_hi(self):
#         print('hi,%s'%self.name)
#
#
# obj=Foo('egon',73)


# print(hasattr(obj,'name'))
# print(hasattr(obj,'say_hi'))
#
#
# n=getattr(obj,'name')
# print(n)
# func=getattr(obj,'say_hi')
# # func()

# setattr(obj,'sb',True)
# setattr(obj,'show_name',lambda self:self.name+'sb')
# print(obj.__dict__)
# print(obj.show_name(obj))
#
#
# print(obj.__dict__)




# 2
# class Foo(object):
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# print(getattr(Foo, 'staticField'))
# print(getattr(Foo, 'func'))
# print(getattr(Foo, 'bar'))
#







# 反射当前模块

# import sys
#
#
# def s1():
#     print('s1')
#
#
# def s2():
#     print('s2')
#
#
# this_module = sys.modules[__name__]
#
# print(hasattr(this_module, 's1'))
# print(getattr(this_module, 's2'))



 # 下划线方法：

# class ClassA(object):
#     def __init__(self, classname):
#         self.classname = classname
#
#
# a=ClassA('fls')

# print(a.age)  # 如果没有定义__getattr__方法，他就会在实例和基类中找，找不到就报错。
# print(a.__dict__)
# print(ClassA.__dict__)  # 基类中dic 中包含下划线方法

# 如果实例和基类中都没有才会调用__getattr__
# class ClassA(object):
#     def __init__(self, classname):
#         self.classname = classname
#
#     def __getattr__(self, item):
#         self.item=item  # 不能这样使用，会出现无限循环，只是 pycharm 屏蔽了
#         print(item)
#         return ('__getattr__',item)
#
#
# a=ClassA('fls')
#
#
# print(a.age)  # 如果定义了__getattr__方法， 当 age 在实例和基类中都没有的时候，这个方法就会被执行，同时接到这个attr参数，
# print(hasattr(a,'age'))
# # print(setattr(a,'age',18))
# print(setattr(ClassA,'age',18))
#
#
#
# print(a.__dict__)
# print(ClassA.__dict__)



# __getattribute__方法，不管对象中有没有找到对应的属性，都会调用这个方法

# class ClassA(object):
#     def __init__(self, classname):
#         self.classname = classname
#
#     def __getattr__(self, attr):
#         return ('invoke __getattr__', attr)
#
#     def __getattribute__(self, attr):
#         return ('invoke __getattribute__', attr)
#
#
# a=ClassA('flsr')
#
# print(a.classname)
#
# print(a.age)




#  __setattr__ 方法




# __str__  方法： 打印实例时会调用

# class Test(object):
#     def __init__(self, value='hello, world!'):
#         self.data = value
#
# t = Test()
# print(Test)
# print(t)    # 默认打印类的实例时，会打印实例所在的内存地址，


# class Test(object):
#     def __init__(self, value='hello, world!'):
#         self.data = value
#     def __str__(self):  # 这个方法一般都只有一个 return 语句,并且只能返回的是 str 类型
#         return  'str fangfa'
#
# t = Test()
# print(Test)
# print(t)   # 这时候打印的是定义的__str__方法返回的信息。



# __repr__方法：  打印类和实例时都会调用 适用于交互模式，其实 repr 方法还是会调用 str 方法
# class Test(object):
#     def __init__(self, value='hello, world!'):
#         self.data = value
#     def __str__(self):  # 这个方法一般都只有一个 return 语句,并且只能返回的是 str 类型
#         return  'str fangfa'
#     def __repr__(self):
#         return 'repr fangfa'
#
#
# t = Test()
# print(Test)
# print(t)



# item系列：
#
# class Foo:
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
#
# a=Foo('fla')
#
# a['age']=19
#
# print(a['age'])



#
# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init function')
#     def __new__(cls, *args, **kwargs):
#         print('in new function')
#         return object.__new__(A)
#
# a = A()
# # print(a.x)






class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __hash__(self):
        return hash(self.name+self.sex)

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True


p_lst = []
for i in range(84):
    p_lst.append(Person('egon',i,'male'))

print(p_lst)
print(set(p_lst))





