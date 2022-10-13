# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


1、字典
copy()方法：
深拷贝：重新申请空间复制该值，
浅拷贝：对于列表类型  只是拷贝引用。 两个都会同时变化

a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
#向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
a['four']=100
print(a)
print(b)
#由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
a['three'].remove(1)
print(a)
print(b)

update 方法：
在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。
a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one':4.5, 'four': 9.3})
print(a)

setdefault() 方法总能返回指定 key 对应的 value；如果该键值对存在，则直接返回该 key 对应的 value；如果该键值对不存在，则先为该 key 设置默认的 value，然后再返回该 key 对应的 value。
a = {'one': 1, 'two': 2, 'three': 3}
# 设置默认值，该key在dict中不存在，新增键值对
print(a.setdefault('four', 9.2))
print(a)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(a.setdefault('one', 3.4))
print(a)

keys()、values()和items()方法:
a = {'数学': 95, '语文': 89, '英语': 90}
print(a.keys())
print(a.values())
print(a.items())
结果：
dict_keys(['数学', '语文', '英语'])
dict_values([95, 89, 90])
dict_items([('数学', 95), ('语文', 89), ('英语', 90)])


使用字典格式化字符串：
当字符串中有很多变量的时候，可以用字典来对字符串进行格式化输出
# 字符串模板中使用key
temp = '教程是:%(name)s, 价格是:%(price)010.2f, 出版社是:%(publish)s'
book = {'name':'Python基础教程', 'price': 99, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name':'C语言小白变怪兽', 'price':159, 'publish': 'C语言中文网'}
# 使用字典为字符串模板中的key传入值
print(temp % book)
运行上面程序，可以看到如下输出结果：
教程是:Python基础教程, 价格是:0000099.00, 出版社是:C语言中文网
教程是:C语言小白变怪兽, 价格是:0000159.00, 出版社是:C语言中文网



2、推导式：
三层列表推导式
e_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(6)]
# e_list列表包含120个元素
print(e_list)

元组推导式：
a = (x for x in range(1,10))
for i in a:
    print(i,end=' ')
print(tuple(a))

字典推导式：
listdemo=['C语言中文网','c.biancheng.net']
new_dict={key:len(key) for key in listdemo}
print(new_dict)

交换现有的值:
olddict={'C语言中文网': 6, 'c.biancheng.net': 15}
new_dict={v,k for k, v in olddict.items() if v >0}
print(new_dict)


3、代码编写建议
不要写重复的代码
可以减少代码的层级，尽可能让 python 扁平化
函数的粒度要尽可能细，不要让一个函数做更多的事情



4.GIL 全局解释器锁：
每隔 15ms 进行抢断
有了 GIL 不一定能保证线程安全，因为python 有 check interval 的抢占机制，导致线程运行过程中会被强行打断
import threading
n = 0
def foo():
    global n
    n += 1
threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()
print(n)
执行此代码会发现，其大部分时候会打印 100，但有时也会打印 99 或者 98，原因在于 n+=1 这一句代码让线程并不安全。如果去翻译 foo 这个函数的字节码就会发现，它实际上是由下面四行字节码组成：
>>> import dis
>>> dis.dis(foo)
LOAD_GLOBAL              0 (n)
LOAD_CONST               1 (1)
INPLACE_ADD
STORE_GLOBAL             0 (n)
而这四行字节码中间都是有可能被打断的！所以，千万别以为有了 GIL 程序就不会产生线程问题，我们仍然需要注意线程安全。



5、垃圾回收机制
引用计数机制

查看函数的内存变化：
import os
import psutil
# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')


func()
show_memory_info('finished')

手动释放内存步骤：
1.del 相应的对象
2.执行gc.collect()

循环引用的问题： 标记清除算法  分代收集
本质就是图论来解决

缓存重用的问题：
范围在 [-5, 256] 之间的小整数	如果之前在程序中创建过，就直接存入缓存，后续不再创建。	全局
bool 类型
字符串类型数据
大于 256 的整数	     只要在本代码块内创建过，就直接缓存，后续不再创建。 	本代码块
大于 0 的浮点型小数
小于 0 的浮点型小数	  不进行缓存，每次都需要额外创建。



6、浮点数精度问题：
因为小数无法用二进制精确标示，舍弃的原则是“0 舍 1 入”

decimal   fractions  来处理精度问题


7、docstring 和注释的区别：
docstring可用 help(函数名) 来调取注释



8、冒泡排序：
data = [5,8,4,1]
for i in range(len(data)-1):
    for j in range(len(data)-i-1):
        if (data[j]) >data[j+1]:
            data[j],data[j+1]=data[j+a],data[j]
print(data)



















