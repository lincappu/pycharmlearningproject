# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 类名和对象名都可以调用，区别在于：变量在哪个命名空间中，是在类中还是在实例中。

# class Person():
#     money=100
#
# sister=Person()
# father=Person()
# Person.money+=100
# Person.money+=100  # 不管是谁赚的钱都应该加到类名中，而不是对象中。
# print(Person.money)


# 动态属性就是方法，方法就是类中的函数，默认传一个 self
# 派生:派生方法、派生属性，就是父类中没有但子类中有的属性和方法。


# 一种特殊的写法：

# class A:
#     def func(self):
#         print('from 父类 A')
#
# class B(A):
#     def func(self):

        # super().func()   #  ==super(B,self).func() ==A.func(self)
        #这两种写法是完全等价的，在类中是可以省略的，
        # print('from 子类的 B')
# b=B()
# b.func()
# 在类外要使用指明使用的是哪个实例化对象来调用父类。  在类外调用子类的父类的方法，
# super(B,b).func()
# A.func('self')


# 面向对象的进阶：
# 1.多态：python 自带多态
# 定义：向不同的对象发送调用同一个函数，会产生不一样的动作，

# class Animal(object):
#     def talk(self):
#         pass
#
# class Person(Animal):
#     def talk(self):
#         print('say hello')
#
# class Dog(Animal):
#     def talk(self):
#         print('汪汪')
#
# class Cat(Animal):
#     print('喵喵')
#
# class Pig(Animal):
#     print('猪猪')
#
#
# person=Person()
# dog=Dog()
# cat=Cat()
# pig=Pig()
# person.talk()
# dog.talk()
# cat.talk()

# 上面是常规的方法，指名道姓法，直接使用名字去调用各自类的函数
# 下面体现的是多态的特性
# def func(obj):  # 这个其实等价于 def func(Animal obj):
#     obj.talk()
#
# func(person)
# func(dog)
# func(cat)
#这就实现了向不同的对象调用同一个函数，得到了不同的结果。
# 好处：
# 1.增加了程序的灵活性：使用者可以使用一种形式去调用，统一是 func(obj) 调用方式是一致的。
# 2.方便扩展，如果新加另一个类和对象，直接写代码即可，调用函数和调用方法并不变。
# func(pig)
#
# print(Pig.mro())  # 新式类的广度优先算法，是按照 mro 的顺序进行查找的。


#鸭子类型：
# 定义：如果是看起来向鸭子，叫声和走路鸭子，那么它就是鸭子
# 比如：list  tuple
#
# class A():
#     def pert(self):
#         print('A')
#
# class B(A):
#     def pert(self):
#         print('B')
#
# class C(A):
#     def pert(self):
#         print('C')
#
# class D(A):
#     pass
#
# class E():
#     def pert(self):
#         print('E')
#
# class F():
#     pass
#
#
# def test(obj):
#     obj.pert()
#
#
# a=A()
# b=B()
# c=C()
# d=D()
# e=E()
# f=F()
#
# test(a)
# test(b)
# test(c)
# test(d)
# test(e)
# test(f)


# print(D.mro())
# 这上面主要是 class E ，它并没有继承 class A，但是他的调用和其他是一致的，所以，多态关注的不是对象的类型，更关注的是对象的调用。
# a 就是 A 类型的，b 就是 B 类型的。
# 多态没有继承的关系：比如 str list tuple 他们的属性、方法、基本都是一样的，但是他们都是继承的 object 类，