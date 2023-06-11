#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/1/6 16:13
# @Project  : pycharmlearningproject
# @File     : 快速生成文件.py

import pymysql
import sshtunnel

db = [
    "'action_db'",
    "'admin_db'",
    "'app_db'",
    "'basic_db'",
    "'cash_db'",
    "'config_db'",
    "'crawler_db'",
    "'credit_db'",
    "'decision_engine'",
    "'default_db'",
    "'information_schema'",
    "'job_db'",
    "'mysql'",
    "'nacos_db'",
    "'outside_db'",
    "'risk_db'",
    "'urge_db'",
    "'urge_db_ft'",
    "'yearning'"]


def mysql_conn():
    proxy_host = sshtunnel.SSHTunnelForwarder(ssh_address_or_host=('110.238.83.48', 22),
                                              ssh_username='myrds-only',
                                              ssh_password='owGNFLOk73fEW',
                                              remote_bind_address=('172.30.10.250', 3306))

    proxy_host.start()
    db1 = pymysql.connect(host='127.0.0.1',
                          port=proxy_host.local_bind_port,
                          user='root',
                          passwd='K$LW9qOGcrGK$RXK',
                          db='credit_db',
                          charset='utf8')
    # with db1.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
    cursor = db1.cursor()
    return cursor


cursor = mysql_conn()

db_list = []
db_table_list = []

all_db_sql = "select CONCAT('%s')  as '数据库' , sum(table_rows) as '记录数' , concat(round(sum(data_length/1024/1024),2),'MB') as  '数据容量' , concat(round(sum(index_length/1024/1024),2),'MB') as  '索引容量' from  information_schema.tables  where  table_schema= '%s';"
all_tabl_sql="SELECT CONCAT('%s') as '数据库' , CONCAT('%s') as '表名' ,table_rows as '记录数', concat(ROUND(SUM(data_length / 1024 / 1024), 2), 'MB') AS  '数据容量' ,concat(round(sum(index_length/1024/1024),2),'MB') as  '索引容量' FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s';"


db_sql = "show databases"
table_sql = "select table_name from information_schema.tables where table_schema= '%s' ;"

cursor.execute(db_sql)
db = cursor.fetchall()
for d in db:
    for d1 in d:
        print(d1)
        db_list.append(d1)
print(db_list)

# for d in db_list:
#     print(all_db_sql %(d,d))

for dbb in db_list:
    full_table_sql = table_sql % (dbb)
    cursor.execute(full_table_sql)
    dbtable = cursor.fetchall()
    for table in dbtable:
        for tab in table:
            d_t = "'" + dbb + "'" + "." + "'" + tab + "."
