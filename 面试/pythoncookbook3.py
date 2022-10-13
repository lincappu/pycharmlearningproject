# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os


# 一、数据结构和算法
#
# # 1.将序列分解
# 单个：
# a=[1,2,3]
# aa,b,c=a
# print(aa)
# print(b)
# print(c)
# 多个：
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)
#
# *middle这个是包括除了头尾的数据，
# *解压出来的永远是列表类型。
# 不能只用一个* 可以用*_



#2. 暴露最后N 个元素
from collections import  deque
def search(lines,pattern,history=5):
    preline=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,preline
        preline.append(line)

# if __name__ == '__main__':
#     with open('test','r') as f:
#         for line,preline in search(f,'SET',5):
#             for pline in preline:
#                 print(pline,end='')
#             print(line,end='')
#             print('-'*20)

'''
3、查找最大或者最小的N 个元素
利用 heapq 的堆模块的堆的特性
大根堆和小根堆：
大根堆就是逆序排列，小跟堆就是正序排列，
6 个函数：
函数                                        描 述
heappush(heap, x)                         将x压入堆中
heappop(heap)                             从堆中弹出最小的元素
heapify(heap)                             让列表具备堆特征
heapreplace(heap, x)                     弹出最小的元素，并将x压入堆中
nlargest(n, iter)                       返回iter中n个最大的元素
nsmallest(n, iter)                       返回iter中n个最小的元素

heappop(0) 永远得到的是最小的元素，
这种适用于数据量特别大的情况，当数据量小的时候也可以用排序加切片。
min() max() 
'''
import heapq
ums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(1,ums))

# heapq.heapify(ums)
# print(ums)


'''
1.5  实现优先级队列
'''
class PriorityQueue:
	def  __init__(self):
		self._queue=[]
		self._index=0
	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		# 这里为什么要弄一个三元组，因为 item 之间是不能比较的，这时候比较只能发生在前两项中。
		self._index += 1
	def pop(self):
		return heapq.heappop(self._queue)[-1]


class Item(object):
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

# a=(1,Item('foo'))
# b=(2,Item('bar'))
# print(a<b)

# (priority, index, item)




'''
1.6  字典健映射多个值
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
'''



'''
###字典
1、排序：
一个是 lamda 函数
一个是利用 collection 和 orderDict 类来实现，只是会保持插入的顺序，所以插入的时候要有序。
from  collections import OrderedDict
d=OrderedDict()
d['b']=1
d['a']=3
d['c']=2
print(d)
for key in d:
    print(key,d[key])


2、运算
字典的运算只能根据键来算，不能根据值来算，所以对字典的运算首先要反转键值，zip()，这反正是一次性的， 不能二次使用。

sort(zip(dict.keys,dict.values)) 完成排序

最大最小值：

min(dict,key=lambda x: dict[x])  # 这个 x 就是键



3、查找相同点：
& 相同点
-  不同点

只支持dict.item()和 dict.key（）方法，不支持 values 上的方法原因是，values 不保证互不相同，就会有问题丁要用就要先 set


4、删除相同元素并且保证有序：
最简单的方法肯定是直接 set（）一个集合，但是不能保证这个有序。
对于可以 hashlable 的元素直接 yield 进行返回，
对于不可 hashlabel 的元素要先转换为可 hashlabel 的元素进行比较。
'''

def diff(items,key=None):
	seen=set()
	for item in items:
		val=item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)
	print(seen)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

# print(list(diff(a,key=lambda d: (d['x'],d['y']))))
# print((list(diff(a, key=lambda d: d['x']))))


'''
切片函数：
slice(start,stop,step)
'''
a=slice(2,10,2)
print(a.indices(8))  # (2, 8, 2) 返回可切片的最大操作
s = 'HelloWorld'
for i in range(*a.indices(len(s))): # 这样就不会出现数组越界的问题
	pass

'''
排序一个字典类列表,
排序一个不能比较对象的时候也是用这种方式：
1、sorted()+lambda
2、利用operator模块的itemgetter函数， 这个会快点，并且可以同时比较多个字段。
'''
from operator  import itemgetter,attrgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname=sorted(rows,key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
by_name = sorted(rows, key=attrgetter('last_name', 'first_name'))
# print(rows_by_fname)
# print(rows_by_uid)





'''
二、字符串和文本

1、re.split()  可以同时使用多个分隔离进行分割：
line = 'asdf fjdk; afed, fjek,asdf, foo'
>>> import re
>>> re.split(r'[;,\s]\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
注意分组（） 如果，这个会输出分组内的内容
如果不想暴露切割的字符串在结果列表中，可以使用 (?:...) 的形式，如下：
re.split(r'(?:,|;|\s)\s*', line)
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


2、字符串开头或者结尾匹配
if name.startswith(('http:', 'https:', 'ftp:')): 数据必须是个元素，如果是列表也必须先转化为元组
if name.endswith(('http:', 'https:', 'ftp:')):


3、简单文件名模式匹配fnmatch 模块
匹配规则：
*	匹配所有
?	匹配任何单个字符
[seq]	匹配 seq 中的任何字符
[!seq]	匹配任何不在 seq 中的字符

fnmatch('Dat45.csv', 'Dat[0-9]*')

fnmatch（）这个大小写不敏感额，
fnmatchcase() 这个是大小写敏感的



字符串对其： ljust  rjust  center
合并字符串：.join



三、数字日期和事件

round(数字，精度)
数字的格式化输出：  format()  <>^
整数和字节之间的相互转化




四、迭代器和生成器

1.遍历可迭代对象： for  next()


五、文件与 IO

1.with open('somefile.txt', 'rt') as f:  读取文本里面有多种格式的文本数据
2.print 到文件中 print('Hello World!', file=f)
3.print 改变分隔符和行尾符：sep end
4.只有在文件不存在时候才写入数据，就是不允许覆盖 with open('somefile', 'xt') as f:   用 x 来代替 w
5.字符串的 IO操作，三类 io  textio  stringio  bytesio
6.压缩文件的操作：
import  gzip
import bz2

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

7.返回固定长度的文件迭代
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:





六、数据编码和处理



八、类与对象
1.__repr__ __str__
2. __slots__减少极大实例所占的内存，创建一个很小的紧凑的数组来构建，而不是为每个实例来定义一个字典。
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day

3.重新加载先前的模块，
>>> import spam
>>> import imp
>>> imp.reload(spam)
<module 'spam' from './spam.py'>
>>>
4.

'''












