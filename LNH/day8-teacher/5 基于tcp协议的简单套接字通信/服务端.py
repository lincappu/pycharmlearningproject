import socket

# 买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#绑定手机卡
phone.bind(('127.0.0.1',8081))

#开机
phone.listen(5)

#等电话链接
print('starting...')
conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
print(conn)
# print(client_addr)

#收消息
data=conn.recv(1024) # 1024最大的限制
print('客户端数据: ',data)

#发消息
conn.send(data.upper())

print('sockname')
print(conn.getsockname())
print(phone.getsockname())
print(conn.getpeername())


#挂电话
conn.close()

#关机
phone.close()



