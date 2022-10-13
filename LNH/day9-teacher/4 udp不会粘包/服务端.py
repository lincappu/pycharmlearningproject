from socket import *

server=socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',8080))



msg1,client_addr=server.recvfrom(100000000)
msg2,client_addr=server.recvfrom(1024)
msg3,client_addr=server.recvfrom(1024)

print(msg1)
print(msg2)
print(msg3)


import os
os.fork
