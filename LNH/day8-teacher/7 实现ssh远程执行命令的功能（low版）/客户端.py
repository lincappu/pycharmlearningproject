import socket
import struct

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',10101))


while True:
    #发消息
    cmd=input('>>: ').strip()
    if not cmd:continue    # 空会卡住
    phone.send(cmd.encode('utf-8'))

    #先收报头
    header_struct=phone.recv(4)
    total_size=struct.unpack('i',header_struct)[0]

    #再收消息
    cmd_res=b''
    recv_size=0
    while recv_size < total_size:
        recv_data=phone.recv(1024)
        cmd_res+=recv_data
        recv_size+=len(recv_data)

    print(cmd_res.decode('utf-8'))

#关机
phone.close()











