# !/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# 变量
# a=100087
# print(id(a),type(a),a)   驼峰体和下划线 （推荐使用下划线）
# 常量的意义---将变量名全部写成大写的，提示为常量，但是其实还是可以修改的
#
# 程序交互：
# python3中，所有input都是string类型的，
# python2中输入什么类型就是什么类型，raw_input等于python3中的input
# 注意要想要 int 类型的使用 int(input(''))
#
# 复数型
# x = 1 - 2j
# print(x.imag) #虚部
# print(x.real) #实部
#
# msg = "My name is Egon , I'm 18 years old!"


# msg = '''
# 今天我想写首小诗，
# 歌颂我的同桌，
# 你看他那乌黑的短发，
# 好像一只炸毛鸡。
# '''
# print(msg)
#
# 字符串的加法（其实就是字符串拼接，但是只有都是字符串类型的才能拼接，str(%d) 转换为字符串类型
# 乘法运算：其实就是拼接
# 只有字符串没有字符的概念

# name = 'egon'
# age = '18'
# print(name+age)
#
# print(name*5)
# #

# 数据类型：
#
# x = 2.3
# print(id(x),type(x),x)
#
# ==和 is  判断的类型：  is 是同一性运算符，判断两个变量id 是不是一样的。
# 有个区别 ：
# 当变量小于256时，两个变量的  x is y 是 true，大于256就不成立。pycharm 这个做了处理显示不出来的。
# 当 x=123 y=x 这种是，x 永远等于 y，
# 这两种区别是 python 结构限制的，申请了两块地址空间，所以 id 不可能相等。
# 这种类型永远是整型和字符串才有的特性。
# print(x is y)
# print(id(x),id(y))
# 长整型，python3中没有长整型，  python3中int就是长整型，   python2  int 是短整型， long是长整型


#####整型#########：
# a=int(10)
# print(a.__and__(19))
# print(round(3.6))
# b=a.__str__()
# print(type('b'))



########字符串######
# 字符串 :  顾头不顾尾
# 内置函数：
# x = 'helloworld'
# 按索引取值
# print(x[1])
# 切片,步长： 头，尾，步长, 顾头不顾尾
# print(x[1::2])
# print(x[5:1:-1])  # 逆向取值，
# 长度：只有字符串有，整型没有这个属性。
# in  判断
# print('he' in x)
# 移除空白strip,默认是两端的空格，
# msg = '*****fs****ff****'
# print(msg.strip('*'))
# print(msg.lstrip('*'))
# print(msg.rstrip('*'))

# 切分操作，按特定的字符，   按什么切，切几次，取第几个值。 最后是个字符串
# msg = 'root:x:0:0:/root'
# print(msg.split(':')[0])
# print(msg.split(':', 1))  # 1： 切分一次
# name = 'C:/a/b/c/d.txt'
# print(name.split('/',1))
# print(name.split('/')[0])
# print(name.split('/')[-1])
# print(name.rsplit('/', 1)[0])
#
# msg = 'niHao'
# print(msg.lower())
# print(msg.upper())
#
# msg = 'abcdefg'
# print(msg.startswith('ab'))
# print(msg.endswith('fg'))
#
# msg = 'zhe  shi  wo  de aaa bbb cc  '
# print(msg.replace('a', 'A', 1).strip())

# format
# res='{} {} {}'.format('egon',18,'male')
# print(res)
# res='{1} {0} {1}'.format('egon',18,'male')
# print(res)
# res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
# print(res)


# msg = 'li xin ni hao'
# print(msg.find('ni'))  # 从左向右找，找到后返回第一个字符的索引
# print(msg.find('fsdf')) #  find如果没有找到就知道返回 -1
# print(msg.index('nn'))  # 如果没有 则直接报错。
#
# msg = 'hello world'
# print(msg.count('l', 0, 3))  #返回的是个数,注意是顾头不顾尾

# msg = 'a:a:b:c:d:e'
# l = msg.split(':')
# print(l)
# l.append('f')  #默认是添加到最后
# print(l.count('a'))
# print(l)
# print('/'.join(l))
# print('#'.join(l))
# tag = '#'
# print(tag.join(['a', 'b', 'c']))

# age=input('your age: ')
# print(age.isdigit()) #只能判断 bytes 和 unicode类型，，判断"字符是否为数字" ##重要理解


