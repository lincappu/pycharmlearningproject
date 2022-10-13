# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os,sys



from conf  import  settings
from core  import  school_view
from core  import  teacher_view
from core import  student_view


class Admin(object):
    def run(self):
        exit_flag=False
        menu='''
        \033[1;34;1m
        1.学校视图
        2.教师视图
        3.学生视图
        \033[0m 
        '''
        while not  exit_flag:
            print('欢迎进入校园管理系统'.center(50,'#'))
            print(menu)

            user_option=input('请输入视图编号（q 退出）>>：').strip()
            if user_option  == '1':
                school_view()
            elif user_option == '2':
                teacher_view()
            elif user_option == '3':
                student_view()
            elif user_option == 'q':
                exit(1)
            else:
                print('请重新输入')
