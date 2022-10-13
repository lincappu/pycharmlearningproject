# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 1.isinstance() 和 issubclass()
# class Foo(object):
#     pass
#
#
# class Bar(Foo):
#     pass
#
#
# obj=Foo()
# print(isinstance(obj,Foo))
#
# print(issubclass(Bar,Foo))



# 2.反射(自省):通过字符串的形式操作对象的相关属性，python 的一切事物都是对象，都可以反射
# hasattr(object,str)
# getattr(object,str)
# setattr(object,str)
# delattr(object,str)


# 简单的例子：(类和对象中通过字符串来获取类中的属性和方法)
# class Person(object):
#     role='Person'
#     country='china'
#     def  __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def func(self):
#         print('%s in func' %(self.name))
#
#
#
#
# alex=Person('egon',80)
# # res=input('>>:').strip()
# if hasattr(alex,'func'):
#     # print(getattr(p,'func'))
#     func=getattr(alex,'func')
#     func()
# #
#
# alex.sex=None  # 原来的赋值方式
# setattr(alex,'sex','不详')  # setattr 的赋值方式
#
#
# def func2(self):
#     print('%s in func' % (self.name))
#
#
#
# print(func2)  #<function func2 at 0x10d2b6f28>
# print(func)  #<bound method Person.func of <__main__.Person object at 0x10d48e0b8>>
#
#
# setattr(alex,'func2',func2)
#
# alex.func2(alex)  # 方法就是一个普通的函数，不会自动传值，需要手动传值，所以这其实是一个伪方法。
#
# delattr(alex,'sex')  == del alex.sex  #(很少出现删除属性的情况。)





# 3.反射同样适用于模块。
import demo

# print(demo.a)  ==  print(getattr(demo,'a'))
# demo.test()  == getattr(demo,'test')()



# 4.反射当前模块成员：就是本模块和导入的模块都有一个同样的变量，默认反射的是导入的模块的变量，现在要反射本模块的变量

# a='aaaaa'
#
# import  sys
#
# this_modules=sys.modules[__name__]
# print(getattr(this_modules,'a'))


# 总结：
# 反射：a.b--> getattr(a,'b')
# hasattr,getattr,setattr,delattr
# python 一切皆对象，所以一切都可以反射。
# 类：静态属性，静态方法
# 对象：动态属性，动态方式
# 模块：变量，函数
# 本模块：函数，变量
# 场景：程序交互，文件交互，





# 4.类的内置方法

#
# class A:
#     def __call__(self, *args, **kwargs):
#         print('aaaa')
#
#
#
# a= A()
# a()  # 自动触发__call__ 方法的执行


#######__new__

# class A:
#
#     def __init__(self):  # 初始化方法
#         print('init 方法被执行')
#
#     def __new__(cls,*args,**kwargs):  # 构造方法
#         print('new方法被执行')
#         return  object.__new__(cls,*args,**kwargs)
#
# a=A()
# # 先执行构造方法，执行初始化方法

#
# class Myclass(object):
#     def __init__(self, x):
#         self.x = x
#
#
# c1 = Myclass(11)
# c2 = Myclass.__new__(Myclass, 12)  # new 的时候才需要一个实例名，或者说才需要接收一个实例名，
# print(hasattr(c2,'__new__'))  #True
# print(hasattr(c2,'__init__'))  #True
# print(c2.__dict__)  # 这个是空
# print(c1.x)
# print(c2.x)  #报错，提示c2 没有 x 属性，因为只调用了__new__  而没有调用__init__方法

# 解决方法：
# print(type(c2))
# Myclass.__init__(c2,12)   # 应该是这个写法，而不是下面这个写法，还是对很多东西应用的不深，很多关系都没有搞懂。
# c2=Myclass.__init__(c2,12)   # new 过的实例名已经注册到了类上，可以直接调用了。

# print(c2.x)




# __str__   __repr__  改变打印的格式。

# 1.常见的情况：
# class A:
#     def __init__(self,name='alex'):
#         self.name=name
#
# a=A()
# print(a)  # 默认打印的是函数的内存地址
# print(a.__str__())
# print(a.__repr__())
#
# # 下面来重构__str__  __repr__方法
# class A:
#     def __init__(self,name='alex'):
#         self.name=name
#
#     def __str__(self):
#         return 'str 方法--实例的名字是:'
#
#     def __repr__(self):
#         return  'repr 方法--实例的名字是:'
#
# a=A()
# # print(a)
# print('%s' %a)
# print('%r' %a)



# 结论：
# 1.str 是面对用户的，repr是面对程序的
# 2.先找 str 方法，在找 repr 方法。
# 3. %s查找顺序，有 str 就是 str，没有就是 repr
#    %r查找顺序，有 repr就 repr，没有就是内存地址
# 4.如果有一个就选 repr


# __len:__
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c=3
#
#     def __len__(self):
#         return len(self.__dict__)
# a = A()
# print(len(a))



# __hash__:
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def __hash__(self):
#         return hash(str(self.a)+str(self.b))
# a = A()
# print(hash(a))



# __eq__: 定义类的==行为。
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def __eq__(self,obj):
#         if  self.a == obj.a and self.b == obj.b:
#             return True
# a = A()
# b = A()
# print(a == b)  # 定义到了 == 的行为。都是构造方法。






# 纸牌游戏
# class  FranchDeck:
#     ranks=[ str(n) for n in range(2,11)] + list('AJKQ')
#     suits=['红桃','方块','黑桃','梅花']
#
#     def __init__(self):
#         self._cards=[(rank,suit) for rank in FranchDeck.ranks for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return  self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key]=value
#
#
# deck=FranchDeck()
# print(deck)
# import  random
# print(random.choice(deck))
# print(random.choice(deck))
#
#
# random.shuffle(deck)
# print(deck[0])
# print(deck[:5])




# 一道面试题: 去重，姓名和性别一致就认为是一个人。
#
# class Person:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def __hash__(self):
#         return hash(self.name+self.sex)
#
#     def __eq__(self, other):
#         if self.name==other.name and self.sex== other.sex:
#             return  True
#
# p_list=[]
# #
# for i in range(80):
#     p_list.append(Person('egon',i,'male'))
#
# print(p_list)
# print(set(p_list))
# print(list(p_list))
# 实现原理：
# 1.hash来确定元素在哪个桶中，通常是一个数组
# 2.新插入的元素根据 equals 方法来一次比较桶内的元素，确定是否存在。

# 在类中进行set会调用__eq__方法。完毕。