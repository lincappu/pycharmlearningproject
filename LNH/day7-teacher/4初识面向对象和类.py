# def
# 面向过程编程
# 固定的目的 固定的结果
# 从头到尾把要执行的步骤堆积出来就好了
# 面向对象编程
# 有一个抽象的过程
# 上帝视角：结果不能预测
'''
class Person:
    rol = '人'         #数据属性、静态属性
    country = '中国'
    def attack(self):  #函数属性、动态属性、方法
        pass

# person 类 Person也是类名
print(callable(Person))
print(Person())   #对象
#一个类名加上括号就会返回一个对象
print(Person.rol)  #.属性名
Person.rol = '人类' #修改属性的值
print(Person.__dict__)  #不可以平时直接用的
#类也有一个属于自己的名称空间：静态属性和动态属性
print(Person.attack)
# print(Person.attack())  报错：没有self参数
'''


# 类的定义
# class 类名:
#     静态属性 = '值'
#     def 方法(self):
#         pass
#
# 对象 = 类名()
# 对象.静态属性
# 对象.方法 #可以调用不能执行



# class Person:
#     role = '人'  # 数据属性、静态属性、类属性
#     country = '中国'
#
#     '''
#     nihao
#     '''
#
#     def __init__(self, name, age, life_value):  # 初始化方法
#         # self.__dict__['name'] = name
#         self.name = name  # 属性、对象属性
#         self.theage = age
#         self.life_value = life_value
#         self.aggr = 200
#
#     def attack(self):  # 函数属性、动态属性、方法
# self只是一个形式参数，可以叫其他名字，但正常没人会这样
# self是水性杨花，那个对象调这个方法，self就是那个对象
# print('attack方法被%s执行了' % self.name)

# alex = Person('alex',38,2000)  #alex 对象
# print(alex.name)
# print(alex.theage)
# print(alex.life_value)
# print(alex.role)
# print(alex.country)

# print(Person.__name__)
# print(Person.__doc__)
# print(Person.__dict__)
# print(Person.__class__)




# 类加上括号的过程：  #实例化
# 1.先创建了一个对象 self = {}
# 2.才执行初始化方法__init__,同时把创建的对象扔到了__init__参数里


# Person.role
# alex.name = 'alex'   #给alex对象创建一个属性
# print(alex.name)     #查看alex的name属性
# alex.name = 'Alexander' #修改alex的name属性
# print(alex.name)     #查看alex的name属性
# print(alex.__dict__['name'])
# alex.__dict__['name'] = 'alex'  #对象可以使用dict来修改属性的值
# print(alex.name)
# alex.age = 38
# print(alex.age)
# print(alex.__dict__)
# egg = Person()
# egg.name = 'egon'
# print(egg.name)
# print(alex.name)

# 类 对象(实例) 实例化
# 类是我们自己抽象出来的
# 实例化 对象 = 类名()
# 类经过实例化就产生了对象/实例


# alex = Person('alex',38,2000)  #alex 对象
# egg = Person('egon',18,1000)  #alex 对象
# 真正使用方法的不是类而是对象
# Person.attack(alex)
# Person.attack(egg)
# alex.attack()  #==Person.attack(alex)
# egg.attack()    #==Person.attack(egg)

# 类：静态属性 动态属性
# 类可以调用静态属性
# 类可以查看动态属性 却必须要带上具体的对象参数才能调用动态属性

# 对象：可以拥有自己的对象属性，并且可以调用类中的方法

# 对象可以调用类的方法么
# class Person:
#     rol = '人'  # 数据属性、静态属性、类属性
#     country = '中国'
#
#     def __init__(self, name, age, life_value):  # 初始化方法
#         # self.__dict__['name'] = name
#         self.name = name  # 属性、对象属性
#         self.theage = age
#         self.life_value = life_value
#
#         return None  # init 方法不能返回任何东西。

