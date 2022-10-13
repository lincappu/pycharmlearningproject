# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import resource
import signal
import os
import sys
import time
import psutil

print("usage stats: => ", resource.getrusage(resource.RUSAGE_SELF))
print('max_cpu :=> ', resource.getrlimit(resource.RLIMIT_CPU))
print('max_data', resource.getrlimit(resource.RLIMIT_DATA))
print('max process: ', resource.getrlimit(resource.RLIMIT_NPROC))
print('page size:', resource.getpagesize())
print('max memory: ', resource.getrlimit(resource.RLIMIT_AS))
print(resource.RLIMIT_AS)


# 100M  1125899906842624

def post_exec(signo, frame):
	print('超出资源限制')
	raise SystemExit(1)


def set_max_runtime(seconds):
	soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
	resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
	signal.signal(signal.SIGXCPU, post_exec)


def set_max_memory(maxsize):
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))




l = []
if __name__ == '__main__':
	# set_max_runtime(5)
	# for i in range(10000):
	# 	print(i)
	# 	time.sleep(1)
	# set_max_memory(40021225472)
	# f=open('a.log','r')
	# data=f.read()
	# pid=os.getpid()
	# p=psutil.Process(pid)
	# print(p.memory_info())
	while True:
		l.append("a"*1000000)
		time.sleep(0.5)