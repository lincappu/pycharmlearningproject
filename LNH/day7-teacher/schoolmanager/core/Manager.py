# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from conf import settings
from core.Course import Course
from core.Classes import Classes
from core.Teacher import Teacher
from core.Student import Student
from core.School import School
from core.Personal import Personal
from core.Login import get_pwd
from lib.MyJson import MyJson
from lib.mylogger import Logger
from core.Prompt import Prompt


class Manager(object):
    operate_lst = [
        ('创建老师', 'create_teacher'),
        ('创建班级', 'create_classes'),
        ('创建课程', 'create_course'),
        ('创建学生', 'create_student'),
        ('创建学校', 'create_school'),
        ('查看老师', 'ses_teacher'),
        ('查看班级', 'ses_classes'),
        ('查看课程', 'ses_course'),
        ('查看学生', 'ses_student'),
        ('查看学校', 'ses_school'),
        ('退出', 'q')
    ]

    def __init__(self, info):
        self.info = info
        if info['role'] == 'Manager':
            self.main()
        else:
            print('你不是 Manager 用户！')

    def input_check(self, msg, data_type='str', scope=0, li=[]):  # 检测输出的信息

        def entry(msg):
            ret = input('请出入 %s ，或者输入 q 退出' % msg).strip()
            return ret

        s1 = entry(msg)
        li.append(s1)

        if not s1:
            print('%s不能为空' % msg)
            self.input_check(msg, data_type, scope)
        else:
            if s1.upper() == 'Q':
                self.q()
            else:
                if data_type == 'int':
                    if s1.isdigit():
                        s1 = int(s1)
                        if s1 == 0:
                            print('%s不能小于%s' % (msg, 0))
                            self.input_check(msg, data_type, scope)
                        if s1 >= scope:
                            print('%s不能超过 %s!' % (msg, scope))
                            self.input_check(msg, data_type, scope)
                        else:
                            return li[-1]
                    else:
                        print('%s请输入整数!' % msg)
                        self.input_check(msg, data_type, scope)
                elif data_type == 'sex':
                    if s1 == '':
                        print('性别不能为空!')
                        self.input_check(msg, data_type, scope)
                    elif s1.upper() == 'M' or s1.upper() == 'F':
                        return li[-1]
                    else:
                        print('性别请输入M或者F')
                        self.input_check(msg, data_type, scope)

                return li[-1]

    def main(self):
        print(Prompt.display('你好 {} 管理员  欢迎使用校园后台管理系统！\n'.format(self.info['username'], 'purple_red')))

    def q(self):
        print('你已退出校园后台管理系统')
        exit()

    def create_teacher(self):
        name=self.input_check('老师的姓名')

        ret=Personal.username_exist(name)