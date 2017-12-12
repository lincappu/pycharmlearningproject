#变量
# a=100087
# print(type(a))
#
# x = 1 - 2j
# print(x.imag)
# print(x.real)
#
# msg = "My name is Egon , I'm 18 years old!"
# print(msg)
#
#
# msg = '''
# 今天我想写首小诗，
# 歌颂我的同桌，
# 你看他那乌黑的短发，
# 好像一只炸毛鸡。
# '''
# print(msg)
#
#字符串的加法和乘法运算，只有字符串没有字符的概念
#
# name = 'egon'
# age = '18'
# print(name+age)
#
# print(name*5)



#列表   取数据时要提前知道有几项，不方便。
# stu=['egon','alex','wupieqi']
# print(stu)
# print(stu[2])
# stu_info=[['egon',18,['play',]],['alex',19,['play','sleep']]]
# print(stu_info)
# print(stu_info[0])
# print(stu_info[1][2])
# print(stu_info[1][2][1])


#字典   可以实现key-value的形式进行取值。
#     'name':'egon',
#     'hobbies':['play','sleep'],
#     'age':18,
#     'sex':'male',
#     'company':{
#         'name':'oldboy',
#         'type':'edu',
#         'emp_num':40,
#     }
# }
#
# print(info['company']['name'])
#
# print('''
# ''')
#
#
#这是列表和字典的同时使用。
# stu=[
#     {'name':'alex','age':18,'hobbies':['paly','sleep']},
#     {'name':'egon','age':19,'hobbies':['read','walk']},
#     {'name':'wupeiqi','age':20,'hobbies':['music','sleep','read']}
# ]
#
# print(stu[2]['hobbies'][2])
#
# print('my name is %s, and my age is %s' %('egon','54'))
# print('my name is %s,and my age is %d' %('egon',54))
#
# # name = input('your name: ')
# # age = input('youe age: ')
#
# print('your name is %s and your age is %s'%(name,age))
#
#打印格式 %s %d 有区别，%s 可以接受任意字符串和数字，而%d只能接受数字，使用的时候要注意默认的规则，比如input都是字符串。
# name=input('name: ')
# age=input('age: ')
# sex=input('sex: ')
# job=input('job: ')
# print('------info of egon------')
# print('Name : %s' %name)
# print('Age  : %s' %age)
# print('Sex  : %s' %sex)
# print('job  : %s' %job)
# print('--------- end-----------')



#if 判断的使用  if  elif  else  注意   ：

# name=input('name: ')
# password=input('password :')
#
# if name=='egon' and password=='123':
#     print('egon login success')
# else:
#     print('用户名或者密码错误')



# '''
# egon --->超级管理员
# tom --->普通管理员
# jack,rain ---->业务主管
# 其他  ----> 普通用户
# '''
# name=input('请输入你的名字：')
#
# if name == 'egon':
#     print('超级管理员')
# elif name == 'tom':
#     print('普通管理员')
# elif name == 'jack' or name == 'rain':
#     print('业务主管')
# else:
#     print('普通用户')

#多种情况判断下如何简写。
# today=input('>>:')
# if today in ['saturday','sunday']:
#     print('出去浪')
# elif today in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
#     print('上班')
# else:
#     print('''请输入下面的一个
#     Monday
#     Tuesday
#     Wednesday
#     Thursday
#     Friday
#     Saturday
#     Sunday
#     ''')


#while循环的   通常和if联合使用
#
# count=0
# while count <=10:
#     print('loop',count)
#     count+=1
#
#
# count=0
# while count<=10:
#     if count %2 == 0:
#         print('loop',count)
#     count+=1
#
# count=0
# while count <= 10:
#     if count %2 == 1:
#         print('loop',count)
#
#     count+=1

#break  退出本层循环
#continue 退出本次循环
# name='egon'
# password='123'

# while True:
#     inp_name=input('用户名: ')
#     inp_pwd=input('密码: ')
#     if inp_name == name and inp_pwd == password:
#         while True:
#             cmd=input('>>: ')
#             if not cmd:
#                 continue
#             if cmd == 'quit':
#                 break
#             print('run <%s> ' %cmd)
#     else:
#         print('用户名或者密码错误')
#         continue
#     break

#
# tag=True
# while tag:
#     inp_name=input('name: ')
#     inp_pwd=input('password: ')
#     if inp_name == name and inp_pwd == password:
#         while tag:
#             cmd=input('>>:')
#             if not cmd:
#                 continue
#             if cmd == 'quit':
#                 break
#             print('run %s' %cmd)
#     else:
#         print('用户名或者密码错误')
#     break

# while True:
#     print('123')
#     break
#     print('456')
#
#
# while True:
#     print('123')
#     continue
#     print('456')



#while +else ： 表示while循环被正常执行完，中间没有被break中断，就会执行else后面的内容。
# count=0
#
# while count <= 5:
#     count += 1
#     if count == 4:
#         break
#     print('loop',count)
#
# else:
#     print('上面的whle正常的执行完了')




#练习题：

# count=1
# while count<=10:
#     if count == 7:
#         count+=1
#         continue
#     print(count)
#     count+=1
#
#
# sum=0
# count=1
# while count <= 100:
#     sum+=count
#     count+=1
# print(sum)

# count=1
# while count <= 100:
#     if count%2 != 0:
#         print(count)
#     count+=1
#
# count=1
# while count <+100:
#     if count%2 == 0:
#         print(count)
#     count+=1
#
# count=1
# sum=0
# while count <= 100:
#     if count%2 == 0:
#         sum-=count
#     else:
#         sum+=count
#     count+=1
#
# print(sum)


#
# count=0
# while count < 3:
#     name=input('输入用户名： ')
#     pwd=input('密码： ')
#     if name == 'egon'  and pwd == '123':
#         print('sucsess')
#         break
#     else:
#         print('fsild')
#         count+=1


# age=65
# count=0
# while count < 3:
#     guess=int(input('你猜：'))
#     if guess == age:
#         print('恭喜你 你猜对了')
#         break
#     count += 1
#     # else:
#     #     print('猜错了，重新猜')


# age=65
# count=0
# while True:
#     if count == 3:
#         choice=input('是否继续(y/n:)')
#         if choice == 'Y' or choice == 'y':
#             count=0
#         else:
#             break
#
#     guess=int(input('>>'))
#     if guess == age :
#         print('你猜对了')
#         break
#     count+=1

#for循环，这个比较简单。
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s * %s=%s is :' %(i,j,i*j),end=' ')
#     print()


