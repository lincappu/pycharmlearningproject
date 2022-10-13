from socket import *


client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


client.send('hello'.encode('utf-8'))
# import time
# time.sleep(10)
client.send('world'.encode('utf-8'))


# 这个是在客户端粘了，因为发送的时间太短了。客