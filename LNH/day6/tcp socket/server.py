# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# import  socket
#
# # 创建一个 socket 套接字：
# ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #   SOCK_STREAM表示的是 tcp 协议，  DGRAM 表示 udp 协议.
#
# # 把地址绑定到套接字
# ss.bind(('127.0.0.1',8898))
#
# # 开启监听：
# ss.listen(5)  # 最大挂起的连接数， 等待的队列
#
# # 等待连接：
# print('等待连接：')
# conn,client_addr=ss.accept()  # 套接字的连接和客户端的 ip 地址。
# print(conn)  # <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8898), raddr=('127.0.0.1', 56799)>
# print(client_addr)  # ('127.0.0.1', 56799)
#
# # 收消息
# data=conn.recv(1024) #最大是1024字节。
# print(data)
#
# conn.send(data.upper())
#
# conn.close()
# ss.close()
# #  这点和文件的操作时一致的，关闭无用的连接，节省资源。
# # 1.程序资源。
# # 2.操作系统资源

#
# import  socket
#
#
# ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# ss.bind(('127.0.0.1',9096))
# ss.listen(5)
#
# while True:
#     print('开始监控套接字：')
#     conn,client_addr=ss.accept()
#     print('获取到客户端套接字%s %s' %(conn,client_addr))
#     while True:
#         try:
#             data=conn.recv(1024)
#             print('客户端消息：%s' %data)
#             if len(data) == 0:  # linux 特殊操作。 这个在 linux下必须判断。
#                 break
#             conn.send(data.upper())
#         except:
#             break
#     conn.close()
#
# ss.close()


# 改进版：  循环发送消息
# import  socket
#
# ip_port=('127.0.0.1',8081)
# BUFSIZE=1024
#
# tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# tcp.bind(ip_port)
# tcp.settimeout(15)
# tcp.listen(5)
# while True:
#     print('开始监听.......')
#     conn,addr=tcp.accept()
#     # print(conn)
#     # print(addr)
#     print('监听到客户端IP:%s的连接：' %(addr[0]))
#     while True: # 通信循环
#         try:
#             msg=conn.recv(BUFSIZE) # 客户端单方面自动断开后，recv 这个会一直收空，然后发空。进入死循环。但是发包是不会出现这种情况的。
#
#             print('客户端%s：  消息：%s ' %(addr[0],msg))
#
#             if len(msg) ==0:  #这个是 linux 的情况，因为不会报错。
#                     break
#
#             conn.send(msg.upper())
#         except:
#             break
#
#     conn.close()

# tcp.close()


















