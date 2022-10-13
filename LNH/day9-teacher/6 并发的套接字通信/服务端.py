from socket import *
from multiprocessing import Process

def talk(conn,addr):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()

def server():
    s=socket()
    s.bind(('127.0.0.1',8080))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        print('客户端 %s:%s' %(addr[0],addr[1]))
        p=Process(target=talk,args=(conn,addr))
        p.start()
    s.close()

if __name__ == '__main__':
    server()



# 开进程变成一个，发消息变成一个，这样就可以做到互相不干扰，由开进程的去调用发消息的，这样就可以相互不影响。