# find  rfind  index  rindex  count    返回都是索引，区别在于报错不报错。  带 r 的为发现的最右边的索引。
# name = 'egon say hello'
# print(name.find('s', 1, 6))
# print(name.index('s', 1, 6))
# print(name.rfind('g', 1, 6))
# print(name.count('e', 0, 13))
#
# center ljust rjust zfill
# msg = 'egon'
# print(msg.center(18,'#'))
# print(msg.ljust(18,'#'))
# print(msg.rjust(18,'#'))
# print(msg.zfill(18)) # 用0 填充，默认是从左边开始填充


# expangtable 制表符的个数，要以 4 个为单位。
# msg = 'abc\tdefs'
# print(msg)
# print(msg.expandtabs(8))


# capitalize   swapcase  titile
# msg = 'egon say Ello'
# print(msg.capitalize())  #首字母大写
# print(msg.lower()) #全部变小写
# print(msg.upper()) #全部变大写
# print(msg.title()) #每个单词的首字母大写
# print(msg.swapcase()) #大小写翻转
#
# is  系列
# msg='Avbcd'
# print(msg.islower())
# print(msg.isupper())
# print(msg.istitle())



# msg = 'abc'
# print(msg.isalpha())   # 字符串是否由字母组成的
# print(msg.isalnum()) #字符串是否由子母或者数字组成

#
# #判断数字
# num1= b'4'
# num2= u'4'  #python3 默认就是 unicod
# num3= '四'  #中文数字
# num4= '肆'  #中文数字
# num5= 'IV'  #罗马数字
# print(msg.isdigit())    #只能判断 bytes 和 unicode 类型的。
# print(msg.isdecimal())  #只能判断 unicode 类型的
# print(msg.isnumeric())  #能判断2 3 4 5四种类型的
# 这三个不能判断浮点类型的数据

# 例子：
# age = 10
# inp=input('you age: ')
# if inp.isdigit():
#     inp=int(inp)
#     if age == inp:
#         print('OK')
#     else:
#         print('error')

# 其他判断：
# print('===>')
name='egon123'
# print(name.isalnum()) #字符串由字母或数字组成
# print(name.isalpha()) #字符串只由字母组成
#
# print(name.isidentifier())  # 是否是有效地标识符， false比如说 数字开头的字符串就不符合。
# print(name.islower())
# print(name.isupper())
# print(name.isspace())
# print(name.istitle())   # 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
#
# msg = '    '
# print(msg.isspace())  #判断字符串是否由空格组成，而不是判断为空。
# msg = 'if'
# print(msg.isidentifier())    #isidentifier() 方法用于判断字符串是否是有效的 Python 标识符，可用来判断变量名是否合法。True或者 False。




# 总结：字符串
# 存的是一个值，有序 ，不可变，


# 练习
# name = ' aleX'
# print(name.strip())
# print(name.startswith('al'))
# print(name.endswith('X'))
# print(name.replace('l','p',1))
# print(name.split('l'))
# print(name.upper())
# print(name.lower())
# print(name[1])
# print(name[2])
# print(name[-2:])
# print(name.index('e'))
# print(name[0:-1])
# print(name[:])


################列表#############
# 列表  索引取值 取数据时要提前知道有几项，不方便。
# stu=['egon','alex','wupeiqi',5]
# print(stu)
# print(stu[2])
# stu_info=[['egon',18,['play',]],['alex',19,['play','sleep']]]
# print(stu_info)
# print(stu_info[0])
# print(stu_info[1][2])
# print(stu_info[1][2][1])
# 操作:
# print(stu[1])
# stu.append('ela')
# print(stu)
# stu[0]='ALEX'
# print(stu)

# 切片： 步长
# print(stu[0:3:2])

# 长度
# print(len(stu))

# 成员判断:
# print('alex' in stu)
# print('ales' not in  stu)
# print(5 in stu)
#

# 增删
# stu.append(7)
# print(stu)

# del stu[0]
# print(stu)
#
# stu.remove('wupeiqi')  #remove 只是单纯的是删除，不会返回删除的值，按值来删除，
# print(stu)
#
# res=stu.pop()  #是按照索引来删除，默认是从末尾删除,有返回值，
# print(stu,res)
#
# del stu[1]   # 按照索引删除，没有返回值，并且这是个命令实现的，
# print(stu)


# 其他操作:
# stu=['alex','wupeiqi','egon','linhaifeng','ela']
# stu.insert(0,'fls')
# print(stu)

# stu.extend(['a','b','c'])  # 两个列表的合并，只能在末尾加
# print(stu)
#
# print(stu.count('alex'))

