# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  socket
import struct
import  json

ip_port=('127.0.0.1',8090)
BUFSIZE=1024

tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp.connect(ip_port)


while True:

    cmd=input('>>:').strip()

    if len(cmd) == 0:
        continue

    # 发命令
    tcp.send(cmd.encode('utf-8'))

    # 先收报头长度
    msg=tcp.recv(4)
    header_size=struct.unpack('i',msg)[0]

    # 再收报头
    header_bytes=tcp.recv(header_size)
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)

    # 再收消息
    cmd_res=b''
    recv_size=0
    while recv_size < header_dic['total_size']:
        recv_data=tcp.recv(1024)
        cmd_res+=recv_data
        recv_size+=len(recv_data)

    print(cmd_res.decode('utf-8'))
    print('消息大小:%s' %(recv_size))

tcp.close()
