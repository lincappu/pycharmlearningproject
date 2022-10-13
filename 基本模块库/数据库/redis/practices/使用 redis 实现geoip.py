# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import csv
import json
import redis


# print(int('1.1.1.1'.split('.')[1])*256*256*256) # 字符串和数字相乘的结果。

# 我擦。。。。。。。
def ip_to_socre(ip_address):
    score = 0
    for v in ip_address.split('.'):
        score = score * 256 + int(v, 10)
    return score


# res=ip_to_socre('2.4.5.1')

def import_blocks_to_redis(conn,filename):
    csv_file = csv.reader(open(filename, 'rt'))
    for count, row in enumerate(csv_file):
        start_ip = row[0].split('/')[0] if row else ''
        if 'i' in start_ip.lower():
            continue
        if '.' in start_ip:
            start_ip = ip_to_socre(start_ip)
        elif start_ip.isdigit():
            start_ip = int(start_ip, 10)
        else:
            continue

        city_id = row[1]+'_'+str(count)
        # print(start_ip, city_id)
        conn.zadd('ip2cityid:0302',city_id,start_ip)


conn=redis.Redis(host='123.56.144.211',port=6379,password='icourt12345',decode_responses=True,db=0)

import_blocks_to_redis(conn,'blocks.csv')


def import_cities_to_redis(conn, filname):
    for row  in csv.reader(open(filname,'rt')):
        city_id=row[0]
        continent=row[3]
        country=row[5]
        city_name=row[10]
        conn.hset('cityid2city',city_id,json.dumps([continent,country,city_name]))


