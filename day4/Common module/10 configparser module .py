# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  configparser


# 针对 ini  cnf 配置文件的


# 查看：

# config=configparser.ConfigParser()
# config.read('my.cnf')
# print(config.sections())
# print(config.options('mysql'))
# print(config.items('mysql'))
# print(config.get('mysql','user'))  # get 获取的全部都是字符串
# print(type(config.getint('mysql','password')))
# print(type(config.getboolean('mysql','x')))
# print(type(config.getfloat('mysql','y')))


# 修改：

# config=configparser.ConfigParser()
# config.read('my.cnf')

# print(config.sections())
#
# config.add_section('egon')
# config.set('egon','user','root')
# config.set('egon','passwd','123')
# config.set('egon','age','18')  # 写的时候必须全部是字符串
# config.write(open('my.cnf','w'))


# config.remove_section('egon')
# config.remove_option('mysql','y')
#
# config.write(open('my.cnf','w'))  # 做修改  这条必须要有
#


# 判断是否存在

# config=configparser.ConfigParser()
# config.read('my.cnf')
#
#
# print(config.has_section('mysql'))
# print(config.has_option('mysql','y'))
#




