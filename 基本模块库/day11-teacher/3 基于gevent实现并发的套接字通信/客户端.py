from socket import *
from threading import Thread,current_thread

def client():
    c=socket(AF_INET,SOCK_STREAM)
    c.connect(('127.0.0.1',8080))

    count=1
    while True:
        c.send(('%s say hello %s' %(current_thread().getName(),count)).encode('utf-8'))
        data=c.recv(1024)
        print(data)
        count+=1

    c.close()


if __name__ == '__main__':
    for i in range(500):
        t=Thread(target=client)
        t.start()