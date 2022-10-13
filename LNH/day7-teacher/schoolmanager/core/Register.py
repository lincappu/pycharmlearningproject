# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Prompt import Prompt
from conf import settings
from core.Login import Login


class Register():
    def __init__(self):
        pass
        # self.usernam = username
        # self.password = password
        # self.role = role

    user_file = settings.file_name['user']

    @staticmethod
    def register():
        user_file = settings.file_name['user']
        print(user_file)

        str = '现在开始注册登陆用户！' \
              '请务必输入用户、密码和角色。' \
              '角色可选项为:  \n' \
              '  Manager    \n' \
              '  read   \n'
        print(str)

        exit_flag = True
        while exit_flag:
            username = input('请输入用户名：').strip()
            if not username:
                print(Prompt.display('用户名不能为空', 'red'))
                continue
            if username == 'q':
                exit_flag = False
                continue
            password = input('请输入密码：').strip()
            if not password:
                print(Prompt.display('密码不能为空', 'red'))
                continue
            if password == 'q':
                exit_flag = False
                continue
            role = input('请输入角色：').strip()
            if not role:
                print(Prompt.display('角色不能为空', 'red'))
                continue
            if role == 'q':
                exit_flag = False
                continue
            print(username, password, role)

            en_pwd = Login.get_pwd(username, password)
            print(en_pwd)

            insert_user_dict = {}

            insert_user_dict['name'] = username
            insert_user_dict['password'] = en_pwd
            insert_user_dict['role'] = role

            print(os.path.getsize(user_file))
            if  os.path.getsize(user_file):
                with open(user_file,'r',encoding='utf-8') as read_f:
                    user_array=json.load(read_f)
                user_array.append(insert_user_dict)

                with open(user_file, 'w', encoding='utf-8') as write_f:
                    json.dump(user_array, write_f)
                    write_f.write('\n')
            else:
                user_array=[]
                user_array.append(insert_user_dict)
                with open(user_file, 'a+', encoding='utf-8') as write_f:
                    json.dump(user_array, write_f)
                    write_f.write('\n')

            print('注册成功！')

            exit_flag=False


a = Register()
a.register()
