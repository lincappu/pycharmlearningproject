# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# import  socket
#
# # 创建一个 socket 套接字：
# ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #   SOCK_STREAM表示的是 tcp 协议，  DGRAM 表示 udp 协议.
#
# # 开启连接功能
# ss.connect(('127.0.0.1',8898))
#
# # 发消息：
# ss.send(b'hello')
#
# data=ss.recv(1024)
# print(data)
#
#
# ss.close()



import  socket

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.connect(('127.0.0.1',9096))

while True:
    info =input('>>:').strip()
    if len(info)  == 0:
        continue

    ss.send(info.encode('utf-8'))

    data=ss.recv(1024)
    print('mess is %s' %(data))
    # print(data.decdode('utf-8'))


ss.close()






# 改进版:
# import  socket
# ip_port=('127.0.0.1',8081)
# BUFSIZE=1024
#
# tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp.connect(ip_port)
#
#
# while True:
#     info=input('>>:').strip()
#
#     if len(info) == 0:
#         continue
#
#     tcp.send(info.encode('utf-8'))
#
#     msg=tcp.recv(BUFSIZE)
#     print('这是服务器发来的消息： %s' %(msg.decode('utf-8')))
#
#
# tcp.close()
#












