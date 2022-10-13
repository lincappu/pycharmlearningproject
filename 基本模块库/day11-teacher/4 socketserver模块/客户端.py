#TCP
# from socket import *
#
#
# c=socket(AF_INET,SOCK_STREAM)
# c.connect(('127.0.0.1',8080))
#
# count=1
# while True:
#     msg=input('>>: ').strip()
#     if not msg:break
#     c.send(msg.encode('utf-8'))
#     data=c.recv(1024)
#     print(data)
#
# c.close()



#UDP
from socket import *


c=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    if not msg:break
    c.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    data=c.recvfrom(1024)
    print(data)

c.close()
