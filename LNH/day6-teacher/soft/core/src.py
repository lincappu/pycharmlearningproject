import sys,os


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from lib import common


#要拿到logger对象
print(__name__)
logger1=common.get_logger(__name__) #core.src
logger2=common.get_logger('collect')

current_user={'user':None}
def auth(func):
    def wrapper(*args,**kwargs):
        if current_user['user']:
            return func(*args,**kwargs)

        name=input('username>>: ').strip()
        password=input('password>>: ').strip()

        db_obj=common.conn_db() #连接数据库，拿到数据库对象
        if db_obj.get(name) and password == db_obj.get(name).get('password'):
            logger1.info('登录成功')
            logger2.info('登录成功')
            current_user['user']=name
            return func(*args,**kwargs)
        else:
            logger1.error('登录失败')
            logger2.error('登录失败')

    return wrapper

@auth
def shop():
    print('is shoping')

@auth
def run():
    print('''
    1 购物
    2 结账
    3 重置
    4 退出
    ''')
    while True:
        choice=input('>>: ').strip()
        if not choice:continue
        if choice == '1':
            shop()



