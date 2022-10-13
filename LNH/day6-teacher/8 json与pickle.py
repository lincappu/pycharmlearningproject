'''
Json模块主要用来进行Python对象的序列化和反序列化。
该模块中常用的方法有以下四个：
json.dump 将Python对象序列化为Json格式的数据流并写入文件类型的对象中
json.dumps 将Python对象序列化为Json格式的字符串
json.load从文件类型的对象中读取Json格式的数据并反序列化成Python对象
json.loads  将包含Json格式数据的字符串反序列化成Python对象

'''

import json
import pickle
import shelve
import datetime

''' json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
下面是  dumps 关键字参数'''

#  skipkeys=False 是否跳过要序列化的对象中字典元素的key不是基本类型的数据；如果为True，则跳过，如果为False，将抛出TypeError异常，必须是 python 的基础数据类型，不能是 bytes 类型

emp_info = {
    'name': 'bob',
    b'age': 24,
}
# json.dumps(emp_info)


# ensure_ascii=True   是否将要序列化的对象中的字符串中的非ascii字符进行转义。如果该参数为True，则将字符串中的非ascii字符转义成unicode字符串，否则，将不会进行转义。

message = '我爱 python3'
res1 = json.dumps(message)
# print(res1)
res2 = json.dumps(message, ensure_ascii=False)
# print(res2)

# loads 出来是一样的
# r1=json.loads(res1)
# print(r1)
# r2=json.loads(res2)
# print(r2)


# check_circular=True 是否进行容器类型的循环引用检查。如果该参数设置为False，则不进行检查，但是可能会引发OverflowError或更严重的情况。如果该参数设置为True，则将进行容器类型的循环引用检查，并在发现循环引用时抛出异常。
emp_dict = {
    'id': 1,
    'dtpt': 'sales',
}
emp_dict['info'] = emp_dict
# json.dumps(emp_dict,check_circular=False)


# allow_nan=True 是否允许序列化超出范围的float类型的值（如float('inf')、float('-inf')、float('nan')）。如果该参数设置为True，则上面列出的那些值将依次使用JavaScript中等价的值（Infinity、-Infinity、NaN）来进 行替代；如果该参数设置为False，并且要序列化的对象中出现了那些超出范围的值，则将引发ValueError异常

num_list = [2, 5, float('inf'), float('-inf'), float('nan')]
res = json.dumps(num_list)
# print(res)

# res2=json.dumps(num_list,allow_nan=False)
# print(res2)


# indent=None 是否在数组元素和对象成员前增加缩进以便使格式更加美观。如果该参数设置为大于等于1的整数，则添加换行符和对应数量的空格表示缩进，如果设置为0，则表示只添加换行符，如果设置为None，则表示无缩进。
response = {'status': 'success', 'code': 200, 'data': ['002', 'json', 5000]}
# print(json.dumps(response,indent=4))



# separators=None 设置Json中各项之间、对象的键和值之间的分隔符；该参数必须是一个2元组，元组第一个元素表示Json数据中各项之间的分隔符，元组的第二个元素表示Json对象的键和值之间的分隔符。默认的分隔符为（’,’, ‘:’）

response = {'status': 'success', 'code': 200, 'data': ['002', 'json', 5000]}
# print(json.dumps(response, indent=4, separators=(';', '!')))



# default=None  指定一个函数，用来将不可进行序列化的Python对象转化为可序列化的Python对象。
# json.dumps(b'hello world')
json.dumps(b'hello world', default=list)  # '[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]'
json.dumps(b'hello world', default=str)  # '"b\'hello world\'"'

# sort_keys=False 是否要将对象中字典元素按照key进行排序。默认为False，即不进行排序，若指定为True，则会进行排序。
emp_info = {'name': 'bob', 'age': 23, 'dept': 'sales', 'gender': 'male'}
# print(json.dumps(emp_info, indent = 4, sort_keys=True))



#  cls=None  指定一个定制的JSONEncoder的子类（例如，重写了.default()方法用来序列化附加的类型），指定该参数时请使用cls关键字参数。如果未指定该参数，则将使用默认的JSONEncoder。


# 非字符串类型作为键名 key：  在Python中, 只有可哈希(hashable)的对象和数据都可以做为Dictionary对象的键, 而JSON规范中则只能使用字符串做为键名. 所以在json.dumps的实现中, 对这个规则进行了检查, 不过键名允许的范围有所扩大, str, int, float, bool和None类型的数据都可以做为键名. 不过当键名非str的情况时, 键名会转换为对应的str值
json.dumps(
    {
        'str': 'str',
        123: 123,
        321.54: 321.54,
        True: True,
        False: False,
        None: None
    }
)
# json转化后的效果：'{"str": "str", "123": 123, "321.54": 321.54, "true": true, "false": false, "null": null}' 但是当python 中出现一个非基础类型数据做键名时，json 就会报错，如下：
# print(json.dumps({(1, 2): 123}))  # 元组类型作为 key

d = {'a': 1}

