# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os
import subprocess
import logging
import sys

'''
实现 rsync 的功能，方式
1、是调用shell主机的 rsync 命令，或者是 xcopy 命令
2、使用纯 python函数来实现
'''
# 第一种
# res = subprocess.call(['/usr/bin/rsync', '-Ccavzr', '--delete', '/root/logs/', '/tmp'])
# print(res)


# rsync configuration
localdir = '/root/test'
rsync_exe = '/usr/bin/rsync'
pwdfile = '/root/rsync.passwd'
argv = '-Ccravz --delete --password-file=' + pwdfile
user = 'root'
ip = '@172.16.1.146'
module = '::store'

#  vars
homedir = '/root'
logfile = os.path.basename(sys.argv[0]) + '.log'
logpath = homedir + logfile

# logging.basicConfig(level=logging.DEBUG,
# 					format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
# 					datefmt='%Y-%m-%d %H:%M',
# 					filename=logpath,
# 					filemode='a+')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def is_run(processname):
	'''Get processname status'''
	cmd = '/usr/bin/pgrep ' + processname + ' > /dev/null 2>&1'
	try:
		# pstat=subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE)
		pstat = subprocess.Popen(cmd, shell=True)
	except  Exception  as  e:
		logging.error("Get run status failed:: %s ,exit run!" % (e))
		sys.exit(1)
	else:
		pstat.wait()
		if pstat.returncode == 0:
			return True
		else:
			return False


def rsync_store():
	cmd = rsync_exe + argv + ' ' + localdir + ' ' + user + ip
	if is_run('rsync'):
		logging.warning("rsync is running!")
	else:
		try:
			pstat = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		except Exception as e:
			logging.error(("Run script failed:: %d (%s) ,exit run!" % (e.errno, e.strerror)))
			sys.exit(1)
		else:
			pstat.wait()

			if pstat.returncode == 0:
				logging.info("Run script Successful,exit code is %s" % pstat.returncode)
				lines = pstat.stderr.readlines()
				dellist = []
				rsync_dict = {}
				for line in lines:
					if 'deleting' in str(line):
						dellist.append(line.split()[1])
					delcount = len(dellist)
					addlist = [i.rstrip(b'\n') for i in lines[delcount + 2:-3]]
					addcount = len(addlist)
					speed = ' '.join(str(lines)[-2].split()[-2:])
					logging.info("Result,delcount:%d,dellist:%s,addcount:%d,addlist:%s,speed:%s" % (
					delcount, dellist, addcount, addlist, speed))
			else:
				logging.error("Run script End,exit code is %s,With reason <%s>" % (
				pstat.returncode, pstat.stderr.read().rstrip(b'\n')))


# if __name__ == '__main__':
	# rsync_store()



# 第二种：  使用纯 python函数，如果使用纯 python函数来实现，就不能使用rsync命令，
# 原理就是查找、复制、删除基本操作，下面来操作对文件夹内的文件的更新。
# 思路其实就很简单：列出源文件夹下所有的文件夹路径，然后替换成目录文件下的所有路径，然后比较目录文件夹下文件在不在，在就忽略，不在就复制这个文件。同时目的文件有而源文件夹没有文件删除。

for item in os.listdir('/Users/FLS/test/nacos'):
	print(item)























