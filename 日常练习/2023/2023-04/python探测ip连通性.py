#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/4/4 11:25
# @Project  : pycharmlearningproject
# @File     : python探测ip连通性.py
'''
python探测ip的连通性的方法总结

'''

# 1、方法1
import re
import subprocess

def NetCheck(ip):
    try:
        p = subprocess.Popen(["ping -c 3 -w 3 " + ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = p.stdout.read().decode('utf-8')
        # print(out)
        # err=p.stderr.read()
        regex = re.compile('100% packet loss')
        # print out
        # print regex
        # print err
        if len(regex.findall(out)) == 0:
            print(ip + ': host up')
            return 'UP'
        else:
            print(ip + ': host down')
            return 'DOWN'
    except Exception as e:
        print('NetCheck work error:  %s' %e)
        return 'ERR'

# res=NetCheck('114.114.114.114')
# print(res)


# 2、ping3
from ping3 import ping,verbose_ping

if __name__ == '__main__':
    #  正常就是返回的时延，不通的话返回的时None
    second=ping('114.114.114.114',timeout=3)
    print(second)




