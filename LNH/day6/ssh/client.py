# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  socket
import  struct
import  json
#
# ip_port=('127.0.0.1',8081)
# BUFSIZE=1024
#
# tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp.connect(ip_port)
#
#
# while True:
#     cmd=input('>>:').strip()
#
#     if len(cmd) == 0:
#         continue
#
#     tcp.send(cmd.encode('utf-8'))
#
#     # 先收报头
#     msg=tcp.recv(4)
#     total_size=struct.unpack('i',msg)[0]  # 客户端要收报头，然后才能知道要收多少数据。
#
#     # 再收消息
#
#     cmd_res=b''
#     recv_size=0
#     while recv_size < total_size:
#         recv_data=tcp.recv(1024)
#         cmd_res+=recv_data
#         recv_size+=len(recv_data)
#
#
#     print(cmd_res.decode('utf-8'))
#
#
# tcp.close()


phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8086))

while True:
    cmd=input('==>:').strip()
    if len(cmd)==0:
        continue

    phone.send(cmd.encode('utf-8'))

    # 先收报头字典
    msg=phone.recv(4)
    print(msg)
    header_size=struct.unpack('i',msg)[0]

    # 在接受报头
    header_bytes=phone.recv(header_size)
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)

    # 再开始接收消息
    cmd_res=b''
    reve_sie=0
    while  reve_sie  < header_dic['total_size']:
        reve_data=phone.recv(1024)
        cmd_res+=reve_data
        reve_sie+=len(reve_data)

    print('命令执行结果是：\n %s' %(cmd_res).decode('utf-8'))

phone.close()