# print(stu.clear())
#
# l=stu.copy()
# print(l)
#
# stu.reverse()
# print(stu)

# l=[1,3,6,4,7,3,5]
# l.sort()
# l1=l.sort()   # 这个没有返回值，是在原来的列表中操作。所以不能进行赋值操作。
# print(l,l1)
# l.sort(reverse=True)  #原有的列表将会修改，不存在了。
# print(l)
# print(sorted(l,reverse=True))   # sorted 这个不是对原来的列表操作，有返回值。
# print(l)

# print(reversed(l))
# l.reverse()
# print(l)


# 数值列表
# l=list(range(1,11,2))
# print(l)



# 练习：
# data=['alex',49,[1900,3,18]]
# name=data[0]
# age=data[0]
# year=data[2][0]
# month=data[2][1]
# day=data[2][2]
# print(name,age,year,month,day)


# sort 的两种效果,使用匿名函数，一个是使用关键字，一个是使用索引值。
# l=[
#     {'name':'alex','age':84},
#     {'name':'oldboy','age':73},
#     {'name':'egon','age':18},
# ]
#
# l.sort(key=lambda l:l['age'])
# print(l)
#
# l=[('dave', 'B', 23), ('jane', 'B', 2), ('john', 'A', 18)]
# l.sort(key=lambda l:l[2])
# print(l)



# operator 函数进行排序，这个需要导包，以后再说，


# 使用列表模拟 队列和堆栈的效果

# l=[]
# l.append('first')
# l.append('second')
# l.append('third')
#
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))
#
#
# l=[]
# l.insert(0,'fist')
# l.insert(0,'second')
# l.insert(0,'third')
# print(l)
#
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))





#######元组类型###########
# 元组和列表相似，但是不能被修改，用小括号标示。
# tup1 = ('f','l','s')
# tup2 = (1,2,3)
# tup3 = "a","b","c","d"
#
# 创建空元组
# tup = ()
# #元组中只包含一个元素时，需要在元素后面加逗号，某个会被认为是整数
# tup = (52,)
# #和列表相似，使用下标引用，可以进行截取，组合。
# #访问:顾头不顾尾
# print(tup1[1])
# print(tup3[1:2])
# print(tup1[1:])
# #修改元组：拼接和相乘：
# print(tup1+tup2)
# print(3*tup2)
# #del tup1  手动删除元组
# #元组运算符
# print(len((1,2,3)))
# print(2 in (1,2,3))
# #元组的内置函数
# print(min((1,2,3))
# print(max((1,2,3)))
# #元组和列表的转换
# l=['a','b','c','d']
# print(list("wobuhao"))
# print(tuple("nihao"))
# print(tuple(list("wobuhao")))
# print(tuple(l))

# 其他操作：
# tup=('a','b','a','d','e')
# print(tup.count('a'))
# print(tup.index('b'))

# 练习：
dic = {
    'apple': 10,
    'tesla': 10000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10
}
# print(dic.items())  # 将字典的元素以列表的格式显示出来。

# good = []
# while True:
#     for key, item in dic.items():
#         # print(key,item)
#         print('name:{name} price:{price}'.format(name=key, price=item))  # format 格式的传值
#     choice = input('商品名称：').strip()
#     if choice == 'quit':
#         break
#     if not choice or choice not in dic:
#         print('请按下面的输入：')
#         continue
#     count = input('购买个数： ').strip()
#     if not count.isdigit():
#         print('请输入数字：')
#         continue
#     else:
#         good.append((choice, dic[choice], int(count)))


# print(good)
# length=len(good)
# zong=0
# print(length)
# y=0
# for x in goo
#     while y < length:
#         print(y)
#         price=int(good[y][1])
#         geshu=int(good[y][2])
#         zong+=price*geshu
#         y += 1
#         print(zong)

# print('总价钱为：%d' %(zong))




# print函数的用法：
# 1.借用 python2 的用法：
# print('%s %d' %(name,age))
# 2.python3.5以上的用法：
# print('{name}  {age}')
# print('{} {}'.format('fls',10))
# print('{name} {age}'.format(name='fls',age=10,))
# print(f'年纪{name} 年纪{age} ')
#
# 3.固定位输出：
# print("%s%s%s%s" % (format(item[0], "<10"), format(item[1], "<10"), format(item[2], "<10"), format(item[3], "<10")))



