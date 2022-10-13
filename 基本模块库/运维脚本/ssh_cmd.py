# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import os
import sys
import time
import argparse
import datetime
import logging
import paramiko
import math

'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

以上是python2的写法，但是在python3中这个需要已经不存在了，这么做也不会什么实际意义。
在Python2.x中由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换。
在python3中有了明确的str和byte类型区别，从一种类型转换成另一种类型要显式指定encoding。

但是仍然可以使用这个方法代替
import importlib,sys
importlib.reload(sys)
'''

m = {
	'host': '172.16.1.146',
	'port': 10222,
	'user': 'root',
	'password': 'wbBiloHn7#Khpibk'
}

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)s: %(message)s',
	datefmt='%Y%m-%d %H:%M:%S %p',
	filename='ssh.log',
	level=logging.DEBUG,
	filemode='a',
)


# 刚好是 format 和%s 的两种输出方式
def G(s):
	return "\033[1;31m{:#^30}\033[0m".format(s)

# def G(s):
# 	return "%s\033[1;31m %s \033[0m%s" % (chr(35), s, chr(35))


def E(s):
	return "%s\033[1;32m %s\033[0m%s" % (chr(35), s, chr(35))


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def exec_cmd(m, command):
	if m['host'] == '' or m['password'] == '':
		logging.error('主机 ip 地址和密码必须填写，程序退出')
		sys.exit(1)
	elif m['port'] == '':
		m['port'] = '22'
	elif m['user'] == '':
		m['user'] = 'root'
	logging.info('要连接的信息如下：%s' % m)

	try:
		ssh.connect(hostname=m['host'], port=m['port'], username=m['user'], password=m['password'])
		stdin, stdout, stderr = ssh.exec_command(command)
		result = stdout.read()
		if len(result) != 0:
			result = str(result).replace('\\n', '\n')
			'''
			#  "Mounted on\ndevtmpfs "    
			能看到\n，并且没有换行，肯定是因为\n 被转义了，还是不熟练
			'''
			result = result.replace("b'", "").replace("'", "")
			return result
		else:
			return None

	except Exception as e:
		print(e)
		logging.error(e)


# 获取磁盘空间利用率并按字典形式返回
def AllDiskSpace(m):
	ref_dict = {}
	cmd_dict = {"Linux\n": "df | grep -v 'fs' | grep 'dev' | awk '{print $1\":\"$5}'",
				"AIX\n": "df | grep -v 'Filesystem' | awk '{print $4 \":\" $7}'"
				}  # 一是因为uname 获取到的就是一个 Linux 后面本身就有一个空行,第二个是为了转义，是为了在执行的时候本身就要带着"" 号。哎，还是写代码写的太少了

	os_version = exec_cmd(m, 'uname')
	print(os_version)
	for version, run_cmd in cmd_dict.items():
		if version == os_version:
			os_ref = exec_cmd(m, run_cmd)
			print(os_ref)
			ref_list = os_ref.split('\n')
			for each in ref_list:
				if each != "":
					ref_dict[str(each.split(':')[0])] = str(each.split(':')[1])
	return ref_dict


# res=AllDiskSpace(m)
# print(res)


#  获取系统内存利用率：
def memusage(m):
	ref_dict = {}
	cmd_dict = {
		"Linux\n": "cat /proc/meminfo | head -n 3 | awk '{print $2}' | xargs | awk '{print $1 \":\" $2 \":\" $3}'",
		"AIX\n": "df | grep -v 'Filesystem' | awk '{print $4 \":\" $7}'"
		}

	os_version = exec_cmd(m, 'uname')
	for version, run_cmd in cmd_dict.items():
		if version == os_version:
			os_ref = exec_cmd(m, run_cmd)
			print(os_ref)
			mem_total = math.ceil(int(os_ref.split(':')[0]) / 1024 / 1024)
			mem_free = math.ceil(int(os_ref.split(':')[1]) / 1024 / 1024)
			mem_available = math.ceil(int(os_ref.split(':')[2]) / 1024 / 1024)
			mem_used = str(int(mem_total) - int(mem_available))
			used_percent = str(math.floor(int(mem_used) / int(mem_total) * 100))

			print(G('当前机器是 %s' %(m['host'])))
			print("内存总计空间: {}".format(str(mem_total) + " GB"))
			print("内存剩余空间: {}".format(str(mem_free) + " GB"))
			print("内存可用空间: {}".format(str(mem_available) + " GB"))
			print("内存利用率: {}".format(str(used_percent) + " %"))

# memusage(m)



# 获取进程信息  逻辑是一样的，

#



