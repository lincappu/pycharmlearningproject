# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import socket
import struct
import json
import os, sys


class Myftpserver:
    def __init__(self, ip_port):
        self.ip_port = ip_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(30)
        self.socket.bind(ip_port)
        self.socket.listen(5)

    def run(self):
        while True:
            self.conn, self.addr = self.socket.accept()
            print('来自客户端的连接:[%s:%s]' % (self.addr[0], self.addr[1]))
            while True:
                head_struck = self.conn.recv(4)
                print('ok')
                print('head_struck : %s' %(head_struck))
                if not head_struck: break

                head_len = struct.unpack('i', head_struck)[0]

                head_json = self.conn.recv(head_len).decode('utf-8')
                head_dic = json.loads(head_json)

                print(head_dic)

                cmd = head_dic['cmd']
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(head_dic)
                print(head_dic)

    def put(self, args):
        filepath = os.path.join(r'/Users/FLS', args['filename'])

        filesize = args['filesize']
        recv_size = 0
        with open(filepath, 'wb') as f:
            while recv_size < filesize:
                recv_data = self.conn.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)
            print('recvsize:%s  filesize:%s' % (recv_size, filesize))


    def get(self,args):



myftp = Myftpserver(('127.0.0.1', 8091))
myftp.run()