# #############字典###############
# 可以实现key-value的形式进行取值，取值速度快
# key 必须是不可变类型，value 可以是任意类型，
# 列表、词典这种都是可变类型，所以都是不能作为 key 的。元组、字符串、数字都是不可变类型。可以作为 key
user = {
    'name': 'egon',
    'hobbies': ['play', 'sleep'],
    'age': 18,
    'sex': 'male',
    'company': {
        'name': 'oldboy',
        'type': 'edu',
        'emp_num': 40,
    }
}

# print(user['company']['name'])
# # key  value   item
# print(user.pop('name','None'))
# print(user.keys(),user.values())
# for item in user.items():
#     print(item)
#
# print(user.get('name'))
# print(user.popitem()) # 弹出 key 和 value，pop 只弹出 key


# 字典的内置函数：

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# l = dict.copy()
# print(l)

# seq = ('1','2','3','4')
# d1=dict.fromkeys(seq)
# print(d1)
# d2=dict.fromkeys(seq,10)
# print(d2)
#
# print(dict.get('Name',10))
#
# print('Name' in dict)
#
# print(list(dict.keys()))
#
# dict2={'a':'1','b':'2','c':'3'}
# dict.update(dict2)
# print(dict)
#
# print(list(dict.values()))
#
# print(dict.pop('name',0))
#
# print(dict2.popitem())


# 字典的索引,
'''
由于Python 3.7 *字典是顺序保留的，因此它们现在的行为与collections.OrderedDicts 完全相同。不幸的是，
仍然没有专用的方法可以索引到字典的keys()/ values()中，因此可以通过以下方法获取字典中的第一个键/值：
sql_origin.items()    列表形式的字典。
'''
#1、将字典变成列表的形式，然后按索引取值。
sql_origin = {
    "zong_sdjs": {
        "name": "审贷件数",
        "sql": "a",
        "results": 0,
    },
    "zong_sxtgjs": {
        "name": "授信通过件数",
        "sql": "b",
        "results": 0,
    }
}
# list(sql_origin.items())  [('zong_sdjs', {'name': '审贷件数', 'sql': 'a', 'results': 0}), ('zong_sxtgjs', {'name': '授信通过件数', 'sql': 'b', 'results': 0})]
#  这个会变成由元组组成的列表，元组中第一个是key，第二个就是value。
# 2、使用枚举的形式 :  for  index,value in enumerate(sql_origin.items()):
# 这个就拿到了key对应的index，然后根据这个index来拿值








# #######集合###########
# 无序、可变 不重复
# 用{}或者是 set()标示，空集合必须用 set()标示，{}标示空字典。

# a = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(a)

# 集合间的运算

# a = set('12345')
# b = set('1267')
#
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)   # 不同时包含于 a 和 b 的元素


#基本操作：

# a=set('123')
# a.add('9')
# print(a)
#
# a.update(['a','b'])  # update可以插入任何类型的元素
# print(a)
# a.update({'name':"fls"})  # 插入字典的时候只会插入 key 值
# print(a)
# a.update(('c','e'))
# print(a)

# a.remove('name')  # 元素不存在会发生错误
# print(a)

# a.discard('name') # 元素不存在不会报错
# print(a)

# print(a.pop())  # 随机删除一个元素  ,交互模式下，会删除第一个元素

# a.clear()
# print(a)

# print(a)
# print('3' in a)  # 注意是字符串



# 集合内置方法：
#
# a=set('123')
# c=set('145')
# b=a.copy()
# print(b)

# d=set('123456789')
# print(d)

# print(a.intersection(c))  #  a b 的交集
# print(a)

# print(a.union(c))  # a b 的并集
# print(a)


# a.difference_update(c)   # 没有返回值，直接更新原来的集合
# print(a)

# a.intersection_update(c)  # 没有返回值，直接更新原来的集合
# print(a)

# print(a.isdisjoint(c))  # true 没有相同的 元素，false 有相同的元素
# print(a.issubset(b))  # a 是否是 b 的子集
# print(a.issuperset(b)) # b 是否是 a 的子集






#######数据类型总结##################
# 按存储空间的占用分（从低到高）
#
# 数字
# 字符串
# 集合：无序，即无序存索引相关信息
# 元组：有序，需要存索引相关信息，不可变
# 列表：有序，需要存索引相关信息，可变，需要处理数据的增删改
# 字典：无序，需要存key与value映射的相关信息，可变，需要处理数据的增删改
#
# 按存值个数区分：
# 标量／原子类型：数字，字符串
# 容器类型：列表，元组，字典
#
# 按可变不可变区分：
# 可变：列表，字典
# 不可变：数字，字符串，元组
#
# 按访问顺序区分：
# 直接访问：数字
# 顺序访问（序列类型）：字符串，列表，元组
# key值访问（映射类型）：字典
#


