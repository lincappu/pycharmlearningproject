# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import socket
import struct
import json
import os, sys
import subprocess


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
            self.conn,self.addr=self.socket.accept()
            print('[%s:%s]:'%(self.addr[0],self.addr[1]))
            while True:
                args_struck=self.conn.recv(4)
                args_len=struct.unpack('i',args_struck)[0]
                args=self.conn.recv(args_len).decode('utf-8')
                l=args.split()
                cmd=l[0]
                filename=l[1]
                print('%s,%s' %(cmd,filename))
                if cmd != 'get':
                    obj=



    # def put(self, args):




myftp = Myftpserver(('127.0.0.1', 8091))
myftp.run()
