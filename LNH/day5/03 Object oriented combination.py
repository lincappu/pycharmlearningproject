# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 面向对象的组合：
# 就是面向对象的属性就是也是一个面向对象，反映的是一种所属关系。

# class Bithrday:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
#
# class Person:
#     def __init__(self,name):
#         self.name=name
#
# alex_birth=Bithrday(1980,1,20)
# print(alex_birth.year)
#
# alex=Person('alex')
#
# alex.birth=alex_birth  # 一个对象的属性是另一个对象。
#
# print(alex.birth.year)

# 两个对象之间的关系，所属关系



# 人狗大战的组合例子：
# 人有武器

# class Weapon:
#     def __init__(self,name,aggr,money):
#         self.name=name
#         self.aggr=aggr
#         self.money=money
#
#     def kill(self,dog_obj):
#         print('%s 武器攻击了 %s，伤害%s' %(self.name,dog_obj.name,self.aggr))
#         dog_obj.life_value-=self.aggr
#
# class Dog:
#     def __init__(self,name,type,aggr):
#         self.name=name
#         self.type=type
#         self.aggr=aggr
#         self.life_value=2000
#
#     def bite(self,person_obj):
#         print('%s 咬了 %s' %(self.name,person_obj.name))
#         person_obj.life_value -= self.aggr
#
# class Person:
#     def __init__(self,name,age,life_value):
#         self.name=name
#         self.age=age
#         self.live_value=life_value
#         self.aggr=10
#
#     def attack(self,dog_obj):
#         print(' %s 打了 %s'%(self.name,dog_obj.name))
#         dog_obj.life_value-=self.aggr
#
#
# alex=Person('alex',38,2000)
# egon=Dog('egon','土狗',1000)
#
# alex.money=10000
# knife=Weapon('大刀',100,200)
#
# if alex.money >= knife.money:
#     alex.money-=knife.money
#     alex.weapon=knife
#
# print(alex.money)
# alex.weapon.kill(egon)
# print(egon.life_value)