# print(3/2)

# 两种赋值方式######
# 1。链式赋值
# x = y = z = 10
# 交换两个变量的值：
# m = 10
# n = 20
#
# tmp=n
# n=m
# m=tmp
# print(m,n,tmp)
#
# python 的语法：
# m,n=n,m
# print(m,n)
# 2.从一个数据类型中解压出我们想要的值
t=(21,54,4.5,35,56)
# x,y,z,a,b=t
# print(x,y,z,a,b)
#
#
# x,_,_z,_,b=t
# print(_)
#
# x,*_,b=t
# print(b)
#
# x,*_='hello'
# print(x)
#
# x,y,z={'a':1,'b':2,'c':3}
# print(x,y,z)
#
# 直接取出元组的k v 值
# for k,v in user.items():
#     print(k,v)

# user_1={'name':'alex','height':180}
# user.update(user_1)
# print(user)

# dic1={}.fromkeys(['name','age','hobboes'],None)
# print(dic1)



# user = {
#     'name': 'egon',
#     'hobbies': ['play', 'sleep'],
#     'age': 18,
#     'sex': 'male',
#     'company': {
#         'name': 'oldboy',
#         'type': 'edu',
#         'emp_num': 40,
#     }
# }

# 如果没有就直接插入，如果有就返回原来的值
# 用法:
# print(user.setdefault('name','egon'))
# user.setdefault('hobbies',[]).append('read')
# print(user.setdefault('hobbies',[]))
# user.setdefault('hobbies').append('read')
# print(user)


# 这是列表和字典的同时使用。
# stu=[
#     {'name':'alex','age':18,'hobbies':['paly','sleep']},
#     {'name':'egon','age':19,'hobbies':['read','walk']},
#     {'name':'wupeiqi','age':20,'hobbies':['music','sleep','read']}
# ]

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
# 练习：
# 1.
# a={'k1':[],'k2':[]}
# c=[11,22,33,44,55,66,77,88,99,90]
# for i in c:
#     if i > 66:
#         a['k1'].append(i)
#     else:
#         a['k2'].append(i)
# print(a)
# 2.
# a='hello alex alex say hello sb sb'
# l=a.split()
# print(l)
# dic={}
# for item in l:
#     if item in dic:
#         dic[item]+=1
#     else:
#         dic[item]=1
# print(dic)
# print(dic['hello'])





#############集合特性##############
# 作用：去重 ，关系运算：交叉并补
# 优先操作。
# 每个元素必须是不可变类型，不能重复（自动去重，调用的 equals 方法），无序的,
# 定义
# s=set()    # s={}这样创建的是字典
# s={1,2,'a','a','a'} #s=set{1,2,'a'}
# print(type(s))
# print(s)
# print(len(s))
# print('a' in s)
# for item in s:
#     print(item)
# s1 = {1, 2, 4}
# s2 = {4, 6, 5}
# print(s1 | s2)
# print(s1.union(s2))
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s1 - s2 )
# print(s1.difference(s2)) # 只是找到， 返回新 set
# print(s1.difference_update(s2))  # 覆盖掉s1
# print(s1 ^ s2)
# print(s1.symmetric_difference(s2))


# >= s1 包含 s2
# print(s1.issuperset(s2))
# <=  s2 包含 s1
# print(s2.issubset(s1))
# ==  s1  等于 s2


# 常用操作，
# 直接删除，不存在则报错
# s1.pop()     # 末尾删，有返回值 随机删除，不存在会报错。
# print(s1)
# s1.remove(1)  #无返回值 不存在会报错
# print(s1)
# s1.discard(1)  #直接删，不存在则不会报错
# print(s1)
#
# s1.add(3)
# print(s1)

# print(s1.isdisjoint(s2)) # 没有交集则返回 true

# 去重：
# l=[1,1,3,4,5,6,6]  # 不保证顺序了，和列表的顺序一样的
# s=list(set(l))
# print(s)


# 集合和元组一起做去重，元组是不可变类型
# l = [
#     {'name': 'egon', 'age': 18, 'sex': 'male'},
#     {'name': 'alex', 'age': 73, 'sex': 'male'},
#     {'name': 'egon', 'age': 20, 'sex': 'female'},
#     {'name': 'egon', 'age': 18, 'sex': 'male'},
#     {'name': 'egon', 'age': 18, 'sex': 'male'},
# ]
# s = set()
# l2 = []
# for item in l:
#     val = (item['name'], item['age'], item['sex'])
#     if val not in s:
#         s.add(val)
#         l2.append(item)
#         print(s)
# print(l)
# print(l2)
#


