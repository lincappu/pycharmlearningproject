# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  socket
import os,sys
import  json
import struct

class Myftpclient:
    def __init__(self,ip_port):
        self.ip_port=ip_port
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(ip_port)

    def run(self):
        while True:
            inp=input('请输入你的命令>>:').strip()

            if not inp: continue

            l=inp.strip()
            cmd=l[0]
            if cmd !='put':
                inp_len=len(inp)
                inp_strunk=struct.pack('i',inp_len)
                self.socket.send(inp_strunk)
                self.socket.send(inp.encode('utf-8'))
                self.socket.send('fsfsdfsd'.encode('utf-8'))





    # def put(self,args):





client1=Myftpclient(('127.0.0.1',8091))
client1.run()


