# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import json

import pymysql
import requests
import datetime
from mysql_basic import MysqlHelper

'''
爬取所有的澎湃号，和对应的主页url
'''

next_urls = []
user_list = []
user_dic = {}
user_dic_list = []


def pengpai():
    base_url = 'https://www.thepaper.cn/allGovUsers.jsp'

    response = requests.get(base_url)
    content = response.text.strip()
    node_dic = eval(content)

    for node in node_dic['nodeList']:
        # 澎湃号所在的省份
        user_provice = node['name']

        for user in node['userList']:
            # 澎湃号名称
            user_name = user['sname']
            user_name = user_name.strip()

            # 澎湃号主页url
            user_url = 'https://www.thepaper.cn/' + user['url']

            # 澎湃号id
            uid = user['userId']

            print("当前爬取的省份是：%s  澎湃号是: %s  url是: %s" % (user_provice, user_name, user_url))

            #
            user_dic = {}
            user_dic['name'] = user_name
            user_dic['url'] = user_url
            user_dic['provice'] = user_provice
            user_dic['uid'] = uid

            # 去除不完整的值
            if user_dic['name']:
                user_dic_list.append(user_dic)

        if node['nextUrl']:
            next_url = 'https://www.thepaper.cn/' + node['nextUrl']
            next_urls.append(next_url)
            print("目前的省份是：%s 开始翻页url是: %s" % (node['name'], next_url))

            get_info(node['name'], next_url, user_provice)


def get_info(node, next_url, user_provice):
    response = requests.get(url=next_url)
    content = response.text.strip()
    node_dic = eval(content)

    for user in node_dic['userList']:
        # 澎湃号名称
        user_name = user['sname']
        user_name = user_name.strip()

        # 澎湃号主页url
        user_url = 'https://www.thepaper.cn/' + user['url']

        # 澎湃号id
        uid = user['userId']

        print("当前爬取的省份是：%s  澎湃号是: %s  url是: %s" % (user_provice, user_name, user_url))

        user_dic = {}
        user_dic['name'] = user_name
        user_dic['url'] = user_url
        user_dic['provice'] = user_provice
        user_dic['uid'] = uid

        # 除去不完整的值
        if user_dic['name']:
            user_dic_list.append(user_dic)

    next_url = node_dic['nextUrl']
    if next_url:
        next_url = 'https://www.thepaper.cn/' + next_url
        get_info(node, next_url, user_provice)


def save_user_info():
    # 对结果去重
    seen=set()
    new_user_dic_list=[]
    for d in  user_dic_list:
        t=tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_user_dic_list.append(d)

    with  open('user_info.json', 'w', encoding='utf-8') as f:
        json.dump(new_user_dic_list, f, ensure_ascii=False)
    print("写入文件成功")
    #
    # with open('user_info.json', 'r', encoding='utf-8') as f:
    #     new_user_dic_list = json.load(f)


    # 初始化数库
    mysqlhelper = MysqlHelper()

    # 定义insert sql语句
    datetime_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_sql = "INSERT INTO pengpai.all_info(pengpai_name,url,provice,uid,crt_time) VALUES (%s,%s,%s,%s,%s)"

    # 插入数据库
    j = 1
    for user in new_user_dic_list:
        data = (user["name"], user["url"], user["provice"],user['uid'],datetime_now)
        mysqlhelper.exe(insert_sql, data)
        print('success insert:  %s' % j)
        j += 1


# pengpai()
# save_user_info()
# print(len(user_dic_list))
# print(len(user_list))




def cancel_delete_pengpai(select_dic_list):
    mysqlhelper = MysqlHelper()
    set_delete_sql = "UPDATE pengpai_info set deleted=0 WHERE pengpai_name=%s"
    j = 1
    for user in select_dic_list:
        data = (user["name"])
        mysqlhelper.exe(set_delete_sql, data)
        print('success insert:  %s' % j)
        j += 1





get_not_deleted_all_info()




def get_latest_url():
    mysqlhelper = MysqlHelper()
    select_sql = "SELECT pengpai_name,latest_url  from select_info where latest_url  is not NULL"
    res = mysqlhelper.all(select_sql)
    print(res)
    print(len(res))
    i = 1
    for r in res:
        name=r['pengpai_name']
        latest_url=r['latest_url']
        mysqlhelper = MysqlHelper()
        select_sql = "update  pengpai_info   set latest_url=%s  where pengpai_name=%s"
        data=(latest_url,name)
        mysqlhelper.exe(select_sql,data)
        print(i)
        i+=1





'''
从全部的澎湃号中提取出要爬取的澎湃号  
'''


def select_user():
    # 所有澎湃号的文件
    with  open('user_info.json', 'r', encoding='utf-8') as f1:
        s1 = json.load(f1)

    # 要选取的澎湃号名称文件
    with open('select.json', 'r', encoding='utf-8') as f2:
        s2 = f2.readlines()
        # print(len(s2))
        # print(type(s2))
        s2 = list(set(s2))
        # print(len(s2))

    select_dic_list = []
    for line1 in s1:
        for line2 in s2:
            line2 = line2.strip()
            if line2 == line1['name']:
                print("%s %s %s" % (line2, line1['name'], line1['url']))
                select_dic = {}
                select_dic['name'] = line2
                select_dic['url'] = line1['url']
                select_dic['provice'] = line1['provice']
                select_dic['uid'] = line1['uid']
                select_dic_list.append(select_dic)


    # # 保存到文件
    # with open('select_info.json', 'w', encoding='utf-8') as f:
    #     json.dump(select_dic_list, f, ensure_ascii=False)
    #
    # # 保存在数据库
    # mysqlhelper = MysqlHelper()
    # datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # insert_sql = "INSERT INTO pengpai.pengpai_info(pengpai_name,url,provice,uid,crt_time) VALUES (%s,%s,%s,%s,%s)"
    # j = 1
    # for user in select_dic_list:
    #     data = (user["name"], user["url"], user["provice"],user['uid'],datetime_now)
    #     mysqlhelper.exe(insert_sql, data)
    #     print('success insert:  %s' % j)
    #     j += 1

    cancel_delete_pengpai(select_dic_list)







# select_user()





















# db = pymysql.connect(host='rm-2zefb2z5vdsdpt14voo.mysql.rds.aliyuncs.com',
#                      port=3306,
#                      user='fanliusong',
#                      password='yJNDSDcUjIDADJHe',
#                      database='pengpai',
#                      charset='utf8mb4'
#                      )
#
# cursor = db.cursor()
# insert_sql = "INSERT INTO pengpai.select_info(pengpai_name,url,provice,uid) VALUES (%s,%s,%s,%s)"
#
# j = 1
# for user in select_dic_list:
#     data = (user["name"], user["url"], user["provice"],user['uid'])
#     cursor.execute(insert_sql, data)
#     print('success insert:  %s' % j)
#     j += 1
#
# db.commit()
# cursor.close()
# db.close()