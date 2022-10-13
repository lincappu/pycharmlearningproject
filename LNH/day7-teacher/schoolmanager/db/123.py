# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS





# import pickle
#
#
# with open('user_info.json','rb') as f:
#     red=pickle.load(f)
#     print(red)
#     print(type(red))


import  json

dic={}

a={'name':'1','age':11}
b={'name':'2','age':12}
c={'name':'3','age':13}
d={'name':'4','age':14}


with open('a', 'r+', encoding='utf-8') as f:
    json.dump(a,f)
    f.write('\n')
    json.dump(b,f)
    f.write('\n')

with open('a', 'a', encoding='utf-8') as f:
    json.dump(c,f)
    f.write('\n')