# 练习：
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
#
# print(pythons & linuxs)
# print(pythons | linuxs)
# print(pythons - linuxs)
# print(pythons ^ linuxs)


#
#
# 布尔类型：
# not这个特殊
#
#
# 打印格式：
# %s %d 有区别，%s 可以接受任意字符串和数字，而%d只能接受数字，使用的时候要注意默认的规则，比如input都是字符串。
# name=input('name: ')
# age=input('age: ')
# sex=input('sex: ')
# six job=input('six job: ')
# print('info if egon'.center(20,'-'))
# print('Name : %s' %name)
# print('Age  : %s' %age)
# print('Sex  : %s' %sex)
# print('six job  : %s' %six job)
# print('end'.center(20,'-'))
#
#
# ########运算########
# 算数运算
#  + - * / **  //

# 比较运算
# == != <>  < > <=  >=

# 赋值运算
# = += -= *= /= **= //=  %=

# 位运算
# |  &  ……  ~  <<  >>

# 逻辑运算
# and or  not

# 成员运算
# in  not in

# 身份运算
# is not is



# 运算优先级：
# 1.指数优先级大于比较优先级
# 2.比较优先级大于逻辑优先级
# 3.逻辑优先级内部三个 not  and  or



# / // %  除法的三个特性。
# print(5/3)
# print(5//2)
# print(5%2)
# 　　 in
#     not in
#     ＝＝
#     ！＝
#     <,<=
#     >,>=
#     |,|=:合集
#     &.&=:交集
#     －,－=:差集
#     ^,^=:对称差分
#、
#









# a=9
# b=5
# print(a/b)

# boolean 类型的值  not 就是取反的意思，




# if判断的使用:if  elif  else
# 注意：
#
# name=input('name: ')
# password=input('password :')
#
# if name=='egon' and password=='123':
#     print('egon login success')
# else:
#     print('用户名或者密码错误')



#
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
#
# 多种情况判断下如何简写。
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


# while循环的   通常和if联合使用
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
#
# break  退出本层循环
# continue 退出本次循环


# name= 'egon'
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



# 加tag 的话这样就不用写多个 break，一个 tag就将全部的循环条件都置为 False，这样所有的循环就结束掉了
# name= 'egon'
# password='123'
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
#                 tag=False
#             print('run %s' %cmd)
#     else:
#         print('用户名或者密码错误')
#     break


# while True:
#     print('123')
#     break
#     print('456')

#
# while True:
#     print('123')
#     continue
#     print('456')

#
#
# while + else ： 表示while循环被正常执行完，中间没有被break中断，就会执行else后面的内容。

# count=0
# while count <= 5:
#     count += 1
#     if count == 4:
#         break
    # print('loop',count)
# else:
#     print('上面的whle正常的执行完了')
#
#
#
#
# 八个 练习题：
#
# count=1
# while count<=10:
#     if count == 7:
#         count+=1
#         continue
#     print(count)
#     count+=1
# #
#
# sum=0
# count=1
# while count <= 100:
#     sum+=count
#     count+=1
# print(sum)
#
# count=1
# while count <= 100:
#     if count%2 != 0:
#         print(count)
#     count+=1
#
# count=1
# while count <=100:
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
# print(sum)
#
#
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




# for循环，这个比较简单。

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s' %(i,j,i*j),end=' ')
#     print()
#
# user=['test','test1','test2','test3']
# password=['test','1test','2test','3test']
# print(user.index('test3'))
#


###########字符编码##########
# 直接参见资料


# good = {
#     '1':{'apple': 100},
#     '2':{'tesla': 100},
#     '3':{'mac': 100},
#     '4':{'lenovo': 100},
#     '5':{'chicken': 100},
# }



# print(list(good['1'])[0])
# print(mc)
# print(good['1']['apple'])
# x={'a':'10'}
# b=(list(x))
# print(b)
# c=(b[0])
# print(list(x)[0])
# print(x[list(x)])



# 三元表达式：
# a=1
# print('ok') if a>0 else print('false')



# 字符串、列表都是一一对应的：
# a,*_,e='hello'
# print(a,e)


# 解压课迭代对象给多个值：
# record=['lhf','male',18,'12345@qq.com','1861131211']
# *_,phone=record
# name,*_=record
# print(phone)
# print(name)