# print(type(json.dumps(d)))  # dumps 后默认是 str 类型
# with open('1.json','w') as f:
#     f.write(json.dumps(d))

# with open('2.json','r') as f:
#     data=f.read()
#     print(json.loads(data)['a'])

# s_json=json.dumps(d)
# print(s_json,type(s_json))
# print(json.loads(s_json)['a'])





####json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

# loads 字符串类型
# print(json.loads("{'name':1}")['name']) #报错   在 Python中字符串放在单引号和双引号里效果是一样的， 但是在 json 中，字符串数据必须放在双引号中，不能放在单引号中。
# print(json.loads('{"name":1}')['name'])
# print(json.loads("{\"name\":123}")) # 如果 python字符串也是在双引号中，那么 json 中的双引号就要转义。

# loads  bytes 和 bytearray 类型的数据
# print(type(json.loads('{"name":"fls"}'.encode('utf-8'))))
# print(type(json.loads(bytearray('{"name":"fls"}', 'utf-8'))))



# l=[1,2,3,'a']
#
# print(json.loads('[1,2,3,"a"]')[1])

# json.dump(d,open('3.json','w'))
# print(json.load(open('3.json','r'))['a'])




'''JSON解码和编码类实现json.loads, json.load, json.dumps和json.dump这四个方法是通过json.JSONDecoder和json.JSONEncoder这两个类来完成各自的任务的. 所以也可以直接使用这两个类来完成前文描述的功能:
>>> json.JSONDecoder().decode('{"a": 123}')
{'a': 123}
>>> json.JSONEncoder().encode({'a': 123})
'{"a": 123}'
'''

####  pickle 模块
'''pickle模块与json模块的对比
pickle模块实现的二进制转换协议与json模块实现的JSON格式转换协议完全不同。
JSON格式是一个文本序列化格式。pickle字节流格式是一个二进制序列化格式。
JSON是人可读的，而pickle字节流无法供人阅读。
JSON多用于与外部其他系统的交互，而pickle字节流仅供Python内部读写。
JSON只能表示Python内置类型，而pickle字节流可以表示开发人员定制类型。

pickle.dump(obj, file, [,protocol]) 
   含义：pickle.dump（对象，IO 及异步 IO及协程，[使用协议]）
   使用有3种协议，索引0为ASCII，1为旧式二进制，2为新式二进制协议，不同之处在于2要更高效一些。默认dump方法使用0做协议。
   
pickle.load(file) 
   含义：pickle.load(IO 及异步 IO及协程)，将file中的对象序列化读出。
    
'''

# d={'a':1}
# d_pkl=pickle.dumps(d)
# # print(d_pkl,type(d_pkl))
# with open('1.pkl','wb') as f:
#     f.write(d_pkl)
#

# pickle.dump(d,open('2.pkl','wb'))


# x=pickle.load(open('2.pkl','rb'))
# print(x,type(x))


# def func():
#     print('from 序列表.py')



# json.dumps(func)

# print(pickle.dumps(func))

# pickle.dump(func,open('3.pkl','wb'))

# def func():
#     print('==================>')
#
# f=pickle.load(open('3.pkl','rb'))
#
# f()




'''
shelve模块:
在python3中我们使用json或者pickle持久化数据，能dump多次，但只能load一次，因为先前的数据已经被后面dump的数据覆盖掉了。如果我们想要实现dump和load多次，可以使用shelve模块。shelve模块可以持久化所有pickle所支持的数据类型。shelve只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。可以像字典一样使用get来获取数据等。

shelve模块是一个简单的key，value将内存数据通过文件持久化的模块。
shelve就是pickle模块的一个封装。


shevle.open(filename, flag='c', protocol=None, writeback=False):
flag=c 读写模式
flag=r 只读模式


shevle 中 key 必须是字符串，value 可以是所有python 支持的类型


'''

info = {
    'name': 'fls',
    'age':22,
}

name = ['Apoll', 'Zous', 'Luna']


t=datetime.datetime.now()

# with shelve.open('shevle.txt') as f:
#     f['name']=name
#     f['info']=info
#     f['time']=t
#
# with  shelve.open('shevle.txt') as f:
#     n=f.get('name')



# shevle 拷贝机制，就是当查看一个 key 的时候，实际是上先拷贝出来一份在缓存中，看到的值是拷贝的值，所以对这个 key 的修改，实际上是对这个key 的拷贝的修改，而且最后这个值默认是不回写的，所以也就没有保存. 所以需要加writeback=True 这个参数才能保存
lis=['a','b','c']
db1=shelve.open('shevle.db2')
# db1=shelve.open('shevle.db2',writeback=True)
db1['lis']=lis
db1['lis'].append('d')
print(db1['lis'])  # 这个时候 d 并不存在，




# 但是如果是直接对 d[key]=data 这种修改，视为直接存储数据，这个时候修改是源数据，而不是拷贝的数据，所以修改能字节保存。 和上面的并不冲突。
res1=shelve.open('shevle.txt')
res1['info']['name']='AAAA'
print(res1.get('info'))
res1.close()


