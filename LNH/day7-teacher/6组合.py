# 组合 —— 面向对象的一种功能
# 什么有什么的关系
# 每个人都有生日,生日是由年月日组成
# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#         # self.birthday = birth
#
# alex_birth = Birthday(1968,1,1)
# print(alex_birth.year)
# alex = Person('alex')
# alex.birth = alex_birth   #Birthday类的对象是Alex的birth属性
# print(alex.birth.year)
# 组合 - 两个类之间的事儿
# 描述的是一种所属关系

# 组合例二：
# 人狗大战
# 人
# 武器：伤害、属性
# class Weapon:
#     def __init__(self,aggr,name,money):
#         self.aggr = aggr
#         self.name = name
#         self.money = money
#
#     def kill(self,dog_obj):
#         print('%s武器暴击%s,伤害%s'%(self.name,dog_obj.name,self.aggr))
#         dog_obj.life_value -= self.aggr
#
# class Dog:
#     def __init__(self, name, type, aggr):
#         self.name = name
#         self.dog_type = type
#         self.aggr = aggr
#         self.life_value = 2000
#
#     def bite(self, person_obj):  # self==egg,person_obj=alex
#         # 属性的变化
#         print('%s咬了%s' % (self.name, person_obj.name))
#         person_obj.life_value -= self.aggr
#
# class Person:
#     rol = '人'  # 数据属性、静态属性、类属性
#     country = '中国'
#
#     def __init__(self, name, age, life_value):  # 初始化方法
#         self.name = name  # 属性、对象属性
#         self.theage = age
#         self.life_value = life_value
#         self.aggr = 1
#
#     def attack(self, dog_obj):  # 函数属性、动态属性、方法
#         print('%s攻击了%s' % (self.name, dog_obj.name))
#         dog_obj.life_value -= self.aggr
#
# alex = Person('alex', 38, 500)
# egg = Dog('egon', '二哈', 20)
# alex.money = 2000
# knife = Weapon(200,'杀猪刀',1900)
# if alex.money > knife.money:
#     alex.money -= knife.money
#     alex.weapon = knife
#
# print(egg.life_value)
# alex.weapon.kill(egg)
# print(egg.life_value)



# 练习的例子
class Persion:
    role = '人'
    country = '中国'

    def __init__(self, name, age, life_value, money):
        self.name = name
        self.age = age
        self.life_value = life_value
        self.money = money
        self.aggr = 1

    def attack(self, dog):
        print('%s 攻击了 %s' % (self.name, dog.name))
        dog.life_value -= self.aggr


class Dog:
    def __init__(self, name, type, aggr):
        self.name = name
        self.type = type
        self.aggr = aggr
        self.life_value = 1000

    def bite(self, persion):
        print('%s 咬了%s ' % (self.name, persion.name))
        persion.life_value -= self.aggr


class Weapon:
    def __init__(self, name, price, hurt):
        self.name = name
        self.hurt = hurt
        self.price = price

    def buy(self, persion, num):
        total = int(self.price * num)
        if int(persion.money) < total:
            print('你的钱不够')
        else:
            print('%s 买了 %s %s 把' % (persion.name, self.name, num))
            persion.money  -= total
            persion.aggr+=self.hurt*num


alex = Persion('alex', 18, 1000, 1000)
d1 = Dog('haha', 'tugou', 100)
w1 = Weapon('gun', 20, 20)

alex.attack(d1)
print(d1.life_value)

w1.buy(alex, 5)

print(alex.money)
print(alex.aggr)

alex.attack(d1)
print(d1.life_value)

w1.buy(alex,200)

print(alex.money)