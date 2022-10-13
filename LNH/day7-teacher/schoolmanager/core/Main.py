# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import sys

import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import settings
from core.Login import Login
from core.Personal import Personal
# from core.Manager import Manager
# from core.Teacher import Teacher
# from core.Student import Student
from core.Prompt import Prompt


def main():
    lg=Login()
    ret=lg.login()
    print(ret)
    if ret:  # 登陆成功，返回角色。
        clas = getattr(sys.modules['core.' + ret['role'], ret['role']])  # 根据返回的角色拿相对用的类名，
        if ret['role'] == 'Manager':
            obj=clas(ret)   # obj返回的是类名
        elif ret['role'] == 'Teacher':  # 判断角色为老师
            info = Personal.get_info(ret)  # 获取当前登录用户的详细信息
            obj = clas(ret, info['name'], info['age'], info['sex'], info['course'])  # 实例化对象
        elif ret['role'] == 'Student':
            info = Personal.get_info(ret)
            obj = clas(ret, info['name'], info['age'], info['sex'], info['course'], info['score'],info['classes'])
        else:
            print('角色未定义!')




def interlacing_color(operate_lst):  # 隔行换色
    diff = 0  # 差值
    if len(operate_lst) > len(Prompt.colour_list):  # 当菜单列表长度大于颜色列表长度时
        diff = len(operate_lst) - len(Prompt.colour_list)  # 菜单列表长度-颜色列表长度

    colour_list = list(Prompt.colour_list)
    new_list = colour_list  # 新的颜色列表

    if diff >= 0:  # 当菜单列表长度大于等于颜色列表长度时
        for i in range(diff + 1):
            new_list.append(colour_list[i])  # 添加颜色,使颜色列表等于菜单列表长度

    count = -1  # 颜色列表索引值，默认为-1
    for key, item in enumerate(operate_lst, 1):  # 获取每个角色类的operate_lst静态属性,显示的序列号从1开始
        count += 1  # 索引加1
        ret = Prompt.display('{}.\t{}'.format(key, item[0]), new_list[count])  # 按照列表顺序显示颜色
        print(ret)



