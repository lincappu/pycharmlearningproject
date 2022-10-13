# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 一、什么是封装
# 在程序设计中，封装（Encapsulation）是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，其含义是其他程序无法调用。
# 要了解封装，离不开“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。

# 二、为什么要封装
# 封装数据的主要原因是：保护隐私（把不想别人知道的东西封装起来）
# 封装方法的主要原因是：隔离复杂度（比如：电视机，我们看见的就是一个黑匣子，其实里面有很多电器元件，对于用户来说，我们不需要清楚里面都有些元件，电视机把那些电器元件封装在黑匣子里，提供给用户的只是几个按钮接口，通过按钮就能实现对电视机的操作。）
# 提示：在编程语言里，对外提供的接口（接口可理解为了一个入口），就是函数，称为接口函数，这与接口的概念还不一样，接口代表一组接口函数的集合体。


# 封装的两个层面：
# 1.什么都不做
# 实例化对象就是封装， 类名.和实例名.  就是访问隐藏的接口

# 2.定义私有化方法，只在类的内部使用，外部无法访问，或者是只留下少量的接口供外部访问
# 类中所有双下划线开头的名称如_x都会自动变形成：_类名__x的形式

class A:
    __n=10
    def __init__(self):
        self.__x=1
    def __foo(self):
        print('foo')
    def bar(self):
        print('bar')

class B(A):
    def __init__(self):
        A.__init__(self)

    def coo(self):
        print('coo')

a=A()
print(a.__dict__)

a.__y=20
print(a.__dict__)

print(a._A__n)
print(a._A__x)

# a._A__foo()
# a.bar()
#
# b=B()
#
#
# print(b._A__n)



#  父类中的私有方法，子类不能进行重写
# 1.父类中没有私有化方法的情况，这时候 self 始终是子类的对象
# class A:
#     def __init__(self):
#         pass
#
#     def fa(self):
#         print('form A')
#
#     def test(self):
#         self.fa()
#
# class B(A):
#     def fa(self):
#         print('class A:
#     def __init__(self):
#         pass
#
#     def fa(self):
#         print('form A')
#
#     def test(self):
#         self.fa()
#
# class B(A):
#     def fa(self):
#         print('from B')
#
# b=B()
# b.test())
#
# b=B()
# b.test()   # from B


# 2.如果父类中有私有方法，那么子类在调父类方法时 self 是父类自己
# class A:
#     def __init__(self):
#         pass
#
#     def __fa(self):
#         print('form A')
#
#     def test(self):
#         self.__fa()
#
# class B(A):
#     def fa(self):
#         print('from B')
#
# b=B()
# b.test()  # from A


















