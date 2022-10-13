#TCP
# import socketserver
#
# class.txt MyTCPhandler(socketserver.BaseRequestHandler): #通信
#     def handle(self):
#         while True:
#             # conn.recv(1024)
#             data=self.request.recv(1024)
#             self.request.send(data.upper())
#
#
# if __name__ == '__main__':
#     # print(socketserver.ForkingTCPServer)
#
#     s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyTCPhandler)
#     s.serve_forever()


#UDP
import socketserver

class MyTCPhandler(socketserver.BaseRequestHandler): #通信
    def handle(self):
        print(self.request)
        client_data=self.request[0]
        self.request[1].sendto(client_data.upper(),self.client_address)

if __name__ == '__main__':
    s=socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyTCPhandler)
    s.serve_forever()


