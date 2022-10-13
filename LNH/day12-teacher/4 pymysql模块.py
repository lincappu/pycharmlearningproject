# import pymysql
#
# conn=pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123',
#     database='db8',
#     charset='utf8'
# )
#
# cur=conn.cursor(cursor=pymysql.cursors.DictCursor)

# sql='''
# create table userinfo(
#   id int primary key auto_increment,
#   user char(16),
#   password char(20)
# );
# '''
# cur.execute(sql)


# sql='insert into userinfo(user,password) values("alex","123");'
# cur.execute(sql)
# sql='insert into userinfo(user,password) values("egon","123456");'
# cur.execute(sql)
# sql='insert into userinfo(user,password) values("wxx","123456");'
# cur.execute(sql)
# print(cur.lastrowid)


# sql='select * from userinfo;'
# rows=cur.execute(sql)
# print(rows)

#取查询结果
# print(cur.fetchone())
# print(cur.fetchmany(2))
# print(cur.fetchall())

# print(cur.fetchone())
# cur.scroll(0,'absolute')
# cur.scroll(1,'relative')
# print(cur.fetchone())


# cur.close()
# conn.commit()
# conn.close()





# import pymysql
#
# username=input('username>>: ').strip()
# password=input('password>>: ').strip()
#
# conn=pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123',
#     database='db8',
#     charset='utf8'
# )
#
# cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
# # sql='select * from userinfo where user="%s" and password ="%s"' %(username,password)
# # sql='select * from userinfo where user="xxx" or 1=1 -- aa" -- aa" and password ="";'
# #
# # sql='select * from userinfo where user=%s and password =%s'
# #
# # rows=cur.execute(sql,(username,password))
#
#
# sql='insert into userinfo(user,password) values(%s,%s)'
# cur.execute(sql,('yxx','123'))
# cur.executemany(sql,[('axx','123'),('bxx','123')])
#
#
# # if rows:
# #     print('登录成功')
# # else:
# #     print('账号或密码错误')
#
#
# cur.close()
# conn.commit()
# conn.close()
#







