# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  subprocess
from pprint import  pprint

# print(subprocess.call(['df','-h'],shell=False))
# print(subprocess.call('df -r',shell=True)) # 错误的时候返回的是 shell 的错误信息加上 exit 返回码

# print(subprocess.check_call('df -h',shell=True)) # 执行正确返回，就是 shell正确执行，exit 0 返回码
# print(subprocess.check_call('df -r',shell=True))  # shell 执行错误就返回错误

# print(subprocess.check_output(['ls','-la','/Users/FLS']))  # 正确就返回 bytes 类型的结果
# print(subprocess.check_output(['ls','a','/Users/FLS']))   # 错误就就报错





# Popen对象：
# child=subprocess.Popen(['ping','www.baidu.com'],shell=True)  # 不等待子进程，父进程直接返回
# print('parent process')


child=subprocess.Popen(['ping','www.baiu.com'])
print(child.pid)
print(child.poll())
child.wait(20)  # 父进程等待子进程，并输出子进程的输出信息
print('parent process')

# 其他子进程信号：
# child.poll() # 检查子进程状态
# child.kill() # 终止子进程
# child.send_signal() # 向子进程发送信号
# child.terminate() # 终止子进程


# 例子
# import shlex,subprocess
#
# command_line=input('cmd>>:').strip()
# args=shlex.split(command_line)
# p=subprocess.Popen(args)