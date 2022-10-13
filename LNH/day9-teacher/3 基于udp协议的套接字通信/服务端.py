# from socket import *
#
# server=socket(AF_INET,SOCK_DGRAM)
# server.bind(('127.0.0.1',8080))
#
# # server.listen(5) #udp没有
# # server.accept() #udp没有
#
# # while True: #udp没有连接，更不可能有连接循环了
#     # server.accept() #udp没有
#
# while True: #通信循环
#     msg,client_addr=server.recvfrom(1024)
#     print(msg)
#     server.sendto(msg.upper(),client_addr)


