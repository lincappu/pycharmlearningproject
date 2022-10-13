# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import pymysql
import os
import sys
import PIL

# 数据库实例列表
# hw-test-rds
db1 = pymysql.connect(host='110.238.80.112',
					  port=3306,
					  user='root',
					  password='PObo_Et18ZgYjZQ18',
					  database='ztestdb',
					  charset='utf8mb4')

cursor1 = db1.cursor()

''' 1、python 往 mysql 插入图片，bolb类型字段'''
# 注意：blob 默认只能是 65kb 的图片，需要 medblob 或者是 longblob 数据
# 写入图片
with open('5.png', 'rb') as f:
	img = f.read()
	f.close()
sql = 'insert into ztestdb.images (id,image) values (%s,%s);'
args = (5, img)
cursor1.execute(sql, args)
db1.commit()
cursor1.close()
db1.close()

# 取出图片，
with open('6.phg', 'wb') as img:
	cursor1.execute('select * from ztestdb.images where id =5;')
	g = cursor1.fetchone()[1]
	img.write(g)

