# 有参数装饰器，指的是装饰器函数是有参数的，而不是被装饰对象。

# import time
# current_status={'user':None,'login_status':False}
def auth(func):
    def inner(*args,**kwargs):
        if current_status['user'] and current_status['login_status']:
            res = func(*args, **kwargs)
            return res
        name=input('username>>:').strip()
        pwd=input('password>>:').strip()
        if name == 'egon' and pwd == '123':
            print('login successfull')
            current_status['user']=name
            current_status['login_status']=True
            res=func(*args,**kwargs)
            return res
    return inner

@auth #index=auth(index)
def index():
    time.sleep(3)
    print('welcome to index page')
    return 123

@auth
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)
    return 456
index()
home('egon')




#
# import time
# current_status={'user':None,'login_status':False}
# def auth(egine='file'):
#     # egine='file'
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if current_status['user'] and current_status['login_status']:
#                 res = func(*args, **kwargs)
#                 return res
#
#             if egine == 'file':
#                 u='egon'
#                 p='123'
#             elif egine == 'mysql':
#                 print('mysql auth')
#                 u = 'egon'
#                 p = '123'
#             elif egine == 'ldap':
#                 print('ldap auth')
#             else:
#                 pass
#             name = input('username>>:').strip()
#             pwd = input('password>>:').strip()
#             if name == u and pwd == p:
#                 print('login successfull')
#                 current_status['user'] = name
#                 current_status['login_status'] = True
#                 res = func(*args, **kwargs)
#                 return res
#         return inner
#     return wrapper
# @auth(egine='ldap') #@wrapper #index=wrapper(index) #index=inner
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#     return 123
#
#
#
# index() #inner()