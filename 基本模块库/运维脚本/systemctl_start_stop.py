# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import psutil
import logging
import os
import subprocess
import time
import re
import datetime
import getpass
import sys

def G(s):
	return "%s\033[1;32m %s%s \033[0m" % (chr(27), s, chr(27))
def A(s):
	return "%s\033[1;36m %s%s \033[0m" % (chr(27), s, chr(27))
def R(s):
	return "%s\033[1;31m %s%s \033[0m" % (chr(27), s, chr(27))


def check_alive(srv_name):
	cmd = 'ps -ef | grep {0} | grep -v python |grep -v grep'.format(srv_name)
	return_code = os.system(cmd)
	print(return_code)
	if return_code == 0:
		return True
	else:
		return False


def start(srv_name):
	'''
	python3 a.py start cerebro
	'''
	cmd = 'systemctl start {0}'.format(srv_name)
	os.popen(cmd)
	time.sleep(5)
	os.system('systemctl status {0}'.format(srv_name))
	status = os.popen('systemctl status {0}'.format(srv_name)).read()
	running = re.findall('running', status)
	if running and check_alive(srv_name):
		print('{0} 已启动完成 '.format(srv_name))
	else:
		print('{0} 启动没有成功'.format(srv_name))


def stop(srv_name):
	'''
	python3	a.py stop cerebro
	'''
	os.popen('systemctl stop {0}'.format(srv_name))
	time.sleep(5)
	if not check_alive(srv_name):
		print('{0} 已经关闭'.format(srv_name))
	else:
		print('{0} 关闭失败'.format(srv_name))
		os.system('systemctl status {0}'.format(srv_name))


def status(srv_name):
	'''
	python3 a.py status cerebro
	'''
	os.system('systemctl status {0}'.format(srv_name))


def restart(srv_name):
	'''
	python3 a.py status cerebro
	'''
	stop(srv_name)
	time.sleep(5)
	start(srv_name)


if __name__ == "__main__":
	if os.path.exists('./logs'):
		pass
	else:
		os.makedirs('./logs')
	log_ft = datetime.datetime.now().strftime('%Y-%m-%d-%H')
	user_cmd = getpass.getuser()


	logging.basicConfig(
		level=logging.DEBUG,
		format='%(asctime)s {0} %(levelname)s: %(message)s'.format(user_cmd),
		datefmt='%Y-%-m%-d %H:%M:%S',
		filename='./logs/control{0}.log'.format(log_ft),
		filemode='a'
	)

	if user_cmd != 'root':
		print('必须以 root 用户执行此脚本，已退出')
		logging.info('必须以 root 用户执行此脚本，已退出')
		sys.exit(1)

	opts = sys.argv
	try:
		if opts[1] == 'd' or opts[1] == 'help':
			print(G('start :') + R('{0}'.format(start.__doc__)))
			print(G('stop :') + R('{0}'.format(stop.__doc__)))
			print(G('status :') + R('{0}'.format(status.__doc__)))

		elif opts[1] == 'start':
			start(opts[2])
		elif opts[1] == 'stop':
			stop(opts[2])
		elif opts[1] == 'status':
			status(opts[2])
		elif opts[1] == 'restart':
			restart(opts[2])
		else:
			print(R('Script Parameter Error !!!'))
	except IndexError:
		print(R('Script Parameter Error !!!'))