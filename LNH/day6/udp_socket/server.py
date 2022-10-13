# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

# import socket
#
# ip_port = ('127.0.0.1', 9090)
# BUFSIZE = 1024
#
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# udp.bind(ip_port)
#
# while True:
#     print('udp socket starting....')
#     msg,addr= udp.recvfrom(BUFSIZE)
#     print(msg)
#
#     udp.sendto(msg.up per(),addr)



# import  socket
#
# udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udp.bind(('127.0.0.1',8081))
#
# while True:
#     msg,addr=udp.recvfrom(1024)
#     print(msg,addr)
#     udp.sendto(msg.upper(),addr)


__author__ = 'Linhaifeng'
import socket
ip_port=('127.0.0.1',8082)
udp_server_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #买手机
udp_server_sock.bind(ip_port)

while True:
    qq_msg,addr=udp_server_sock.recvfrom(1024)
    print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' %(addr[0],addr[1],qq_msg.decode('utf-8')))
    back_msg=input('回复消息: ').strip()

    udp_server_sock.sendto(back_msg.encode('utf-8'),addr)