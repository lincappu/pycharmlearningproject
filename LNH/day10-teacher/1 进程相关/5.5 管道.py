# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# 返回2个连接对象(conn1, conn2),代表管道的两端,默认是双向通信.如果duplex=False,conn1只能用来接收消息,conn2只能用来发送消息.不同于os.open之处在于os.pipe()返回2个文件描述符(r, w),表示可读的和可写的
# conn1  负责存储=发送，conn2 负责读取=接收

# from multiprocessing import  Process,Pipe

# (conn1,conn2)=Pipe()
# conn1.send('nihao')
# conn1.send('women')
#
# print(conn2.recv())
# print(conn2.recv())
# print(conn2.recv())  # 没有收到就会一直在阻塞。
# conn1.close()
# conn2.close()



# from  multiprocessing import  Process, Pipe
#
# def sender(pipe):
#     pipe.send('nihao')
#     pipe.close()
#
#
# if __name__ == '__main__':
#     (conn1,conn2)=Pipe()
#     sender=Process(target=sender,args=(conn1,))
#     sender.start()
#
#     print('conn2 recv:', conn2.recv())
#
#     conn2.close()



# 同时接收和发送消息
from multiprocessing import Process, Pipe

def talk(pipe):
    pipe.send(dict(name='Bob', spam=42))            # 传输一个字典
    reply = pipe.recv()                             # 接收传输的数据
    print('talker got:', reply)

if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()                  # 创建两个 Pipe() 实例，也可以改成 conf1， conf2
    child = Process(target=talk, args=(childEnd,))  # 创建一个 Process 进程，名称为 child
    child.start()                                   # 启动进程
    print('parent got:', parentEnd.recv())          # parentEnd 是一个 Pip() 管道，可以接收 child Process 进程传输的数据
    parentEnd.send({x * 2 for x in 'spam'})         # parentEnd 是一个 Pip() 管道，可以使用 send 方法来传输数据
    child.join()                                    # 传输的数据被 talk 函数内的 pip 管道接收，并赋值给 reply
    print('parent exit')










