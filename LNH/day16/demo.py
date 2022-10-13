#
#
# import requests
#
# data=requests.get("https://www.baidu.com/s?wd=alex",
#                   headers={
#                      "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
#                   }
#                   )
#
# with open("alex.html", "wb") as f:
#
#     f.write(data.content)




import socket

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8081))
    sock.listen(5)

    while True:
        print("server is working.....")
        conn, address = sock.accept()
        data = conn.recv(1024)
        conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n<h1>Hello Yuan</h1>","utf8"))
        conn.close()

if __name__ == '__main__':

    main()