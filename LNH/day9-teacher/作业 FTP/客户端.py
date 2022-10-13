# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS



import struct
import os
import json
import socket


class MyTCPClient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.myclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.myclient.connect(self.server_address)

    def run(self):
        while True:
            inp = input('>>:').strip()
            if not inp:
                continue
            l = inp.split()
            cmd = l[0]
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(l)

    def put(self, args):
        cmd = args[0]
        filename = args[1]

        if not os.path.isfile(filename):
            print('file not find')
            return
        else:
            filesize = os.path.getsize(filename)

        head_dic = {'cmd': cmd,
                    'filename': os.path.basename(filename),
                    'filesize': filesize
                    }
        print('报头字典为：', head_dic)

        head_json=json.dumps(head_dic)

        head_bytes=bytes(head_json.encode('utf-8'))


        head_struct=struct.pack('i',len(head_bytes))

        self.myclient.send(head_struct)

        self.myclient.send(head_bytes)

        size_send=0

        with open(filename,'rb') as read_f:
            for line in read_f:
                self.myclient.send(line)
                size_send+=len(line)
                print('size_send:',  size_send)

            else:
                print('upload  successful')


client=MyTCPClient(('127.0.0.1',10023))
client.run()