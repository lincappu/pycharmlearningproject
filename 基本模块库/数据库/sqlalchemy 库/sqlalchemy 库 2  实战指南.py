# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from sqlalchemy import Table, Column,Numeric, String,Integer, create_engine,MetaData,DateTime,Boolean,ForeignKey
import  pymysql

from   datetime import  datetime

from sqlalchemy import insert,select,update,delete
from sqlalchemy import   and_,or_,not_

from sqlalchemy import PrimaryKeyConstraint,UniqueConstraint,CheckConstraint,ForeignKeyConstraint

metadata=MetaData()

cookies = Table('cookies', metadata,
Column('cookie_id', Integer(), primary_key=True),
Column('cookie_name', String(50), index=True),
Column('cookie_recipe_url', String(255)),
Column('cookie_sku', String(55)),
Column('quantity', Integer()),
Column('unit_cost', Numeric(12, 2))
)

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now,    onupdate=datetime.now)
)

orders = Table('orders', metadata,
Column('order_id', Integer(), primary_key=True),
Column('user_id', ForeignKey('users.user_id')),
Column('shipped', Boolean(), default=False)
)

line_items = Table('line_items', metadata,
Column('line_items_id', Integer(), primary_key=True),
Column('order_id', ForeignKey('orders.order_id')),
Column('cookie_id', ForeignKey('cookies.cookie_id')),
Column('quantity', Integer()),
Column('extended_cost', Numeric(12, 2))
)
engine=create_engine('mysql+pymysql://root:icourt12345@39.96.213.91:3306/fls?charset=utf8mb4',
                     echo=True,
                     max_overflow=10)
# metadata.create_all(engine)  # 持久化，就是创建表到数据库中，

conn=engine.connect()  # 拿到这个数据库的连接


# 1.3.2 定义键和约束：
# 1.是在定义列后面设置
# primary_key=true也可以设置多个来设置符合主键
# 2.就是使用元组来显示创建
# PrimaryKeyConstraint('user_id', name='user_pk')
# UniqueConstraint('username', name='uix_username')
# CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')
# 1.3.3  索引
# Index('ix_cookies_cookie_name', 'cookie_name',unique=True)
# 函数索引：
# Index('ix_test', mytable.c.cookie_sku, mytable.c.cookie_name))  # 这种写法是实际的列，而不是字符串的形式。



# CRUD操作
#1.insert
# 两种插入方法：
# 一种是表名.insert().values()
# 一种是函数 insert（表名）.values()

ins=insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)

# res=conn.execute(ins)

# 插入多条记录
ins=cookies.insert()

inventory_list = [
{
'cookie_name': 'peanut butter',
'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
'cookie_sku': 'PB01',
'quantity': '24',
'unit_cost': '0.25'
},
{
'cookie_name': 'oatmeal raisin',
'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
'cookie_sku': 'EWW01',
'quantity': '100',
'unit_cost': '1.00'
}
]

# result = conn.execute(ins, inventory_list)
# print(result)


# 2 查询
s=select([cookies])
rp=conn.execute(s)
# res=rp.fetchall()
# print(res.items)
# 上面这个方法就是按照全部列的顺序每行为一个元组，全部一读出。


# 节省内存的读法： resultproxy方法
s=select([cookies.c.cookie_name,cookies.c.cookie_recipe_url]).where(cookies.c.cookie_name=='chocolate chip')
s = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])  # +运算符

# 布尔运算，尽量不要用布尔运算，用连接词查询，

# 连接词查询
s = select([cookies]).where(
and_(
cookies.c.quantity > 23,
cookies.c.unit_cost < 0.40
)
)


s=s.order_by(cookies.c.cookie_name)
s=s.limit(2)


# for record in conn.execute(s):
#     print(record.cookie_name,record.cookie_recipe_url)
    # print(record)
    # print(record.items)

# 其他的方法
# between(cleft, cright) 查找在 cleft 和 cright 之间的列
# concat(column_two) 连接列
# distinct() 查找列的唯一值
# in_([list]) 查找列在列表中的位置
# is_(None) 查找列 None 的位置（通常用于检查 Null 和 None）
# contains(string) 查找包含 string 的列（区分大小写）
# endswith(string) 查找以 string 结尾的列（区分大小写）
# like(string) 查找与 string 匹配的列（区分大小写）
# startswith(string) 查找以 string 开头的列（区分大小写）
# ilike(string) 查找与 string 匹配的列（不区分大小写）


# 3、更新数据
u=update(cookies).where(cookies.c.cookie_name=='chocolate chip')

u=u.values({
    cookies.c.cookie_name:'chocolate ccccchip',
    cookies.c.cookie_sku:'CC001',
})
# res=conn.execute(u)
# print(res.rowcount)


# 4. 删除数据   只接受一个 where 语句
u=delete(cookies).where(cookies.c.cookie_name=='peanut butter')
# res=conn.execute(u)
# print(res.rowcount)



# 添加剩余的数据：
customer_list = [
{
'username': 'cookiemon',
'email_address': 'mon@cookie.com',
'phone': '111-111-1111',
'password': 'password'
},
{
'username': 'cakeeater',
'email_address': 'cakeeater@cake.com',
'phone': '222-222-2222',
'password': 'password'
},
{
'username': 'pieguy',
'email_address': 'guy@pie.com',
'phone': '333-333-3333',
'password': 'password'
}
]

# ins=users.insert()
# res=conn.execute(ins,customer_list)

ins=insert(orders).values(user_id=1,order_id=1)
# res=conn.execute(ins)

ins=insert(line_items)
order_items=[
    {
    'order_id': 1,
    'cookie_id': 1,
    'quantity': 2,
    'extended_cost': 1.00
    },
    {
    'order_id': 1,
    'cookie_id': 3,
    'quantity': 12,
    'extended_cost': 3.00
    }
]

# res=conn.execute(ins,order_items)


ins = insert(orders).values(user_id=2, order_id=2)
# result = conn.execute(ins)
ins = insert(line_items)
order_items = [
{
'order_id': 2,
'cookie_id': 1,
'quantity': 24,
'extended_cost': 12.00
},
{
'order_id': 2,
'cookie_id': 4,
'quantity': 6,
'extended_cost': 6.00
}
]
# result = conn.execute(ins, order_items)



# 连接查询 join、 outer join
cookies_order=select([orders.c.order_id, users.c.username, users.c.phone,cookies.c.cookie_name, line_items.c.quantity,line_items.c.extended_cost]).select_from(
    orders.join(users).join(line_items).join(cookies)).where(users.c.username =='cookiemon')


res=conn.execute(cookies_order).fetchall()
for row in res:
    print(row)


# group_by 分组
# count() 计数




# 2.9 原始查询  就是真正的 sql 语句来查询 这个比较少用
# ﻿result = connection.execute("select * from orders").fetchall()
# print(result)


# 部分文本查询： 就是字符串查询，就是符合sql 语句的写法。
# ﻿from sqlalchemy import text
# stmt = select([users]).where(text("username='cookiemon'"))
# print(connection.execute(stmt).fetchall())
















