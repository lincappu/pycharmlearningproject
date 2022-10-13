# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  pymysql

# 1.pymysql 驱动引擎

db = pymysql.connect(host='35.236.152.207',
                     port=3306,
                     user='root',
                     password='iCourt12345',
                     database='python',
                     charset='utf8'
                     )


cursor=db.cursor()

item={
    'text_id': 123,
    'text_name':'book',
    'text_author':'fls',
    'text_type': '玄幻',
    'text_status': '连载',
    'text_latest': '进行',
    'text_intro':'fdfdsfdsfdfffsd',
}

sql = "INSERT INTO `python`.`text_info` (`text_id`, `text_name`, `text_author`, `text_type`, `text_status`, `text_latest`, `text_intro`) " \
      "VALUES ('" + item['text_id'] + "', '" + item['text_name'] + "', '" + item['text_author'] + "', '" + item['text_type'] + "', '" + item['text_status'] + "', '" + item['text_latest'] + "', '" + item['text_intro'] + "');"




create_database_sql="CREATE DATABASE IF NOT EXISTS  testdb2  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_unicode_ci;"



create_table_sql='''CREATE TABLE users (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
AUTO_INCREMENT=1 ;
'''


alter_table_sql='''ALTER TABLE users
	ADD COLUMN name VARCHAR(255)  NOT NULL,
	CHANGE COLUMN password pwd VARCHAR(255);
'''


inner_join='''SELECT  * FROM dept_manager INNER JOIN  employees  WHERE  dept_manager.emp_no=employees.emp_no;'''


left_join='''SELECT  * FROM dept_manager LEFT JOIN  employees   on dept_manager.emp_no=employees.emp_no;'''



sql = 'select * from dept_emp'
sql1 = "INSERT INTO `employees`.`departments`(`dept_no`, `dept_name`) VALUES ('d014', 'IT5')"


try:
    with db.cursor() as cursor:
        result = cursor.execute('select * from departments')


获取查询数据：
print('获取数据 {}:'.format(cursor.fetchone())) # 获取剩余结果的的第一行
print(format(cursor.fetchmany(4)))  # 获取剩余的前n行
print(cursor.fetchall())  # 获取剩余结果的的所有行


返回受影响的行数
effect_row=cursor.execute('select * from departments')
print(effect_row)

effect_row=cursor.execute("UPDATE departments SET dept_name='ITMm' WHERE dept_no='d010'")
print(effect_row)


executemany 插入数据
1.在写sql语句时,不管字段为什么类型,占位符统一使用%s,且不能加上引号
 sql="insert into tablename (id,name) values (%s,%s)"
2.添加的数据的格式必须为list[tuple(),tuple(),tuple()]或者tuple(tuple(),tuple(),tuple())
sql="insert into tablename (id,name) values (%s,%s)"

effect_row=cursor.executemany("INSERT INTO departments(dept_no, dept_name) VALUES(%s,%s)", [('d13','SQ'), ('d14', 'SE')])
new_id=cursor.lastrowid
print(new_id)
print(effect_row)


操作游标  (跳过的行数，位置)
cursor.execute('select * from departments')
cursor.scroll(2,'relative')
print(cursor.fetchone())



fetch的数据类型：转换为json格式的字典。
cursor.execute('select * from departments')
result=cursor.fetchall()
l=[]
for i,row in enumerate(result):
    dept_no=row[0]
    dept_name=row[1]
    data={'department number':dept_no,'department_name':dept_name }
    print(data)
    print(type(data))
    l.append(data)

print(l)

with open('emp.json','w',encoding='utf-8') as f:
    json.dump(l,f)


cursor.execute(create_table_sql)



执行存储过程
# cursor.execute('call showall()')
cursor.callproc('showall')
res=cursor.fetchall()
print(res)

cursor.execute(create_database_sql)




设置游标为字典类型： 获取的结果直接就是列表形式的字典。
    with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        # cursor.execute("select * from employees.departments")
        # res=cursor.fetchall()
        # print(res)

        cursor.execute('select version()')
        res=cursor.fetchall()
        print(res)

        db.commit()
except:
    db.rollback()



流式流标SSCursor和SSDictCursor
SSCursor和SSDictCursor被称为流式游标，这类游标不会像上面使用的Cursor和DictCursor那样，一次性返回所有的数据，流式游标会陆陆续续一条一条得返回查询数据，
所以这类游标适用于内存低、网络带宽小、数据量大的应用场景中。
import pymysql
import time
db = pymysql.connect(
                 host='rm-2zefb2z5vdsdpt14voo.mysql.rds.aliyuncs.com',
                 port=3306,
                 user='fanliusong',
                 password='yJNDSDcUjIDADJHe',
                 database='pengpai',
                 charset='utf8mb4',)


cursor=db.cursor(pymysql.cursors.SSCursor)
cursor.execute("select * from pengpai_info")
book=cursor.fetchone()
while book is not None:
    print(book)
    time.sleep(1)
    book = cursor.fetchone()





update查看影响行数：
cursor.execute(sql)
print(cursor.rowcount)
这个一点就是数量是随着fetch 增加的，所以要看全部就要fetchall一次，
















# 带上下文管理器版本的代码：

# mysql_with.py

class DB:
  def __init__(self,
         host='localhost',
         port=3306,
         db='itcast',
         user='root',
         passwd='123456',
         charset='utf8'):
    # 建立连接
    self.conn = connect(
      host=host,
      port=port,
      db=db,
      user=user,
      passwd=passwd,
      charset=charset)
    # 创建游标，操作设置为字典类型
    self.cur = self.conn.cursor(cursor=cursors.DictCursor)

  def __enter__(self):
    # 返回游标
    return self.cur

  def __exit__(self, exc_type, exc_val, exc_tb):
    # 提交数据库并执行
    self.conn.commit()
    # 关闭游标
    self.cur.close()
    # 关闭数据库连接
    self.conn.close()



客户端使用，
from mysql_with import DB

with DB() as db:
  db.execute("select * from student")
  ret = db.fetchone()
  print(ret)




