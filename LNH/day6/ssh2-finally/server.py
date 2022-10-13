# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
'''
在基础的版本上需要解决的问题：
1.报头不应该只包含数据的大小。
2.打包的时候选用的 i 类型标示的数据量很小。
解决方法：
第一个问题：使用字典，将要传输的信息用字典的形式展示出来，
第二个问题：先传报头的大小，先接受报头。
'''




import  socket
import  subprocess
import  struct
import  json

ip_port=('127.0.0.1',8090)
BUFSIZE=1024

tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcp.bind(ip_port)
tcp.listen()


while True:
    print('Listen starting...')
    conn,addr=tcp.accept()
    print('Client %s  connected' %(addr[0]))
    while True:
        cmd=conn.recv(BUFSIZE)

        if len(cmd) == 0:
            break

        cmd=cmd.decode('utf-8')
        print('接收到的客户端命令：%s' % (cmd))

        obj=subprocess.Popen(cmd,shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        stdout_res=obj.stdout.read()
        stderr_res=obj.stderr.read()

        # 制作报头
        header_dic={
            'filename':'a.txt',
            'total_size':len(stdout_res)+len(stderr_res),
            'md5':'1111111111'
        }

        header_json=json.dumps(header_dic)
        header_bytes=header_json.encode('utf-8')
        print(struct.pack('i',len(header_bytes)))

        # 先发报头长度
        conn.send(struct.pack('i',len(header_bytes)))

        # 发送报头
        # total_size=len(stdout_res)+len(stderr_res)
        # conn.send(struct.pack('i',total_size))
        conn.send(header_bytes)

        # 再发数据
        conn.send(stdout_res)
        conn.send(stderr_res)


    conn.close()


tcp.close()









