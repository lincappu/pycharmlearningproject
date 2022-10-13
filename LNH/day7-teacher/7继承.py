#继承 —— 面向对象的三大特性之一
#想产生继承关系，必然是两个类以上
#继承表达的是一种 什么 是 什么的关系
# class Animal:
#     def __init__(self,name,aggr,life_value):
#         self.name = name
#         self.aggr = aggr
#         self.life_value = life_value
#
#     def func(self):
#         print(self.name)
#
# class Foo:
#     def func(self):
#         print(self.name)
#
# class Dog(Animal,Foo):
#     def __init__(self,name,aggr,life_value,type):
#         # # 下面三个是等价的
#         # Animal.__init__(self,name,aggr,life_value)
#         # super().__init__(name,aggr,life_value)
#         super(Animal,self).__init__(name,aggr,life_value)
#         self.dogtype = type    #派生属性
#
#     def bite(self):
#         #派生方法
#         Animal.func(self)
#         super().func()
#
# class Person(Animal):
#     def __init__(self,name,aggr,life_value,money):
#         Animal.__init__(self,name,aggr,life_value)
#         self.money = money
#
#     def attack(self):pass

# egg = Dog('egon',100,2000,'金毛')
# egg.bite()
# alex = Person('alex',100,2000,2000)
# # print(egg.__dict__)
# print(alex.__dict__)
# alex.func()
#Dog继承了Animal
#父类 ：Animal
#子类 ：Dog

#一个类可以有多个子类
#子类调用方法；先调自己的，自己没有就调用父类的
#写继承的过程：是先抽象，后继承
#派生：父类没有的属性和方法在子类中就是派生出来的


#多继承
#一个类可以拥有多个父类
# class A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass
#
# print(A.__base__)

#object  类祖宗
#如果一个类有指定的父类，那么他的父类就是被指定的那个
#如果一个类没有指定的父类，那么他的父类就是object
#凡是继承了object类的类都是新式类
#python3里所有的类都是新式类
#新式类调用父类的方法：
    # 指名道姓:父类名.方法名(self,aggr1...)；   ---->经典类
    # super关键字:super().方法名(aggr1,...)    ----> 只适用于新式类


#教授类
    #属性 年龄 姓名
    #行为 讲课 写专利
#教师类：
    #属性 年龄 姓名
    #行为 讲课
#教授是教师
#教师是父类/基类
#教授是子类

# class Teacher:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def teach(self):
#         print('%s正在讲课'%self.name)
#
# class Professor(Teacher):
#     def print_write(self):
#         print('%s正在写专利'%self.name)
#
# egon = Professor('egon',18,20000)
# print(egon.__dict__)
# print(egon.salary)
# egon.teach()
# egon.print_write()



# class Teacher:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.teach()   # 还是调用的是子类的那个Professor 的实例对象方法。
#
#     def teach(self):
#         print('%s正在讲课'%self.name)
#
# class Professor(Teacher):
#     def print_write(self):
#         print('%s正在写专利'%self.name)
#
#     def teach(self):
#         # super().teach()
#         print('教授%s正在讲课'%self.name)
#
# egon = Professor('egon',18,20000)
# egon.teach()
# print(egon.__dict__)
# print(egon.salary)
# egon.teach()
# egon.print_write()




#新式类多继承, 执行父类的方法是 广度优先
class A:
    def func(self):
        print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B):pass
    # def func(self):
    #     print('D')

class E(C):
    def func(self):
        print('E')

class F(D,E):pass
    # def func(self):
    #     print('F')

# f = F()
# f.func()

# 广度优先
# print(F.mro())


#经典类和新式类的区别
#1、关于基类 ： 新式类默认继承object
#2、关于在子类中执行父类的方法:新式类有super，经典类只能用指名道姓
#3、关于多继承：新式类 广度优先（mro），经典类：深度优先
#在py3没有经典类；在py2里经典类和新式类共存

#关于继承：
#子类继承父类
#子类的对象调用方法，优先在子类中找，如果子类中有，就执行子类中的，如果子类中没有，就执行父类的，多个父类以广度优先为准

#关注self到底是哪个类的实例化


# 模拟一个抽象类

import  abc

class All_file(metaclass=abc.ABCMeta):
    All_file='file'
    @abc.abstractclassmethod
    def read(self):
        pass

    @abc.abstractclassmethod
    def write(self):
        pass

class Txt(All_file):
    pass
    def read(self):
        print('read')
    def write(self):
        print('write')


t1=Txt()





# 多态
# 不同的子类对象调用相同的父类方法，产生不同的执行效果，可以增加代码的调用灵活度
# 多态   以 继承和 重写父类方法为基础
# 多态   是调用方法的技巧，不影响类的内部设计


# class Dog(object):
#     def work(self):
#         pass
#
#
#
# class Armdog(Dog):
#     def work(self):
#         print('armdog')
#
# class DrugDog(Dog):
#     def work(self):
#         print('drugdog')
#
#
# class Persion(object):
#     def work_with_dog(self,dog):
#         dog.work()
#
# p=Persion
# a=Armdog()
# p.work_with_dog(p,Armdog())















