 # !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
'''
解决的问题：
1.数据为空的问题，就是判断，接收的数据为空
2.判断粘包的问题：
发包阶段：tcp 的特性，较短的时间较小的数据会一起发送
收包阶段：接受端一次没有收完所有的包，造成一次可能接受了两个包，而 tcp不知道中间数据的界限，一次性提取多少字节的数据进行解包。

注意：
udp 是永远不会粘包的。udp 不会使用合并优化算法，udp 是链式结构，每个包都有包头，这样每个包就知道该接收多少个数据包。

解决方法：
1.发包阶段：将数据打包，整型没有 bytes 类型，所以，要用 struck 模块打包，
2.收包阶段：先接受4个包，这样就知道要接收数据的大小，然后循环收包即可，
'''


import  socket
import  subprocess
import  struct
import  json

# ip_port=('127.0.0.1',8081)
# BUFSIZE=1024  # 这个也可以增加，但是因为目的就是一次性收完所有的数据，然后接收。并且内存不是无限大的，所以就要循环收，然后
#
# tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# tcp.bind(ip_port)
# tcp.settimeout(15)
# tcp.listen(5)
# while True:
#     print('开始监听......')
#     conn,addr=tcp.accept()
#     while True:
#         try:
#             cmd=conn.recv(BUFSIZE)
#
#             if len(cmd) ==0:
#                     break
#
#             cmd=cmd.decode('utf-8')
#
#             obj=subprocess.Popen(cmd,shell=True,
#                                  stdout=subprocess.PIPE,
#                                  stderr=subprocess.PIPE)
#
#             stdout_res=obj.stdout.read()
#             stderr_res=obj.stderr.read()
#
#             # 先发报头
#             total_size=len(stdout_res)+ len(stderr_res)
#             conn.send(struct.pack('i',total_size))
#
#             # 再发数据
#             conn.send(stdout_res)
#             conn.send(stderr_res)
#             # conn.send(cmd.upper())
#
#         except ConnectionResetError:
#             break
#
#     conn.close()
#
# tcp.close()


ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

ss.bind(('127.0.0.1',8086))
ss.listen(5)

while True:
    conn,addr=ss.accept()
    while True:
        try:
            cmd=conn.recv(1024)

            if len(cmd) ==0:
                break

            obj=subprocess.Popen(cmd,shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

            stdout_res=obj.stdout.read()
            stderr_res=obj.stderr.read()

            # 制作报头

            header_dic={
                'filename':'socke',
                'total_size':len(stdout_res)+len(stderr_res),
                'md5':'xxxxxxxx'
            }

            header_json=json.dumps(header_dic)
            header_bytes=header_json.encode('utf-8')
            print(header_bytes)
            print(len(header_bytes))

            # 先发报头长度
            print(struct.pack('i',len(header_bytes)))
            conn.send(struct.pack('i',len(header_bytes)))

            #  发报头
            total_size=len(stdout_res)+len(stderr_res)
            # conn.send(struct.pack('i',total_size))
            conn.send(header_bytes)

            # 再开始发送数据
            conn.send(stdout_res)
            conn.send(stderr_res)
        except:
            break
    conn.close()

ss.close()








