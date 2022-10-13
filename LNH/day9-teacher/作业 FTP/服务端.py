# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import socket
import json
import subprocess
import os
import struct


class MyTCPServer:

    server_dir=r'/Users/FLS/OneDrive - 北京新橙科技有限公司/onedrive/pycharmlearningproject/day9-teacher/作业 FTP'

    def  __init__(self,server_address):
        self.server_address=server_address

        self.mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.mysock.bind(server_address)
        self.mysock.listen(10)



    def run(self):
        print('run 方法开始执行：')
        while True:
            self.conn,self.client_address=self.mysock.accept()
            print('client from:',self.client_address)
            while True:
                head_struct=self.conn.recv(4)
                if not head_struct:
                    break

                print(head_struct)
                head_len=struct.unpack('i',head_struct)[0]
                head_json=self.conn.recv(head_len).decode('utf-8')
                head_dic=json.loads(head_json)

                print('报头结构体是:' ,head_dic)

                cmd=head_dic['cmd']

                if hasattr(self,cmd):
                    func=getattr(self,cmd)
                    func(head_dic)


    def put(self,args):
        file_path=os.path.normpath(os.path.join(self.server_dir,args['filename']))

        file_size=args['filesize']

        recv_size=0

        print('开始上传文件:',file_path)

        with open(file_path,'wb') as  write_f:
            while recv_size < file_size:
                recv_data=self.conn.recv(1024)
                write_f.write(recv_data)
                recv_size+=len(recv_data)
                print('recvsize:%s filesize:%s' %(recv_size,file_size))






tserver=MyTCPServer(('127.0.0.1',10023))
tserver.run()





