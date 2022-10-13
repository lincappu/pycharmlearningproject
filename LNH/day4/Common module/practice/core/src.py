# !/usr/bin/env python3
# _*_coding:utf-8_*_

from lib import common




print(__name__)  # core.src
logger1=common.get_logger(__name__)
logger2=common.get_logger('collect')


current_user={'user':None}
def auth(func):
    def wrapper(*args,**kwargs):
        if current_user['user']:
            return func(*args,**kwargs)

        name=input('name>>：').strip()
        password=input('password>>:').strip()

        db_obj = common.db_conn('utf-8')
        if  db_obj.get(name) and password == db_obj.get(name).get('password'):
            print('登陆成功')
            logger1.info('登陆成功')
            logger2.info('登陆成功')
            current_user['user']=name
            return  func(*args,**kwargs)
        else:
            print('登陆失败')
    return wrapper




@auth
def shop():
    print('开始购物')

@auth  # run=auth(run)
def run():
    print('''
    1.购物
    2.结账
    3.重置
    4.退出
    ''')
    while True:
        choice=input('选择>>:').strip()
        if not choice:continue
        if choice  == '1':
            shop()


# run()

