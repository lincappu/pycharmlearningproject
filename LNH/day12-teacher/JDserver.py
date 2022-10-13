


import socket


sock=socket.socket()
sock.bind(("127.0.0.1",8080))
sock.listen(5)


while 1:

    conn,addr=sock.accept()

    data=conn.recv(1024)
    print(data)

    with open("index.html") as  f:
        data=f.read()

    conn.send(("http/1.1 200 Ok\r\n\r\n %s"%data).encode("utf8"))

    conn.close()