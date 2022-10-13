# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
'''
简单的多人聊天系统：
就是多个人可以和服务器进行聊天。
client 发送消息，服务器回消息，谁发的，服务器就回谁的
client 之间是不能聊天的。
'''


import socket

ip_port = ('127.0.0.1', 9090)
BUFSIZE = 1024

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(ip_port)

print('udp socket starting....')

while True:
    msg,addr= udp.recvfrom(BUFSIZE)
    print(addr)
    print('来自[%s:%s]的消息：\033[1;34;1m %s\033[0m' %(addr[0],addr[1],msg.decode('utf-8')))
    back_log=input('回复消息>>:').strip()
    udp.sendto(back_log.encode('utf-8'),addr)