# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  pymongo

from  bson.objectid import ObjectId

# 2.连接mongodb

# clinet=pymongo.MongoClient(host='123.57.152.184',port='27017')
# 等价于：

# client=pymongo.MongoClient('mongodb://123.57.152.184:27017')


# 待认证的登录
# client=pymongo.MongoClient('mongodb://123.57.152.184:27017')
# db=client.fls
# db.authenticate("fls", "icourt123456",mechanism='SCRAM-SHA-1')


# 也可以连接的时候带着认证信息：
MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
uri = "mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-256"
uri = "mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-1"

指定默认数据库和认证数据库：默认数据库：default_db 认证数据库：admin
uri = "mongodb://user:password@exampldefault_dbe.com/default_db?authSource=admin"


# 在连接中指定数据库
client=pymongo.MongoClient('mongodb://fls:icourt123456@123.57.152.184:27017/fls')


# 3.单独指定数据库：
db=client.fls

# db=client['fls']

# 4.指定集合
collection=db.stu
# collection=db['stu']

# 5.插入数据：
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }

# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
实际上在PyMongo 3.X版本中，insert()方法官方已经不推荐使用了，当然继续使用也没有什么问题，
官方推荐使用insert_one()和insert_many()方法将插入单条和多条记录分开。

result=collection.insert([student1,student2])
print(result)  # insert返回的是直接就是_id值


result=collection.insert_many([student1,student2])
print(result.inserted_ids)
这两个返回结果和insert()方法不同，这次返回的是InsertOneResult和InsertManyResult对象，我们可以调用其inserted_id属性获取_id。



# 6.查询：
# find_one: 返回单条数据   字典类型
# find() 返回的是生成器对象

根据属性值查询：
result=collection.find_one({'id':'20170101'})
print(result)

根据objectId查询，需要导入bson的objectId库
from bson.objectid import ObjectId
# result=collection.find_one({'_id': ObjectId('5ee2de6dcf406830c01a189d')})
# print(result)

操作符查询：
"""
比较符号含义示例
$lt小于{'age': {'$lt': 20}}
$gt大于{'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne不等于{'age': {'$ne': 20}}
$in在范围内{'age': {'$in': [20, 23]}}
$nin不在范围内{'age': {'$nin': [20, 23]}}
"""
"""
功能符号含义示例示例含义
$regex匹配正则{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$type类型判断{'age': {'$type': 'int'}}age的类型为int
$mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0
$text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
"""

# result=collection.find({'age':21})
# for  r in result:
#     print(r)

# result=collection.find({'age':{'$gt':20}})
# for  r in result:
#     print(r)



# 7.计数：
# count=collection.find({'age':21}).count()
# print(count)

# count=collection.count_documents({'age':21})
# print(count)


# 8.排序：可以调用sort方法，传入排序的字段及升降序标志即可
# result=collection.find().sort('name',pymongo.ASCENDING)
# print([r['name'] for r in result])

# result=collection.find().sort('name',pymongo.DESCENDING)
# print([r['name'] for r in result])


# 9.偏移,可能想只取某几个元素，在这里可以利用skip()方法偏移几个位置，比如偏移2，就忽略前2个元素，得到第三个及以后的元素。

# 跳过
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

# 获取限制
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])


# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出。此时可以使用类似如下操作来查询：
# from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})



# 10.更新：
con={'name':'Jordan'}
student=collection.find_one(con)
student['age']=25
result=collection.update(con,student)
print(result)
在这里我们将name为Kevin的数据的年龄进行更新，首先指定查询条件，然后将数据查询出来，修改年龄，之后调用update方法将原条件和修改后的数据传入，即可完成数据的更新。
# 运行结果：
{'ok': 1, 'nModified': 1, 'n': 1, 'updatedExisting': True}
返回结果是字典形式，ok即代表执行成功，nModified代表影响的数据条数。

另外update()方法其实也是官方不推荐使用的方法，在这里也分了update_one()方法和update_many()方法，用法更加严格，
第二个参数需要使用$类型操作符作为字典的键名，我们用示例感受一下。





复制数据库：

都未带认证
>>> from pymongo import MongoClient
>>> client = MongoClient('target.example.com')
>>> client.admin.command('copydb',
                         fromdb='source_db_name',
                         todb='target_db_name')

从另一个mongodb实例中拷贝到当前实例中，
>>> client.admin.command('copydb',
                         fromdb='source_db_name',
                         todb='target_db_name',
                         fromhost='source.example.com')

两个库都在认证，
>>> client = MongoClient('target.example.com',
...                      username='administrator',
...                      password='pwd')
>>> client.admin.command('copydb',
                         fromdb='source_db_name',
                         todb='target_db_name',
                         fromhost='source.example.com')










