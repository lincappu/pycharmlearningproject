# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 继承的关系：

# class Animal:
#     def __init__(self,name,aggr,life_value):
#         self.name=name
#         self.aggr=aggr
#         self.life_value=life_value
#
#     def func(self):
#         print(self.name)
#
#
# class Foo:
#     def func(self):
#         print(self.name)
#
#
# class Person(Animal,Foo):
#     def __init__(self,name,aggr,life_value,money):
#         Animal.__init__(self,name,aggr,life_value)
#         self.money=money   # 派生属性
#
# class Dog(Animal,Foo):
#     def __init__(self,name,aggr,life_value,type):
#         # Animal.__init__(self,name,aggr,life_value)
#         super().__init__(name,aggr,life_value)    # super 的方式，可以不用传 self。
#         self.type=type  # 派生属性
#     def bite(self,person_obj):  # 派生方法
#         print('%s 咬了 %s' %(self.name,person_obj.name))
#
#
# egon=Dog('egon',100,1000,'土狗')
# alex=Person('alex',200,2000,10000)
#
# print(egon.__dict__)
# print(alex.__dict__)
#
# print(Person.__bases__)
# print(Dog.__bases__)
#
# alex.func()
# egon.func()
#
# egon.bite(alex)


# 继承的第二个例子:
# class Person:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Courses:
#     def __init__(self,name,period,price):
#         self.name=name
#         self.perion=period
#         self.price=price
#
#     def tell_info(self):
#         print('课程：%s  周期是:%s  价格是：%s' %(self.name,self.perion,self.price))
#
#
# class Teachers(Person):
#     def __init__(self,name,age,sex,title):
#         Person.__init__(self,name,age,sex)  # 指名道姓的方法，继承也能使用父类的方法，但是无法使用父类的方法。
#         self.title=title
#         self.courses=[]
#         self.students=[]
#
#
# class Students(Person):
#     def __init__(self,name,age,sex,):
#         Person.__init__(self,name,age,sex)
#         self.course=[]
#
#
#
# egon=Teachers('egon',18,'男','讲师')
# fls=Students('fls',27,'男')
# python=Courses('python','4个月',9900)
# linux=Courses('linux','5个月',18000)
#
# print(Teachers.__base__)


# egon.students.append(fls)
# egon.courses.append(python)

# fls.course.append(python)
# fls.course.append(linux)


# for obj in  egon.courses:
#     print('egon 老师教授的课程情况')
#     obj.tell_info()
#
# for obj in fls.course:
#     print('fls学生所学的课程情况')
#     obj.tell_info()




# class Person:   #定义一个人类
#     role = 'person'  #人的角色属性都是人
#     def walk(self):  #人都可以走路，也就是有一个走路方法
#         print("person is walking...")
#
#
# print(Person.role)   #查看人的role属性
# print(Person.walk)   #引用人的走路方法，注意，这里不是在调用
# print(Person.walk()) #这时在调用


# 面向对象的第三个例子：方法的调用关系，顺序
# class Teacher:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.teach()     # 这个方法在实例化的过程中被执行，按照子类-父类的调用顺序执行。
#
#     def teach(self):
#         print('%s 正在讲课' %(self.name))
#
# class Professor(Teacher):
#     def write(self):
#         print('%s 正在写作' %(self.name))
#
#     def teach(self):
    # 当子类的所有参数都是父类的参数时，可以不写子类的 init方法，就用父类的方法进行实例化
    # 父类的 self 就是子类中的数理化对象，所以在父类中调用 teach() 其实就是调用alex.teach()方法，所以优先从子类中查找。子类没有的才会在父类中找
    #     print('%s 在教书' %(self.name))

# alex=Professor('alex',38,10000)
# print(Teacher.__bases__)
# print(alex.teach())

# print(Professor.mro())



# 新式类的多继承：python3中只有广度优先的算法， python2经典类中有深度优先。




