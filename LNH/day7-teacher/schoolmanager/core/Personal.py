# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import settings
from lib.MyJson import MyJson


class Personal(object):  # 获取个人信息。

    def __init__(self):
        pass

    def get_info(self):
        role = self['role'].lower()
        user = MyJson(settings.file_name[role]).load()
        for i in user:
            if self['username'] == i['name']:
                return i
        return False

    @staticmethod
    def username_exist(username):  # 判断用户名是否存在
        '''
        判断注册用户名是否可用
        :param username:
        :return:
        '''
        if not username:
            print('用户名不能为空!')
            return False

        user = MyJson(settings.file_name['user']).load()

        for i in user:
            if username == i['username']:
                return False

        return True

    @staticmethod
    def write_auth_file(username, password, role):
        '''

        :param username:
        :param password:
        :param role:
        :return:
        '''

        t1_user = {'username': username, 'password': password, 'role': role}

        user=MyJson(settings.file_name['user'])
        write_user=user.dump(t1_user)
        if write_user:
            return True
        else:
            return False

    @staticmethod
    def write_user_details(infomation,role):
        '''

        :param infomation:
        :param role:
        :return:
        '''

        if not infomation or not role:
            return '用户详细信息或者角色不能为空'

        user=MyJson(settings.file_name[role])

        write_user=user.dump(infomation)
        if write_user:
            return True
        else:
            return False


if __name__ == '__main__':
    pass





















