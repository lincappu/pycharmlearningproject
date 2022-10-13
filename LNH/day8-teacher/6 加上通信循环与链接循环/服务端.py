import socket

#买手机
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议
# # phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
#
# #绑定手机卡
# phone.bind(('127.0.0.1',8080))
#
# #开机
# phone.listen(5)
#
# #等电话链接
# print('starting...')
# while True:
#     conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
#     print(client_addr)
#
#     while True: #通信循环
#         #收消息
#         try:
#             data=conn.recv(1024) # 1024最大的限制
#             print('客户端数据: ',data)
#             if not data:break #针对linux系统
#             #发消息
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#
#     #挂电话
#     conn.close()
#
# #关机
# phone.close()



phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',10000))

phone.listen(10)

while True:
    print('server starting.....')
    conn,client_addr=phone.accept()
    print(client_addr)

    while True:
        try:
            data=conn.recv(1024)
            print('client data:', data)
            if not data:
                break
            conn.send(data.upper())

        except ConnectionResetError:
            break
    conn.close()


phone.close()








