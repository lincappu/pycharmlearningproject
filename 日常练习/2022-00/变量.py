# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# ！！！全局变量：
a = 3
def Fuc():
    print (a)
    a = a + 1
Fuc()
这个就会出现未定义而使用的情况，因为Fuc里面的a会变成局部变量，如果要引用的是全局的那个a
a = 3
def Fuc():
    global  a
    print (a)
    a = a + 1
Fuc()
要首先申明称全局变量，才可以。但是main函数除外
a = 3
def Fuc():
    global a
    print (a)  # 1
    a = a + 1
if __name__ == "__main__":
    print (a)  # 2
    a = a + 1
    Fuc()
    print (a)  # 3
main 函数中不加global依然调用的全局变量。

类变量作为全局变量使用，定义一个类变量，然后用类名.来引用。

同样要注意事项变量绑定语句还是变量操作语句：
num = 100
def func():
    x = num + 100 这是一个变量操作语句，它会按照顺序进行查找num，最后会找到全局变量中的num，所以这个num是全局变量，不会报错。
    print(x)
func()





# ！！！类变量和实例变量：
# 实例变量是对于每个实例都独有的数据，而类变量是该类所有实例共享的属性和方法
# 实例一旦修改类变量，这个类变量就会自动进入实例的命令空间，会创建相同名称的变量，
# 如果是类自己修改了类变量，那么还在引用类变量的实例会对应变化。
# 在函数中如果啊要引用类变量要加 类名.属性 来引用，不过一般用的比较少。


class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name


d1 = Dog('1')
d2 = Dog('2')
d3 = Dog('3')

print(d1.kind)
print(d2.kind)
print(d3.kind)

print(d1.name)
print(d2.name)
print(d3.name)

d1.kind = '1'
print(d1.kind)
print(d2.kind)
print(Dog.kind)
Dog.kind = 'heklo'
print(d1.kind)
print(d2.kind)


# 是否会在实例上创建新的变量，关键是看是否是属性绑定语句还是属性操作语句，


# 这个就是属性绑定语句：
class Dog:
    kind = 'canine'   # 类变量也就是静态变量，定义在类中，并且没有在任何方法下面，不带self
    country = 'China'

    def __init__(self, name, age, country):  # 在init中定义的带sel发的变量都是实例变量也就是成员变量。
        self.name = name
        self.age = age
        self.country = country


dog = Dog('Lily', 3, 'Britain')
print(dog.name, dog.age, dog.kind, dog.country)  # Lily 3 canine Britain
print(dog.__dict__)  # {'name': 'Lily', 'age': 3, 'country': 'Britain'}

dog.kind = 'feline'
print(dog.name, dog.age, dog.kind, dog.country)  # Lily 3 feline Britain
print(dog.__dict__)
print(Dog.kind)  # canine 没有改变类属性的指向


# {'name': 'Lily', 'age': 3, 'country': 'Britain', 'kind': 'feline'}



# 下面救赎属性操作语句：
class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)  # 这个就是属性操作语句，操作的类属性，既所有实例都可以对这个类变量


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  # ['roll over', 'play dead']


# 方法属性：
class MethodTest:
    def inner_test(self):
        print('in class')

def outer_test():
    print('out of class')

mt = MethodTest()
mt.outer_test = outer_test

print(type(MethodTest.inner_test))  # <class 'function'>
print(type(mt.inner_test))  # <class 'method'>
print(type(mt.outer_test))  # <class 'function'>

# 实例只有在引用方法属性的时候才会将自身作为第一个参数传递，调用实例的普通函数则不会，