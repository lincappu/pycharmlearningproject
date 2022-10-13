from socket import *


server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen()

conn,addr=server.accept()

data1=conn.recv(5)   # 客户端粘，服务器端不一定会粘，可以指定收多少。
print('data1:',data1)
# data2=conn.recv(5)
# print('data2:',data2)
