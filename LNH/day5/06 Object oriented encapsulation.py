# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# 封装==私有

# class A:
#     __COUNTRY='China'
#     def func(self):
#         print(A.__COUNTRY)  # 在内部调用是不受影响的，但其实是自动做了变形，
#
#     def __foo(self):
#         print('这是父类的私有方法')
#
#     def test(self):
#         self.__foo()
#
# class B(A):
#     def __foo(self):
#         print('这时子类的私有方法')



# print(a.__COUNTRY)    #  类外不能直接调用了，因为变形了
# print(A.__dict__)  # _A__COUNTRY
# print(A._A__COUNTRY)  # 使用变形之后的结果来调用，就没有问题，但是一般是不能这样调用的。双下方法并没有限制我们
# 使用私有的属性，但是，一般来说，这种方法调用是不允许的

# a=A()
# a.func()  #  这样就可以调用私有属性，

# 父类如果不想让子类覆盖自己的方法，就可以把方法设置为私有的。
# b=B()
# b.test()

# 1.正常情况下，如果没有私有方法，执行 b.test()，B 类中没有，就去 A 类中找，找到，执行 foo()方法，在自己的类
# 中找到，于是执行执行的是子类中的__foo()的方法，
# 2.如果有私有方法，子类去父类中找 test()后，执行的是 A._A__foo() 所以会在父类中执行，而不会执行子类的方法。



# 封装的目的：
# 1.封装数据：隐藏起对外操作的变量或者接口，然后对变量和接口做限制，从而完成对数据属性操作的要求

# 第一个例子：
# class Teacher:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#
#     def tell_info(self):
#         print('姓名：%s  年龄：%s' %(self.__name,self.__age))
#
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             raise  TypeError('姓名必须是字符串类型')
#         if not isinstance(age,int):
#             raise  TypeError('年龄必须是整型')
#
#         self.__name=name
#         self.__age=age
#
#
# alex=Teacher('alex',38)
# alex.tell_info()
#
# alex.set_info('alex',39)
# alex.tell_info()

# 第二个例子：
# class Goods:
#     __discount=0.8
#     def __init__(self,price):
#         print('价格：%s' %(price*self.__discount))
#
# apple=Goods(10)


# 2.封装方法：降低复杂度，屏蔽了接口的具体实现细节，只对外提供一个接口名称即可
# class ATM:
#     def __card(self):
#         print('插卡')
#     def __auth(self):
#         print('用户认证')
#     def __input(self):
#         print('输入取款金额')
#     def __print(self):
#         print('打印账单')
#     def __take_money(self):
#         print('取款')
#
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print()
#         self.__print()
#         self.__take_money()
# a=ATM()
# a.withdraw()



# 四、属性:property
# 表面上看它是一个方法，但是在调用的时候是听过属性的方式去调用
# 在property类中，有三个成员方法和三个装饰器函数。
# 三个成员方法分别是：fget、fset、fdel，它们分别用来管理属性访问；
# 三个装饰器函数分别是：getter、setter、deleter，它们分别用来把三个同名的类方法装饰成property。
# fget方法用来管理类实例属性的获取，fset方法用来管理类实例属性的赋值，fdel方法用来管理类实例属性的删除；
# getter装饰器把一个自定义类方法装饰成fget操作，setter装饰器把一个自定义类方法装饰成fset操作，deleter装饰器把一个自定义类方法装饰成fdel操作。
# 只要在获取自定义类实例的属性时就会自动调用fget成员方法，给自定义类实例的属性赋值时就会自动调用fset成员方法，在删除自定义类实例的属性时就会自动调用fdel成员方法。





# 例1：
# class Person:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height**2)
#
# egon=Person('egon',160,1.75)
# print(egon.bmi)

# 例2：
# import  math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     @property
#     def area(self):
#         return math.pi * self.radius**2
#
#     @property
#     def primeter(self):
#         return 2*math.pi*self.radius
#
#
# c=Circle(5)
# print(c.area)
# print(c.primeter)
#
# c.area=2  # 此时虽然调用的使用是按照属性进行调用的，但是是不能被赋值的。实质还是方法

# 特性的目的：
# 1.将类的函数定义为方法后，调用的时候就直接使用 obj.name 的形式去调用，统一的访问方式

# class Foo:
#     def __init__(self,val):
#         self.__name=val
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError('%s 必须是 str类型' %(value))
#         self.__name=value
#
#     @name.deleter
#     def name(self):
#         raise TypeError('不允许删除')
# 其实调用的是python 内置的__getattr__和__setattr__就是将方法变为属性功能的

# f=Foo(34)
# print(f.name)
# 注意：实例化的时候，其实是 get 方法，这个时候其实没有做限制的

# f.name=10
# 这个调用的是 set方法，这个才是调用的 name.setter 方法，才会做检查。
# del f.name
# 这个调用的 deleter 方法，也有限制。


# 进阶：
# class Foo:
#     def __init__(self,val):
#         self.__name=val
#
#     def getname(self):
#         return self.__name
#
#     def setname(self,value):
#         if not isinstance(value,str):
#             raise TypeError('%s 必须是 str类型' %(value))
#         self.__name=value
#
#     def delname(self):
#         raise TypeError('不允许删除')
#
# # 如果上述代码原来是这个样子，没有加装饰器，想编程装饰器的样子，但是不破坏原来代码的结构，做法：
#     name=property(getname,setname,delname)
#
# f=Foo('egon')
# print(f.name)
#
# f.name='alex'
# print(f.name)




# 另外一个 property 的例子：
# 半径和直径是有制约关系的，当修改其中一个的时候希望另外一个自动修改。
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def diameter(self):
#         return self.radius * 2
#
#     @diameter.setter
#     def diameter(self, newdiameter):
#         self.radius = newdiameter / 2
#
#
# c = circle(5)
# print(c.radius)
# print(c.diameter)
# c.diameter=4
# print(c.diameter)
# print(c.radius)






#
# import  uuid
#
# print(uuid.uuid1())
# print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))
# print(uuid.uuid4())
# print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))