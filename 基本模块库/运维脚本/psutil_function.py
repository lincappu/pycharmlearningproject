# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import psutil
import datetime
import decimal

'''
psutil是一个跨平台库（http://code.google.com/p/psutil/），能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要应用于系统监控，分析和限制系统资源及进程的管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统，
'''

# 1、cpu 相关信息
# print(psutil.cpu_stats())
# print(psutil.cpu_count())
# print(psutil.cpu_count(logical=False))

# cpu 利用率：
# print(psutil.cpu_percent(1))
# print(psutil.cpu_percent(1,percpu=True))
# cpu_info=['cpu0','cpu1','cpu2','cpu3']
# cpu_per=zip(cpu_info,[1,2,3,4])
# print(list(cpu_per))

# for c in list(cpu_per):
# 	print(c[0]+':'+str(c[1]))  # 很简单的问题，用+连接的时候，不能连接 str 和 int类型的，还是写的代码太少了，
# print(list(cpu_per))

# 2、内存
# print(str(round(psutil.virtual_memory().total /1024/1024/1024,2))+'G')
# print(str(round(psutil.virtual_memory().free /1024/1024/1024,2))+'G')
# print(psutil.swap_memory())

# 3、磁盘
print(psutil.disk_usage('/'))
for d in psutil.disk_partitions():
	o = psutil.disk_usage(d.mountpoint)
	print('磁盘：%s,挂载点：%s,文件类型：%s,总容量：%sG,已用容量: %dG ,可用容量:%dG,利用率：%.2f%%' % (
	d.device, d.mountpoint, d.fstype, int(o.total / (1024.0 * 1024.0 * 1024.0)),
	int(o.used / (1024.0 * 1024.0 * 1024.0)), int(o.free / (1024.0 * 1024.0 * 1024.0)), int(o.used / o.total * 100)))

'''
整数取整：
1、向下取整： int()
2、四舍五入： round（）  python3 使用的是 四舍六入五平分，奇进偶不进
print(round(1.5))
print(round(2.5))   这两个都是 2，所以是不准确的，避免用 round 函数，

3、向上取整： math.ceil()
4、分开取整数和小数： math.modf() 是一个元组（整数部，小数部）

5、浮点数输出：
f 默认保留 6 位小数
e 默认 6 为小数 但是是指数的形式
g 在保证 6 位数的前提下，使用小数方法，否则使用科学计数法。


正确的四舍五入的方法：

ROUND_HALF_DOWN：5，则做进位操作；否则舍弃；
ROUND_HALF_UP：末位大于等于5，则做进位操作；否则舍弃；
ROUND_HALF_EVEN：默认情况看 四舍六入五平分，奇进偶不进

print(decimal.getcontext().rounding) 
decimal.getcontext().rounding= "ROUND_HALF_UP"
print(decimal.getcontext().rounding)
print(decimal.Decimal('1.15').quantize(decimal.Decimal('0.0')))
'''

# print(psutil.disk_io_counters(perdisk=True))


# 4、网络
# print(psutil.net_io_counters())
# print('{0:.2f} Mb'.format(psutil.net_io_counters().bytes_sent/1024/1024))
# print('{0:.2f} Mb'.format(psutil.net_io_counters().bytes_recv/1024/1024))


# 5、系统信息
# 当前用户数
# for u in  psutil.users():
# 	print(u.name)
# 	print(u.terminal)
# user_list=','.join([u.name for u in psutil.users()])
# print(user_list)


# 当前系统时间
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# 6、进程信息
print(psutil.pids())
p=psutil.Process(64499)
print(p.memory_percent() )
for pid in psutil.pids():
	p = psutil.Process(pid)
	print(u"进程名 %-20s 进程号 %-10s 进程状态 %-10s 创建时间 %-10s " % (p.name(), p.pid(), p.status(), p.started()))

''''
进程信息：
p.name()   #进程名
p.exe()    #进程的bin路径
p.cwd()    #进程的工作目录绝对路径
p.status()   #进程状态
p.create_time()  #进程创建时间
p.uids()    #进程uid信息
p.gids()    #进程的gid信息
p.cpu_times()   #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()   #返回进程列表
p.num_threads()  #进程开启的线程数

'''



# 开启进程
'''
听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息

from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()
'''


