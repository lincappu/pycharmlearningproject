# # !/usr/bin/env python3
# # _*_coding:utf-8_*_
# # __author__：FLS
#
# # import os,time
# # print(os.getpid()) #自己的进程的pid
# # print(os.getppid()) #自己的进程的pid
# # time.sleep(1000)

# 详解：
# Python subprocess模块用来管理子进程，以取代一些旧模块的方法
# os.system、
# os.spawn*、
# os.popen*、
# popen2.*、
# commands.*）。
# 不但可以调用外部的命令作为子进程，而且可以连接到子进程的input/output/error管道，获取相关的返回信息。
#
# 这些是老的 api
# call()  check_call()  check_output()
# 新的 api 为 run 和 popen，其中 popen 更为高级。



import  subprocess

# subprocess.run(args, *,
#                stdin=None, input=None, stdout=None, stderr=None,
#                capture_output=False, shell=False, cwd=None, timeout=None,
#                check=False, encoding=None, errors=None, text=None, env=None,
#                universal_newlines=None)¶
#
# class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None,
#             stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False,
#             cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0,
#             restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None,
#             errors=None, text=None)


# res=subprocess.run(args='ls -la',shell=True,stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE)
# print(res)

data=subprocess.run('la -s',input=b'-la',shell=True,timeout=2,capture_output=True)  # 返回的 TextIOWrapper  bytes 类型。
# print(type(data))
# print(data.args)   # 被用作启动进程的参数. 可能是一个列表或字符串.
# print(data.returncode)    # 子进程的退出状态码. 通常来说, 一个为 0 的退出码表示进程运行正常.一个负值 -N 表示子进程被信号 N 中断 (仅 POSIX).
# print(data.stdout)    # 从子进程捕获到的标准输出. 一个字节序列, 或一个字符串, 如果 run() 是设置了 encoding, errors 或者 text=True 来运行的. 如果未有捕获, 则为 None. 如果你通过 stderr=subprocess.STDOUT 运行, 标准输入和标准错误将被组合在一起, 并且 stderr` 将为 None.
# print(data.stderr)
# print(data.check_returncode())  # 如果 returncode 非零, 抛出 CalledProcessError.


# print(subprocess.Popen(args=['ls','-la'],stdout=subprocess.PIPE ,check=True))
#
#
# p = subprocess.Popen('df -Th', stdout=subprocess.PIPE, shell=True)
# print(p.stdout.read())
#
#
# print(subprocess.run(["ls", "-l", "/dev/null"]))


# popen 方法：
# args  在没有设置 shell=True 的时候只能是列表的形式，如果是字符串必须是命令全路径的形式，否则找不到，因为没有环境变量。
# window 就没有这种问题。


# import time
# import subprocess
#
# def cmd(command):
#     subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
#     subp.wait(2)  # 如果子进程在限定的时间内没有中断，就会自动抛出一个TimeoutExpired 异常
    # if subp.poll() == 0:  # 检查子进程是否退出，设置并返回 returncode 的属性，
    #     print(subp.communicate()[1])  # 这个读取的内存的缓存，如果是返回的数据过大或者无限的，不要用此方法。
    # else:
    #     print("失败")


    # print(subp.stdout.read())   # 这种可以接受大量的数据

# cmd("ls -la")
# cmd("exit 1")




# class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None,
#             stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False,
#             cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0,
#             restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None,
#             errors=None, text=None)



# res1=subprocess.Popen('ls -la ',shell=True,
#                     stderr=subprocess.PIPE,
#                     stdout=subprocess.PIPE,
#                     )
# data1=res1.stdout.read()
# print(data1)

# res2=subprocess.Popen(args=['grep 10'],shell=True,
#                     stdin=res1.stdout,
#                     stderr=subprocess.PIPE,
#                     stdout=subprocess.PIPE,
#                     )

# print(res2.stdout.read().decode('utf-8'))







# 练习：这个不会主进程不会退出的例子：
# python（父进程）用subprocess.Popen新建一个进程（子进程）去开启一个shell， shell新开一个子进程（孙进程）去执行ping www.baidu.com的命令。
# 由于孙进程ping www.baidu.com一直在执行,就类似于一个daemon程序，一直在运行。在超时时间后，父进程杀掉了shell子进程，
# 但是父进程阻塞在了p.communicate函数了，是阻塞在了调用wait()函数之前，感兴趣的朋友可以看一下源码_communicate函数，
# linux系统重点看_communicate_with_poll和_communicate_with_select函数，你会发现是阻塞在了while循环里面，因为父进程一直在获取输出，
# 而孙进程一直像一个daemon程序一样，一直在往子进程的输出写东西，而子进程的文件句柄继承自父进程。虽然shell子进程被杀掉了，但是父进程里面的逻辑并没有因为子进程被意外的干掉而终止，
# （因为孙进程一直有输出到子进程的stdout，导致子进程的stdout一直有输出，也就是父进程的stdout也有输出），所以while循环一直成立，就导致了阻塞，进而导致wait()没有被调用，所以子进程没有被回收，就成了僵尸进程。


# 要完美的解决这个问题就是即要能获取到subprocess.Popen的进程的输出，在超时又要能杀掉子进程，让主进程不被阻塞。

# import subprocess
# from threading import Timer
# import os
#
# class test(object):
#     def __init__(self):
#         self.stdout = []
#         self.stderr = []
#         self.timeout = 10
#         self.is_timeout = False
#         pass
#
#     def timeout_callback(self, p):
#         print('exe time out call back')
#         print(p.pid)
#         try:
#             p.kill()
#         except Exception as error:
#             print(error)
#
#     def run(self):
#         cmd = ['bash', '/Users/FLS/test/test.sh']
#         p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         my_timer = Timer(self.timeout, self.timeout_callback, [p])
#         my_timer.start()
#         try:
#             print("start to count timeout; timeout set to be %d \n" % (self.timeout,))
#             stdout, stderr = p.communicate()
#             exit_code = p.returncode
#             print(exit_code)
#             print(type(stdout), type(stderr))
#             print(stdout)
#             print(stderr)
#         finally:
#             my_timer.cancel()
#
# t=test()
# t.run()


# 解决方法： 详细看 cnblogs
import subprocess
from threading import Timer
import os
import signal

class test(object):
    def __init__(self):
        self.stdout = []
        self.stderr = []
        self.timeout = 10
        self.is_timeout = False
        pass

    def timeout_callback(self, p):
        print('exe time out call back')
        print(p.pid)
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except Exception as error:
            print(error)

    def run(self):
        cmd = ['bash', '/Users/FLS/test/test.sh']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,preexec_fn=os.setsid)

        my_timer = Timer(self.timeout, self.timeout_callback, [p])
        my_timer.start()
        try:
            print("start to count timeout; timeout set to be %d \n" % (self.timeout,))
            stdout, stderr = p.communicate()
            exit_code = p.returncode
            print(exit_code)
            print(type(stdout), type(stderr))
            print(stdout)
            print(stderr)
        finally:
            my_timer.cancel()

t=test()
t.run()