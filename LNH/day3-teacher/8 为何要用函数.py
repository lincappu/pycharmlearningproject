'''
1. 组织结构混乱，可读性差
2. 代码冗余
3. 无法统一管理，维护难度极大

具备某一功能的工具即函数

函数的使用的必须遵循：先定义，后调用
'''

#函数分类：
#1 内置函数：python解释器自带的函数，python解释器启动就会定义好这些函数
# len()
# max()
# min()
# sum()

#2 自定义函数：
#语法：
# def 函数名(参数1,参数2,...):
#     """注释"""
#     函数体
#     return 返回值


#定义阶段
def tell_tag():
    print('===========')

def tell_msg(msg):
    print(msg)


#调用阶段
tell_tag()
tell_tag()
tell_msg('hello world')
tell_tag()
tell_tag()
# func()

print(tell_msg)

'''
===========
===========
hello world
===========
===========

'''



















