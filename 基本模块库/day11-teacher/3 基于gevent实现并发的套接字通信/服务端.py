from gevent import monkey;monkey.patch_all()
import gevent
from socket import *

def server(ip,port):
    server=socket(AF_INET,SOCK_STREAM)
    server.bind((ip,port))
    server.listen()
    while True:
        conn,addr=server.accept()
        g1=gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            print(data)
            conn.send(data.upper())
        except Exception:
            break

if __name__ == '__main__':
    server('127.0.0.1',8080)