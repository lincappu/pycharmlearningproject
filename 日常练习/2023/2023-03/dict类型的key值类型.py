#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/31 17:04
# @Project  : pycharmlearningproject
# @File     : dict类型的key值类型.py


'''
1 字典的定义与特性
字典是Python语言中唯一的映射类型。
定义：｛key1:value1,key2:value2｝
特性：
    1.key-value结构
    2.key必须可hash、且必须为不可变数据类型、必须唯一
    3.可存放任意多个值、可修改、可以不唯一
    4.无序
'''

# menu = {
#     {
#         'name': '宫保鸡丁',
#         'price': 23
#     }, {
#         'name': '红烧肉',
#         'price': 25
#     }, {
#         'name': '酸菜鱼',
#         'price': 30
#     }, {
#         'name': '西红柿鸡蛋',
#         'price': 12
#     },
# }
# 这种类型的的字典其实都只有一个字典，根本就没有key和value的概念，所以其实没有keys 和values的值

menu2 = {
    "a": {
        'name': '宫保鸡丁',
        'price': 23
    },
    "b": {
        'name': '红烧肉',
        'price': 25
    },
    "c": {
        'name': '酸菜鱼',
        'price': 30
    },
    "d": {
        'name': '西红柿鸡蛋',
        'price': 12
    },
}

# print(menu2.keys())

'''
这种就可以按正常的keys() values()  items()来取值
但是不能 menu['a']['name']="fls" 来修改参数，只能是a['name']="fls"  key不能是可变结构，
'''

