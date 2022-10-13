# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  socket
import  os,sys
import  json
import  struct

class Myftpclient:
    def __init__(self,ip_port):
        self.ip_port=ip_port
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(ip_port)

    def run(self):
        while True:
            inp=input('请输入命令>>:').strip()
            if not inp :
                continue
            l=inp.split()
            cmd=l[0]
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func(l)

    def put(self,args):
        cmd=args[0]
        filename=args[1]
        if not os.path.isfile(filename):
            print('%s 文件不存在' %(filename))
            return
        else:
            filesize=os.path.getsize(filename)

        head_dic={
            'cmd':cmd,
            'filename':filename,
            'filesize':filesize,
            'md5':'111111111'
        }

        print(head_dic)
        head_json=json.dumps(head_dic)
        head_json_bytes=head_json.encode('utf-8')

        head_struck=struct.pack('i',len(head_json_bytes))

        print(len(head_struck))
        self.socket.send(head_struck)
        print('ok')
        self.socket.send(head_json_bytes)
        print('ok')


        send_size=0
        with open(filename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
            print(send_size)
            print('upload success')

    def get(self,args):
        self.socket.send(args.encode('utf-8'))







client1=Myftpclient(('127.0.0.1',8091))
client1.run()


