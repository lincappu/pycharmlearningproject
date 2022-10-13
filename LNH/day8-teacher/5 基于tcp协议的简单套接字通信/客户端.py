import socket

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',8081))


#发消息
phone.send('hello'.encode('utf-8'))

#收消息
data=phone.recv(1024)
print(data)

#关机
phone.close()



