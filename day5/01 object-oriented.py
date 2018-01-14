# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 基本的面向对象的例子:


def person(attack, life_value, name, level):
    def atk(dog_d):
        print('%s 打了 %s' % (name, dog_d['name']))
        dog_d['life_value'] -= attack

    person_dic = {
        'attack': attack,
        'life_value': life_value,
        'name': name,
        'level': level,
        'atk': atk
    }
    return  person_dic

def dog(attack, life_value, name, level):
    def bite(person_d):
        print('%s 咬了 %s' % (name, person_d['name']))
        person_d['life_value'] -= attack

    dog_dic = {
        'attack': attack,
        'life_value': life_value,
        'name': name,
        'level': level,
        'bite': bite,
    }
    return  dog_dic

alex=person(100,1000,'alex',2)
wangcai=dog(200,2000,'wangcai',5)

alex['atk'](wangcai)
wangcai['bite'](alex)
wangcai['bite'](alex)
wangcai['bite'](alex)
wangcai['bite'](alex)

print('%s的生命值现在是：%d' %(alex['name'],alex['life_value']))
print('%s的生命值现在是：%d' %(wangcai['name'],wangcai['life_value']))





# 类： 面向对象编程

# 类的定义：
# class Person: # 可以不加括号
#     role='人'            # 数据属性、静态属性
#     country='中国'
#     def __init__(self,name,age,life_value):  # 初始化操作
#         # 这个 self 是对象本身，是不可变的。
#         self.name=name
#         self.theage=age
#         self.life_value=life_value
#         self.aggression=200
#     def attack(self):    # 函数属性、动态属性， 在类里面的函数称为方法
#         # 这个 self 是个形式参数，因为调用的时候就已经指定对象了。
#         print('attact 方法被 %s 执行了' %(self.name))

# Person()  # 类名加() 就是实例化一个对象，然后这个这个对象没有没有名字，并且类中的代码已经被执行。
# print(Person.role)
# print(Person.__dict__['role'])  # 不可修改及删除，是经典类的方法


# alex=Person()
# 类加上（）的过程：  实例化的过程
# 1.先创建一个对象，{}
# 2.执行__init__方法，同时把创建的对象扔到__init__参数里
# print(alex.role)

# alex.name='alex'  # 给对象添加对象
# alex.age=19
# print(alex.name,alex.age)
# alex.__dict__['name']='aaaa'   # 新式类这个字典属性内容是可以修改的，
# print(alex.name,alex.age)
#
# egon=Person()
# egon.name='egon'
# print(egon.name,egon.age)
#
#
# Person.name  # 一般不用类名调对象的方法



#  标准实例化
# alex=Person('alex',28,2000)
# egon=Person('egon',18,1000)
# Person.attack(alex)  # 类可以查看动态属性，却必须加上具体的的对象参数才能调用
# Person.attack(egon)

# 对象可以拥有自己的属性，并且可以调用类中的方法、

# alex.attack() # == Person.attack(alex)  # 真正使用方法的不是类而是对象，
# egon.attack() # ==Person.attack(egon)



# class Dog:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type # 将传入的值和对象属性进行了绑定，否则是没有值的
#         self.life_value=2000
#
#
#     def bite(self,name):
#         print('% 咬了 $s' %(self.name,name))
#
#
# 旺财=Dog('旺财','土豆')
# 使用 init 方法进行属性的初始化
# 1.规范所有对象都拥有的一些属性
# 2.方便，可以拥有自己的属性和对象，







# 练习：

class Dog:
    counter=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.counter+=1


史努比 = Dog('史努比','大白狗')
史努比2 = Dog('史努比','大白狗')
print(史努比.counter)
print(史努比2.counter)


# 思路：
# 将一个实例抽象成一个类，并且确定方法

# from math import  pi
#
# class Circle:
#     def __init__(self,r):
#         self.r=r
#
#     def area(self):
#         return  self.r**2*pi
#
#     def perimeter(self):
#         return self.r*2*pi
#
# c1=Circle(4)
# print(c1.area())
# print(c1.perimeter())
#
# c2=Circle(8)
# print(c2.area())
# print(c2.perimeter())






class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def action(self,act):
        print('%s,%s岁，%s，%s' %(self.name,self.age,self.sex,act))


xiaoming=Person('xiaoming',10,'男')
print(xiaoming.name)
xiaoming.action('上山砍材')
xiaoming.action('开车去东北')

xiaoli=Person('xiaoli',20,'男')
xiaoli.action('打了小明')
