# import socket
# import subprocess
# import struct
#
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议
# phone.bind(('127.0.0.1',10101))
# phone.listen(5)
#
# while True:
#     conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
#     print(client_addr)
#
#     while True: #通信循环
#         #收消息
#         try:
#             cmd=conn.recv(1024) # 1024最大的限制
#             if not cmd:break #针对linux系统
#
#             #执行，拿到执行结果
#             obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
#                                     stdout=subprocess.PIPE,
#                                     stderr=subprocess.PIPE)
#
#             stdout_res=obj.stdout.read()
#             stderr_res=obj.stderr.read()
#             #先发报头
#             total_size=len(stderr_res)+len(stdout_res)
#             conn.send(struct.pack('i',total_size))
#
#             #再发真是的数据
#             # conn.send(stdout_res+stderr_res)
#             conn.send(stdout_res)
#             conn.send(stderr_res)
#         except ConnectionResetError:
#             break
#
#     #挂电话
#     conn.close()
#
# #关机
# phone.close()






import subprocess
import socket


phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.2',10102))

phone.listen(5)


while True:
    conn,client_addr=phone.accept()
    print(client_addr)


    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:
                break
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout_res=res.stdout.read()
            stderr_res=res.stderr.read()
