# def attack(self):  # 函数属性、动态属性、方法
# self只是一个形式参数，可以叫其他名字，但正常没人会这样
# self是水性杨花，那个对象调这个方法，self就是那个对象
# print('attack方法被%s执行了' % self.name)



# egg = Person('egon',18,1000)
# alex = Person('alex',38,2000)
# print(alex.rol)
# print(alex.country)
# egg.aggr = 200
# alex.country = '印度'
# print(alex.country)
# print(egg.country)

# 类有属于自己的命名空间
# 对象也是
# 类不可以调用对象的属性
# 但是对象在寻找属性的时候，是先找自己名称空间的，找不到就找类名称空间里的

# class Dog:
#     def __init__(self, name, type):
#         self.name = name
#         self.dog_type = type
#         self.life_value = 2000
#
#     def bite(self, name):
#         print('%s咬了%s' % (self.name, name))
#
#
# 旺财 = Dog('旺财', '土狗')


# 使用init去进行属性的初识化
# 1.规范所有的对象都拥有一些基础的属性
# 2.方便

# print(旺财.name)
# print(旺财.dog_type)
# print(旺财.life_value)
# 旺财.bite('alex')   #Dog.bite(旺财,'alex')
# __init__再讲

# 再讲类中的方法


# 练习
# 创建一个类,实例化对象，需要做一个计数器，这个类每实例化一次，计数器加一
# 所有的对象共享这个计数个数
# class Dog:
#     counter = 0
#     def __init__(self,name,type):
#         self.name = name
#         self.dog_type = type
#         self.life_value = 2000
#         Dog.counter += 1
#
# 史努比 = Dog('史努比','大白狗')
# 史努比2 = Dog('史努比','大白狗')
# print(史努比.counter)
# print(史努比2.counter)



# 练习2
# 创建一个圆形类
# 有一个属性：圆的半径
# 提供两个方法：计算圆面积 、计算圆周长
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#
#     def area(self):
#         return self.r**2*pi
#
#     def perimeter(self):
#         return 2*pi*self.r
#
# c1 = Circle(5)
# print(c1.area())
# print(c1.perimeter())
# c2 = Circle(20)
# print(c2.area())
# print(c2.perimeter())


# 练习 3
# 在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健

# 两个人物 --》 人类
# 姓名 年龄 性别   ---》属性
# 行为  --> 方法
# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def shangshan(self):
#         print('%s,%s岁,%s,上山去砍柴' % (self.name, self.age, self.sex))
#
#
# xiaoming = Person('小明', 10, '男')
# old_li = Person('老李', 90, '男')
# xiaoming.shangshan()
# old_li.shangshan()

# 面向过程和面向对象编程
# 思路1 从只关心某一个对象变成抽象规范了一类对象
# 思路2 当多个函数都需要传递同样的多个参数的时候，考虑面向对象的思想

# 面向对象作业
# 1.正方形类





# 知识点：为类动态添加方法：
class CLanguage :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    def __init__(self,name,add):
        #下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name,"网址为：",add)
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)

# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("C语言中文网","http://c.biancheng.net")



# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对clanguage的foo方法赋值（动态绑定方法）
clanguage.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
clanguage.foo(clanguage)  # ①
# 使用lambda表达式为clanguage对象的bar方法赋值（动态绑定方法）
clanguage.bar = lambda self: print('--lambda表达式--', self)
clanguage.bar(clanguage) # ②

# 上面的第 5 行和第 11 行代码分别使用函数、lambda 表达式为 clanguage 对象动态增加了方法，但对于动态增加的方法，Python 不会自动将方法调用者绑定到它们的第一个参数，因此程序必须手动为第一个参数传入参数值，如上面程序中 ① 号、② 号代码所示。
# print(clanguage.foo())



# 借助 types 模块下的 MethodType自动给 self 传值
from  types import MethodType
def info(self,content):
    print('111111  %s' %content)

clanguage.info=MethodType(info,clanguage)

clanguage.info('22222')








self就是指定那个初始化类的那个的实例对象











