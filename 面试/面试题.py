# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# # 4、字典删除键和合并字典
# del
# update
#
#
# 20、python2和python3区别？列举5个
# 1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi') Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比 如 print 'hi'
# 2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# 3、python2中使用ascii编码，python中使用utf-8编码
# 4、python2中unicode表示字符串序列，str表示字节序列  python3中str表示字符串序列，byte表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要
# 6、python2中是raw_input()函数，python3中是input()函数



# sort 函数修改的原来的数据
# sorted(dict.items(),keys=lambda  i: i[0], reverse=False)
# sorted(dict.items(),keys=lambda  i: i[1], reverse=False)
# x[0]代表用key进行排序；x[1]代表用value进行排序。
# sorted() 返回的是新的函数



# import  datetime
# print(datetime.datetime.now().isoweekday()) #  显示星期几




import re
a="not 404 found 张三 99 深圳"
a1=a.split(' ')
print(a1)
a2=re.findall("\d+|[a-zA-Z]+",a)
print(a2)
for i in a2:
    if i in a1:
        a1.remove(i)
print(a1)
"\d+|[a-zA-Z]"和"\d+|[a-zA-Z]+"的区别：+和？ 这两个代表重复前面的方式，没有这两个只能匹配单个字符，默认是贪婪匹配，？不是贪婪匹配
小数的匹配： \d+\.?\d*





两层列表推导式：
a=[[1,2],[3,4],[5,6]] 一行代码展开该列表，得出[1,2,3,4,5,6]
x=[j for i in a for j in i]

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

p={key:value for key,value in prices.items()  if value>100}
print(p)

嵌套列表的坑： 录入五个学生三门课的成绩
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']




zip 函数:拉链函数会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。
两个可迭代对象按索引顺序组成元组，





match 和 search 的区别。
re.match(pat, s) 只从字符串s的头开始匹配，比如(‘123’, ‘12345’)匹配上了，而(‘123’,’01234’)就是没有匹配上，没有匹配上返回None，匹配上返回matchobject
re.search(pat, s) 从字符串s的任意位置都进行匹配，比如(‘123’,’01234’)就是匹配上了，只要s只能存在符合pat的连续字符串就算匹配上了，没有匹配上返回None，匹配上返回matchobject
re.sub(pat,newpat,s) 对字符串中s的包含的所有符合pat的连续字符串进行替换，如果newpat为str,那么就是替换为newpat,如果newpat是函数，那么就按照函数返回值替换。sub函数两个有默认值的参数分别是count表示最多只处理前几个匹配的字符串，默认为0表示全部处理；最后一个是flags，默认为0
re.sub(pattern=,string=,inter)
匹配表情包：
re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')



单例模式的实现方式：
# 1、类的形式
# class Singleton(object):
#     __instance=None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance


# a=Singleton()
# b=Singleton()
# print(id(a))
# print(id(a))

# 2.装饰器的形式
# def singleton(cls):
#     __instance={}
#
#     def inner():
#         if cls not in __instance:
#             __instance[cls]=cls()
#         return __instance[cls]
#     return inner
#
# @singleton
# class Cls(object):
#     def __init__(self):
#         pass
#
# c1=Cls()
# c2=Cls()
# print(id(c1))
# print(id(c2))

# 3、通过__new__关键字来实现，通过干预__new__关键字开干预创建的过程
class Singleton(object):
    __instance=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=cls.__new__(cls, *args, **kwarg)

        return cls.__instance

    def __init__(self):
        pass

single1 = Single()
single2 = Single()
print(id(single1) == id(single2))

上面的例子都是现成不安全的单例装饰器，下面是现成安全的单例装饰器：
from functools import wraps
from  threading import RLock
def singleton(cls):
    instance={}
    locker=RLock()

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not  in instance:
            with locker:
                if cls not in instance:
                    instance[cls]=cls(*args,**kwargs)
        return instance[cls]
    return wrapper





深拷贝和浅拷贝的原理：
深拷贝都是完全复制。
浅拷贝分为不可变和可变对象
浅拷贝copy有两种情况：
第一种情况：复制的 对象中无 复杂 子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。
第二种情况：复制的对象中有 复杂 子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值 中的复杂子对象的值 ，会影响浅复制的值。
import copy

