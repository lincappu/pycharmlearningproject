# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# import  socket
#
# ip_port=('127.0.0.1',9090)
# BUFSIZE=1024
#
# udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# while True:
#     msg=input('>>:').strip()
#
#     if len(msg) ==0:
#         continue
#
#     udp.sendto(msg.encode('utf-8'),ip_port)
#
#
#     data,addr=udp.recvfrom(BUFSIZE)
#     print(data.decode('utf-8'))


#
# import  socket
# udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # udp.connect(('127.0.0.1',8081))  # udp 是没有连接的
#
# while True:
#     msg=input('==>:').strip()
#
#     if len(msg) == 0:
#         continue
#
#     udp.sendto(msg.encode('utf-8'),('127.0.0.1',8081))
#
#     data,addr=udp.recvfrom(1024)
#
#     print(data.decode('utf-8'),addr)

import socket
BUFSIZE=1024
udp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

qq_name_dic={
    '狗哥alex':('127.0.0.1',8081),
    '瞎驴':('127.0.0.1',8082),
    '一棵树':('127.0.0.1',8082),
    '武大郎':('127.0.0.1',8082),
}


while True:
    qq_name=input('请选择聊天对象: ').strip()
    while True:
        msg=input('请输入消息,回车发送: ').strip()
        if msg == 'quit':break
        if not msg or not qq_name or qq_name not in qq_name_dic:continue
        udp_client_socket.sendto(msg.encode('utf-8'),qq_name_dic[qq_name])

        back_msg,addr=udp_client_socket.recvfrom(BUFSIZE)
        print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' %(addr[0],addr[1],back_msg.decode('utf-8')))

udp_client_socket.close()