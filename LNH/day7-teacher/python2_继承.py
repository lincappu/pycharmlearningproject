#coding:utf-8
class A:pass
    # def func(self):
    #     print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B,C):pass

# d = D()
# d.func()
# class A1(object): #新式类：广度优先
#     pass

class A:pass
    # def func(self):
    #     print('A')

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

f = F()
f.func()