# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os
import subprocess

# 阻塞的
# 等待子进程运行完成，如果没有输出就返回 code，如果有输出就一直返回输出结果。是实时输出结果。
# print(os.system('cd /Users/FLS'))
# print(os.system('df -H'))
# print(os.system('ping www.qq.com'))


# 非阻塞的，只有在使用 read()的时候才会阻塞主进程,一次性的拿出结果。
print(os.popen('ping www.qq.com'))
print(os.popen('netstat  -nr'))
print(os.popen('ls -la').read())
# 返回的是执行过程中输出的内容

'''
语法
popen()方法语法格式如下：
os.popen(command[, mode[, bufsize]])

参数
command – 使用的命令。
mode – 模式权限可以是 ‘r’(默认) 或 ‘w’。
bufsize – 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。

返回值
返回一个文件描述符号为fd的打开的文件对象

特性：
1、返回的是文件对象，里面是执行的内容，有可能是列表。
fs=os.popen('ls -la')
print(type(fs))
print(fs.readlines())

2、非阻塞popen 不会等着 cmd命令执行再执行，除非用 read 来读取结果的时候才会等着他 返回。

3、完全阻塞的情况: 
print(os.popen('ping 127.0.0.1').read())
因为ping 127.0.0.1 会一直执行不会结束，popen 一直拿不到结果，主程序会一直等着，同时也无法进入交互模式，这时候就形成了完全阻塞的状态，只能终止程序的运行。

'''






'''
subprocess.popen()
打开的是一个进程，
subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
# 其中args值的是需要传入的要执行的程序路径(字符串)，如果是列表的话，第一项是程序的路径，后面的参数是执行该程序所需要的参数，这个与popen一致。

# 下面是各个参数的详解
# bufsize 指定缓冲，0 无缓冲， 1 行缓冲 其他正值 缓冲区大小  负值 采用的默认系统缓冲(一般是全缓冲)
# executable： 用于指定可执行程序。一般情况下我们通过args参数来设置所要运行的程序。如果将参数shell设为 True，executable将指定程序使用的shell。在windows平台下，默认的shell由COMSPEC环境变量来指定。
# stdin stdout stderr 三者是成程序的标准输入、标准输出、错误句柄。可以赋值为None(没有任何重定向，继承父进程)、PIPE(创建管道)、文件对象、文件描述符(整数)等,其中stderr还是可以设置成STDOUT，
# preexc_fn：只是在Unix下生效，用于指定一个可执行对象,它将在子进程运行之前被调用。
# close_sfs：在windows平台下，如果如果该参数被设置成True，那么新创建的子进程将不会继承父进程的输入输出错误管道，我们不能将该函数设置为True同时重定向子进程的标准输入输出与错误。
# shell：在unix下就是相当于在args前面添加了"/bin/sh /c" 在windows下相当于添加了"cmd.exe /c"
# cmd：设置子进程的工作目录
# env：字典类型，用于指定子进程的环境变量，如果env=None,那么子进程的环境变量将从父进程中继承
# Universal_newlines:不同操作系统下，文本的换行符是不一样的。如：windows下用'/r/n'表示换，而Linux下用 '/n'。如果将此参数设置为True，Python统一把这些换行符当作’/n’来处理。
# 参数startupinfo与createionflags只在windows下有效，它们将被传递给底层的CreateProcess()函数，用 于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等。


'''





