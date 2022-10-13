# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


'''
这是改模块的注释内容： hello.py
'''


class Hello():
    '''这时 hello 类'''

    def world(self):
        '''这时 world 方法'''


print(__doc__)
print(Hello.__doc__)
print(Hello.world.__doc__)

'''如果函数里面带有参数，也能给参数添加注释
一个标准的函数注释应该包含着几个部分：

函数实现功能、
参数说明(需传的参数是什么意思，参数类型)
函数返回值，没return 默认为None
'''


def login(user, psw):
    """
    登录函数-连着输入三个双引号后回车，自动出来格式
    :param user: 用户名，str
    :param psw: 密码, str
    :return: resut是登录结果， True or False
    """
    print(user)
    print(psw)
    resut = "登录结果"
    return resut


print(login.__doc__)

'''docstring添加变量
在docstring里面添加变量内容，变量的部分用%s代替，最后取值的时候，前面加一行代码
用变量替换里面的%s部分

'''
c = "这里是变量内容"
def hello():
    """添加的注释部分，%s"""
    print("hello world!")


hello.__doc__ %= c  # 先用变量c替换里面的%s部分
print(hello.__doc__)



'''
使用装饰器decorator 来实现对注释添加变量，使用装饰器把变量传入进去
'''

def docstring_decorator(*args):
    '''这时一个可以实现对docstring添加变量的装饰器'''
    def dec(obj):
        obj.__doc__=obj.__doc__.format(*args)
        return obj
    return dec

@docstring_decorator('hello函数')
def hello():
    '''这时注释的内容，{0}'''
    print('hello')

print(hello.__doc__)


@docstring_decorator('hello函数,','world函数')
def world():
    '''这时注释的内容，{0} {1}'''
    print('hello world')

print(world.__doc__)









