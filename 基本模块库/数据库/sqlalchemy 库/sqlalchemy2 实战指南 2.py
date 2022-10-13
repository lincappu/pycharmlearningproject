# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,DateTime, ForeignKey, Boolean, create_engine,insert,select,update,delete,CheckConstraint)
metadata = MetaData()
cookies = Table('cookies', metadata,
Column('cookie_id', Integer(), primary_key=True),
Column('cookie_name', String(50), index=True),
Column('cookie_recipe_url', String(255)),
Column('cookie_sku', String(55)),
Column('quantity', Integer()),
Column('unit_cost', Numeric(12, 2)),
CheckConstraint('quantity > 0', name='quantity_positive')
)
users = Table('users', metadata,
Column('user_id', Integer(), primary_key=True),
Column('username', String(15), nullable=False, unique=True),
Column('email_address', String(255), nullable=False),
Column('phone', String(20), nullable=False),
Column('password', String(25), nullable=False),
Column('created_on', DateTime(), default=datetime.now),
Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)
orders = Table('orders', metadata,
Column('order_id', Integer()),
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
engine = create_engine('sqlite:///:memory:')
metadata.create_all(engine)
connection = engine.connect()

# 3、异常和异常处理
from sqlalchemy.exc import IntegrityError
ins = insert(users).values(
    username="cookiemon",
    email_address="damon@cookie.com",
    phone="111-111-1111",
    password="password"
    )
try:
    pass
    # result = connection.execute(ins)
except IntegrityError as error:
    print(error.orig.message, error.params)
# 其他异常处理方法是一样的。


# 4.事务
# 简单的例子就是如果一个订单中有多个商品，但是其中某个商品没有货了，这样整个订单都不能成交。
# from sqlalchemy.exc import IntegrityError
# def ship_it(order_id):
#     s = select([line_items.c.cookie_id, line_items.c.quantity])
#     s = s.where(line_items.c.order_id == order_id)
#     transaction = connection.begin() # 事务开始
#     cookies_to_ship = connection.execute(s).fetchall()
#     try:
#         for cookie in cookies_to_ship:
#             u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
#             u = u.values(quantity = cookies.c.quantity-cookie.quantity)
#             result = connection.execute(u)
#         u = update(orders).where(orders.c.order_id == order_id)
#         u = u.values(shipped=True)
#         result = connection.execute(u)
#         print("Shipped order ID: {}".format(order_id))
#         transaction.commit()  # 事务提交
#     except IntegrityError as error:
#         transaction.rollback()   # 事务回滚
#         print(error)


#  5 反射
# 就是将本地数据库的数据反射到 sqlalchemy 对象中。可以用来做查询

# 6、ORM 模式  就是将 sql 对象作为 python 的对象处理，这个和 core 是完全两套处理语法


# 7、alembic 数据迁移工具






















