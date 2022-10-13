# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  urllib3


from json import load
'''
分为两类：
1、是直接返回 ip
2、返回地理信息
3、根据 ip 查询 ip 信息
'''

http=urllib3.PoolManager()
response=http.request('GET','http://ip.42.pl/raw')
print(response.status,response.data.decode('utf-8'))



# my_ip = load(urlopen('http://jsonip.com'))['ip']
# print 'jsonip.com', my_ip
#
# from json import load
# from urllib2 import urlopen
#
# my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
# print 'httpbin.org', my_ip
#
# from json import load
# from urllib2 import urlopen
#
# my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
# print 'api.ipify.org', my_ip




#

