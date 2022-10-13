# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

'''
是一种设计模式，具体就是一个类中始终只有一个实例存在，
方法：
1.使用模块
2.使用__new__
3.使用装饰器
4.使用元类
'''

# 两种写法：第一种
# class Foo:
#     __instance=None
#     def __new__(cls, *args, **kwargs): # 这时候不能使用__init__方法，因为只有在实例过后才会有 init 方法
#         if cls.__instance is None:
#             cls.__instance=super(Foo, cls).__new__(cls,*args,**kw)
#         return cls.__instance
#     def __init__(self,number):
#         self.number=number
#
#
# s1=Foo(6)
# s2=Foo(9)
# print(s1 == s2)
# print(s1 is s2)
# print(s1.number)
# print(s2.number)


# 第二种：

class Foo:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=object.__new__(cls,*args,**kwargs)
        return  cls._instance


one=Foo()
two=Foo()


# 下面这种演示方式是有问题的，因为这实际上是修改了属性值
one.a=1
print(one.a)
two.a=4
print(two.a)


# 这才是真正可以获取的结果。
print(one==two)
print(one is two)



# 总结：
# 单例模式是一种设计模式，是在面试的时候用。