l1=[2,2,[9,4,5]]
a=copy.copy(l1)
b=copy.deepcopy(l1)
print(a)
print(b)

print(id(l1))
print(id(a))
print(id(b))




import  random
l=[1,2,3,4,5]
random.shuffle(l)  # 打散函数
print(l)



# 1.有一个jsonline格式的文件file.txt大小约为10G如何读出
# 核心原理：
# 需要分块，然后设置合适的块大小。

# import time
# bulksize=655535
#
# with open('test','r',encoding='utf-8') as f:
#     while True:
#         line=f.readlines(2)
#         if not line:
#             break
#         for l in line:
#             print(l,end='')
#         time.sleep(2)

# mmap的方式：
# import mmap
# def get_line():
#     with open('test','r+',encoding='utf-8') as f:
#         m=mmap.mmap(f.fileno(),0)
        # print(m.read(10))
        # print(m.read(10))
        # print(m.size())
        # print(m.tell())
        # print(m.seek(0))
        # print(m.readline())

        # while True:
        #     line =m.readline().strip()
        #     print(line)
        #     if m.tell()==m.size():
        #         break

        # tmp = 0
        # for i, char in enumerate(m):
        #     if char == b'\n':
        #         yield m[tmp:i + 1].decode()
        #         i + 1



# 2.补充缺失的代码

def print_directory_contents(sPath):
"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import  os
for file_path in os.listdir(s_path):
    s_child_path=os.path.join(s_path,file_path)
    if os.path.isdir(s_child_path):
        print_directory_contents(s_child_path)
    else:
        print(s_child_path)


3、反转字符串：
print("aStr"[::-1])



4、glob.glob和 glob.iglob的区别：
glob.glob 返回是列表，全部的对象
glob.globi 返回的是生成器





5、字符串的相减操作：
给定一个字符串，给出未包含的字母
原理 set1=[a-z]
    set2=string

result=set1=set2




6、查找最大或最小的 N 个元素，或者是优先级的元素
利用 headq 的堆模块的堆的特性，



7、字典健映射多个值
一个 key 映射多个 value，
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
利用collections 模块中的 defaultdict 来构造这样的字典。 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。比如：

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)



8、字典排序，
一个是 lamda 函数
一个是利用 collection 和 orderDict 类来实现。默认是按 value 来实现






迭代工具模块：
itertools模块
无穷迭代器： count  cycle  repeat
根据最短输入序列长度停止的迭代器：
accumulate()
chain()
compress()
排列组合迭代器：
product() p, q, ... [repeat=1]  笛卡尔积，相当于嵌套的for循环
permutations() p[, r] 长度r元组，所有可能的排列，无重复元素
combinations() p, r 长度r元组，有序，无重复元素
combinations_with_replacement() p, r长度r元组，有序，元素可重复



collections 模块的作用总结：
deque： 双端队列  对于头尾操作来说时间复杂度为 O（1）
counter dict 的子类，健是元素，值是元素计数，most_common()方法
orderdict 会记录字典插入的顺序
defaultdict 规定字典的默认值





面向对象：
三个支柱：封装 继承 多态

对象复制： （深复制/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆）

垃圾回收、循环引用和若引用。


垃圾回收机制：在计数引用的基础上同时引用了标记-清除和分代收集策略
计数引用会导致循环引用的问题，从而导致内存泄露，

标记-清除和分代收集策略 见博客


面向对象设计原则：
单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息
说明：上面加粗的字母放在一起称为面向对象的SOLID原则。

GoF设计模式：
创建型模式：单例、工厂、建造者、原型
结构型模式：适配器、门面（外观）、代理
行为型模式：迭代器、观察者、状态、策略




迭代器和生成器：
python 用魔术方法来标示协议




并发编程：
python 实现并发编程的三种方法： 多线程、多进程、异步 IO
多线程：Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier

重点：多线程和多进程的比较。

以下情况需要使用多线程：

程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
以下情况需要使用多进程：

程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
程序的输入可以并行的分成块，并且可以将运算结果合并。
程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。



重点：异步I/O与多进程的比较。

当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。































