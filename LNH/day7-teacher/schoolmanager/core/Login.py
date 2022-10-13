# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys
import hashlib
import logging

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Prompt import Prompt
from conf import settings
# from lib.MyPickle import MyPickle
from lib.MyJson import MyJson
from lib import MyLogger
from conf import settings

MyLogger.load_my_logging_cfg()
logger = logging.getLogger()
logger_error = logging.getLogger('error')


class Login(object):
    def __init__(self):
        self.auth_dic = {
            'username': None,
            'status': False,
            'role': None,
            'failure': 1,
            'maxmum': 5,
            'flag': True,
        }

    # 装饰器函数，用于验证是否登陆了
    # @staticmethod
    def wrapper(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            if self.auth_dic['status']:
                ret = func(*args, **kwargs)
                return ret
            else:
                print('请先进行登陆')
                reg = logger()
                if reg:
                    reg = func(*args, **kwargs)
                    return reg

        return inner

    @staticmethod
    def get_pwd(username, password):
        '''
        获取加密密码
        :param username:
        :param password:
        :return:32位的十六进制数据字符串
        '''
        if not password:
            return '用户名和密码不能为空'
        salt = settings.secret_key
        m = hashlib.md5((username + salt).encode('utf-8'))
        m.update('password'.encode('utf-8'))
        return m.hexdigest()

    def login(self):
        exit_flag = False
        while not exit_flag:
            while self.auth_dic['failure'] <= self.auth_dic['maxmum']:
                username = input('请输入用户名 :').strip()
                if not username:
                    print(Prompt.display('用户名不能为空', 'red'))
                    continue
                password = input('请输入你的密码: ').strip()
                if not password:
                    print(Prompt.display('密码不能为空!', 'red'))
                    continue

                encrypt_pwd = self.get_pwd(username, password)

                auth_res = self.user_auth(username, encrypt_pwd)
                # print(type(auth_res))

                if auth_res['msg']:
                    print(Prompt.display(' 登陆成功', 'green'))
                    logger.info('%s登陆成功' % (username))

                    # 修改登陆后的用户信息
                    self.auth_dic['username'] = username
                    self.auth_dic['status'] = True
                    self.auth_dic['role'] = auth_res['role']

                    return {'username': username, 'role': auth_res['role']}

                else:
                    chance = self.auth_dic['maxmum'] - self.auth_dic['failure']
                    print('用户名或者密码错误，请重新输入。你还有 ' + Prompt.display(chance, 'red') + '机会!')
                    self.auth_dic['failure'] += 1
                    logger.info('%s 登陆失败次数 %s 次' % (username, self.auth_dic['maxmum'] - chance))

                # 如果失败次数超过最大值，直接退出
                if self.auth_dic['failure'] > self.auth_dic['maxmum']:
                    self.auth_dic['flag'] = False
                    print('你尝试登陆次数超过最大登陆次数，账户已经锁定，暂时不能登陆，请联系管理员')
                    return False

    @staticmethod
    def user_auth(username, password):
        '''
        判断用户输入的用户名和密码是否正确。
        :param username:
        :param password:
        :return:
        '''

        # print(username,password)
        # if not username or not  password:
        #     print(Prompt.display('用户名和密码不能为空', 'red'))
        #     return False

        user_info = MyJson(settings.file_name['user'])
        # print(user_info)
        read_user = user_info.load()

        # for user_l in read_user:
        #     user_list.append(user_l)
        #     print(user_l)
        # print(user_list)
        for user in read_user:
            # print(user)
            # print(user)
            if username == user['name'] and password == user['password']:
                result = {'msg': True, 'role': user['role']}
                return result
            else:
                return {'msg': False, 'role': None}


def get_pwd(username, password):  # 用于别的模块导入
    return Login().get_pwd(username, password)


if __name__ == '__main__':
    Login().login()
