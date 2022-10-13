# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

#
# user = ['test','test1','test2','test3']
# password=['test','test1','test2','test3']
# count=0
#
# while  True:
#     if count >2:
#         print('你操作太频繁了，请等一会再操作')
#         break
#     name= input('your name:')
#     if not name in user:
#         print('your name not exists')
#         continue
#     pwd=input('your password')
#     id=user.index(name)
#     if pwd == password[id]:
#         print('欢迎登陆')
#         continue
#     else:
#         print('密码错误')
#         count+=1


# dic = {
#     'apple': 10,
#     'tesla': 10000,
#     'mac': 3000,
#     'lenovo': 30000,
#     'chicken': 10
# }
# good=[]
# while True:
#     for key,item in dic.items():
#         print('name={name},price={price}'.format(name=key,price=item))
#     choice=input('商品名称：').strip()
#     if  choice=='quit':
#         break
#     if choice not in dic:
#         print('您选择的东西不存在，请重新选择')
#         continue
#     count=int(input('数量').strip())
#     if not count.isdigit():
#         print('请出入数字')
#         continue
#     else:
#         print('您购买的商品为%s %d:' %(choice,int(count)))
#         print('您购买的商品为%s %d:' %(format(choice),format((count))))  #这种 format 只能是 str 类型的，不能是数字类型的。

# 三级菜单的功能
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
# exit_tag = True
# while exit_tag:
#     for key in menu:
#         print(key)
#     choice =input('your city:').strip()
#     if not choice:
#         continue
#     if choice=='quit':
#         exit_tag=False
#         continue
#     if choice=='bye':
#         continue
#
#     if choice in menu:
#         while exit_tag:
#             first=menu[choice]
#             for key2 in first:
#                 print(key2)
#             choice2=input('town:').strip()
#             if choice2 == 'bye':
#                 break
#             if not choice2:
#                 continue
#             if choice2 == 'quit':
#                 exit_tag = False
#                 continue
#             if choice2 in first:
#                 while exit_tag:
#                     second=first[choice2]
#                     for key3 in second:
#                         print(key3)
#                     choice3=input('whres：').strip()
#                     if not choice3:
#                         continue
#                     if choice3 == 'quit':
#                         exit_tag = False
#                         continue
#                     if choice3 in second:
#                         third= second[choice3]
#                         for key4 in third:
#                             print(key4)
#                         choice4=input('four:').strip()
#                         if not choice4:
#                             continue
#                         if choice4 == 'quit':
#                             exit_tag = False
#                             continue


#
#
#
# b=u'你好'
# print([b.encode('utf-8')])
#
# x='上'
# print(type(x))





# with  open('log','r',encoding='utf-8') as rf , open('log','w+',encoding='utf-8') as wf:
#
#     wf.write('nihao\n')
#     wf.writelines(['wo\n','men\n'])
#     line = rf.readlines()
#     print(line)


# with  ope n('log','a+',encoding='utf-8') as f:
#     f.writelines(['1','2\n','3'])


#
# with open('a.jpeg','rb',) as f:
#     line=f.readlines()
#     print(line)





# data=f.read(4)
# data=f.read(5)
# data=f.readlines()

# print(f.readable())
# print(data)
# for i in range(8):
#     print(f.readline(),end='')



# for line in f:
#     print(line,end='')

# line=f.readline()
# while line:
#     print(line,end='')
#     line=f.readline()

# for line in open('log','r',encoding='utf-8'):
#     print(line,end='')

# lines=f.readlines()
# for line in lines:
#     print(line,end='')
#     line=f.readlines()
# f.write('nihao')

# line=f.readlines()






# for line in f.readlines():
#     print(line,end='')








# f.close()






#  这个例子很好，函数的定义雨调用，作用域的关系。
# from pymysql import protocol
#
# # a = 1
# #
# #
# # def fun_1():
# #     a = 2
# #
# #     def fun_2():
# #         nonlocal a
# #         a = 3
# #
# #         def fun_3():
# #             a = 4
# #             print(a)
# #
# #         print(a)
# #         fun_3()
# #         print(a)
# #
# #     print(a)
# #     fun_2()
# #     print(a)
# #
# #
# # print(a)
# # fun_1()
# # print(a)
# #
# # fun_1()
#
# # .msg = '''
# # def func():
# #     print('有计划没行动等于零')
# # func()
# # '''
# # exec(msg)
#
#
# from threading import Thread
# import time
# def foo():
#     print(123)
#     time.sleep(2)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(2)
#     print("end456")
#
#
# t1=Thread(target=foo)
# t2=Thread(target=bar)
#
# t1.daemon=True
# t1.start()
# t2.start()
# print("main-------")



# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(g.send(7))




#  __eq__ 和 __str__ 类的方法使用规范：
class Item:
    def __int__(self,name,weight):
        self.name = name
        self.weight = weight

    def __eq__(self,other):  # 限定比较的参数
        if type(self) == type(other) and  self.weight == other.weight and self.name == other.name:
            return True
        else:
            return False

    def __str__(self):  # 重写 print(实例名)时调用的 __str__方法
        print('the name of this cat is {}'.format(self.name))

















