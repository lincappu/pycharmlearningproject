from socket import *


server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen()

conn,addr=server.accept()

data1=conn.recv(1)
print('data1:',data1)
import time
time.sleep(5)
data2=conn.recv(1024)
print('data2:',data2)


# 服务端粘了，客户端没粘。