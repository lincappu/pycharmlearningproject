# !/usr/bin/env python3
# _*_coding:utf-8_*_




import  json


def db_conn():
    db_obj=json.load(open('db.json', 'r', encoding='utf-8'))
    return  db_obj


# dic=db_conn()
# print(dic['fd'])
dic={"egon": {"password": "123", "balance": 3000}, "alex": {"password": "alex3714", "balance": 4000}, "ysb": {"password": "dsb", "balance": 5000}}
json.dump(dic, open('db.json', 'w', encoding='utf-8'), indent=4)

