# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:icourt12345@39.96.213.91:3306/fls?charset=utf8mb4',
                       echo=True,
                       max_overflow=10)
# 申明映射 第一种方式
base = declarative_base()


class Teacher(base):
    __tablename__ = 'teacher'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    city = Column(String(20))

    def __repr__(self):
        tpl = 'Teacher (id={}, name={}, age={}, city={}'
        return tpl.format(self.id, self.name, self.age, self.city)


# # 第二种方式：模式申明，通过__table__来映射
# metadata = MetaData()
# user=Table('user', metadata,
#            Column('id', Integer, primary_key=True),
#            Column('name', String(50)),
#            Column('fullname', String(50)),
#            Column('password', String(12))
#            )
#
# class User(object):
#     def __init__(self, name, fullname, password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password
#
# mapper(User,user)

# MetaData 创建表到数据库中
# Teacher.metadata.create_all(engine)


# 将当前的引擎帮定给这个会话，
dbsesssion = sessionmaker(bind=engine)

# 如果还没有这个引擎，可以先创建这个会话，然后在绑定引擎
# dbsesssion=sessionmaker()
# dbsesssion.configure(bind=engine)

#  上面创建的是个类 ，需要实例化
dbs = dbsesssion()

# 1.添加数据
new_uer = Teacher(id='100', name='fls', age=20, city='beijing')

# 添加到 session
# dbs.add(new_uer)


# 1、添加和更新对象
# select_user=dbs.query(Teacher).filter_by(name='fls').limit(10)
# print(select_user)

# new_uer2=Teacher(id='101',name='f',age=30,city='beijing2')
# dbs.add(new_uer2)   # 只要 add 以后实际上数据已经别挂起了，说白了就是在内存中已经生效了，只是还没有写入而已，包括以后针对数据的修改都是实时生效的， 只不过在最后才写入，
# select_user2=dbs.query(Teacher).filter_by(name='f').first()
# print(select_user2)

# new_uer2.age=40
# select_user2=dbs.query(Teacher).filter_by(name='f').first()
# print(select_user2)

# print(dbs.dirty)
# print(dbs.new)  # 新修改的但没提交的数据
#
# dbs.commit()  # 提交数据
# print(new_uer2.id)  #  id 值    行号  这个不标示第多少行， 除非是自增


# 2、回滚：回滚 . 操作和 add的操作
# new_uer.name='flsfls'
# print(new_uer.name)
# new3=Teacher(id='102',name='f3',age=60,city='beijing4')
# dbs.add(new3)
#
# s2=dbs.query(Teacher).filter_by(name='f3').all()
# print(s2)
#
# dbs.rollback()

# 3、查询 格式
for instance in dbs.query(Teacher).order_by(Teacher.id):
    print(instance.name, instance.age)

for name, fullname in dbs.query(User.name, User.fullname):
    print(name, fullname)

# 常用的筛选器运算符
filter()
的基础上进行操作

equals ：：
query.filter(User.name == 'ed')

not equals ：：
query.filter(User.name != 'ed')

LIKE ：：
query.filter(User.name.like('%ed%'))

ILIKE （不区分大小写，例如）：：
query.filter(User.name.ilike('%ed%'))

IN ：：
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# works with query objects too:
query.filter(User.name.in_(
    session.query(User.name).filter(User.name.like('%ed%'))
))

NOT
IN ：：
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))

IS
NULL ：：
query.filter(User.name == None)
# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None)

IS
NOT
NULL ：：
query.filter(User.name != None)
# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))

AND ：：
# use and_()
from sqlalchemy import and_

query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

OR ：：
from sqlalchemy import or_

query.filter(or_(User.name == 'ed', User.name == 'wendy'))
注解
确保使用
or_()
和
not Python or 接线员！

MATCH ：：
query.filter(User.name.match('wendy'))

返回的列表和变量：
all()
返回一个列表：

>> > query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
SQL >> > query.all()
[ < User(name='ed', fullname='Ed Jones', nickname='eddie') >,
< User(name='fred', fullname='Fred Flintstone', nickname='freddy') >]

first()
应用一个限制并以标量形式返回第一个结果：

SQL >> > query.first()
< User(name='ed', fullname='Ed Jones', nickname='eddie') >

one()
完全获取所有行，如果结果中不存在一个对象标识或复合行，则会引发错误。找到多行时：

>> > user = query.one()
Traceback(most
recent
call
last):
...
MultipleResultsFound: Multiple
rows
were
found
for one()
找不到行：

>> > user = query.filter(User.id == 99).one()
Traceback (most recent call last):
    ...

NoResultFound: No
row
was
found
for one()
这个 one() 对于希望处理“未找到项目”和“找到多个项目”不同的系统来说，方法是很好的；例如RESTful Web服务，它可能希望在未找到结果时引发“404未找到”，但在找到多个结果时引发应用程序错误。

one_or_none() 就像 one() ，但如果没有找到结果，则不会引发错误；它只是返回 None.喜欢 one() 但是，如果发现多个结果，则会引发错误。


scalar() 调用 one() 方法，并在成功时返回行的第一列：

>> > query = session.query(User.id).filter(User.name == 'ed'). \
        ...order_by(User.id)
SQL >> > query.scalar()


文本 sql:
    计数：count（）

# 关闭 session
# dbs.close()


# 连接池的概念
