# 第一次作业:登陆接口
user=['test','test1','test2','test3']
password=['test','1test','2test','3test']
count=0
while True:
    if count > 2:
        print('''
        你操作太频繁,请稍后再试!
        ''')
        break
    name = input('your name: ')
    pwd = input('your password: ')
    if  not name in user:
        print('用户名不存在')
        continue
    id=user.index(name)
    if  pwd == password[id]:
        print('欢迎登陆！')
        break
    else:
        print('用户名或者密码错误！请重试')
        count+=1
#进阶：
# user=['test','test1','test2','test3']
# password=['test','1test','2test','3test']
# count=0
# while True:
#     name = input('your name: ')
#     pwd = input('your password: ')
#     with open('denylogin.txt', 'r')  as file:
#         denylist = file.read()
#         if name in denylist:
#             print('你的账户已经锁定，不能登陆，请联系管理员！')
#             break
#     if  not name in user:
#         print('用户名不存在')
#         continue
#     id=user.index(name)
#     if  pwd == password[id]:
#         print('欢迎登陆！')
#         break
#     else:
#         print('用户名或者密码错误！请重试')
#         count+=1
#     if count > 2:
#         print('''你操作太频繁,账户已经锁定''')
#         with open('denylogin.txt','a') as  file :
#             file.write('%s' %name+'\n')
#             break
