# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  socket

ip_port=('127.0.0.1',9090)
BUFSIZE=1024

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

qq_name_dic={
    'alex':('127.0.0.1',9090),
    'egon':('127.0.0.1',9090),
    'eva':('127.0.0.1',9090),
    'yh':('127.0.0.1',9090)
}
while True:
    name=input('请输入聊天对象：').strip()
    while True:
        msg=input('请输入消息，回车发送>>:').strip()

        if name == 'quit' or name =='q':
            break

        if not msg or not name or name not in qq_name_dic:
            continue

        udp.sendto(msg.encode('utf-8'),qq_name_dic[name])

        back_msg,addr=udp.recvfrom(BUFSIZE)
        print('来自[%s:%s]的消息： %s'%(addr[0],addr[1],back_msg.decode('utf-8')))


udp.close()
