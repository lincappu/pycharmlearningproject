#人狗大战
class Dog:
    def __init__(self,name,type,aggr):
        self.name = name
        self.dog_type = type
        self.aggr = aggr
        self.life_value = 2000

    def bite(self,person_obj):  #self==egg,person_obj=alex
        #属性的变化
        print('%s咬了%s'%(self.name,person_obj.name))
        person_obj.life_value -= self.aggr

class Person:
    rol = '人'         #数据属性、静态属性、类属性
    country = '中国'
    def __init__(self,name,age,life_value): #初始化方法
        self.name = name       #属性、对象属性
        self.theage = age
        self.life_value = life_value
        self.aggr = 1

    def attack(self,dog_obj):  #函数属性、动态属性、方法
        print('%s攻击了%s'%(self.name,dog_obj.name))
        dog_obj.life_value -= self.aggr

alex = Person('alex',38,500)
egg = Dog('egon','二哈',20)
print(alex.life_value)
egg.bite(alex)   #Dog.bite(egg,alex)
print(alex.life_value)
print(egg.life_value)
alex.attack(egg)
print(egg.life_value)

#类的定义
#对象
#实例化
#交互


