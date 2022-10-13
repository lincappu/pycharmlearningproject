# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import configparser
import paramiko

# 1.基于用户名和密码的sshclient方式登录
# ssh=paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# ssh.connect(hostname='172.30.0.120',port=22,username='root',password='iCourt12345')
# while  True:
#     inp=input('>>').strip()
#     if not inp:
#         continue
#     if inp=='quit':
#         break
#
#     stdin,stdout,stderr=ssh.exec_command(inp)
#     res=stdout.read()
#     if len(res)==0:
#         print(stderr.read())
#
#     else:
#         print(str(res,'utf-8'))
#
#
# ssh.close()



# 2.封装方法，隐藏属性。,调用文件的方式。
# class Paramikoclient(object):
#     def __init__(self, ini_file):
#         self.config = configparser.ConfigParser()
#         self.config.read(ini_file)
#         self.host = self.config.get('ssh', 'host')
#         self.port = self.config.get('ssh', 'port')
#         self.user = self.config.get('ssh', 'user')
#         self.pwd = self.config.get('ssh', 'pwd')
#         self.timeout = self.config.get('ssh', 'timeout')
#         self.client = paramiko.SSHClient()
#         self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.client.connect(hostname= self.host, port=self.port, username=self.user,password=self.pwd,timeout=float(self.timeout))
#
#     def run_ssh(self,cmd):
#         stdin,stdout,stderr=self.client.exec_command(cmd)
#         result=stdout.read()
#         if len(result) ==0:
#             print(stderr.read().decode())
#         else:
#             print(str(result,'utf-8'))
#
#
#     def close(self):
#         self.client.close()
#
#
#
# if __name__ == '__main__':
#     client=Paramikoclient('config.ini')
#     while True:
#         cmd=input('>>:').strip()
#         if not cmd:
#             continue
#         if cmd =='quit':
#             break
#         client.run_ssh(cmd)



# 3.通过 transpor 的方式
# import paramiko
# #实例化一个transport对象
# transport = paramiko.Transport(('172.16.32.129',2323))
# #建立连接
# transport.connect(username='root',password='123')
# #建立ssh对象
# ssh = paramiko.SSHClient()
# #绑定transport到ssh对象
# ssh._transport=transport
# #执行命令
# stdin,stdout,stderr=ssh.exec_command('df')
# #打印输出
# print(stdout.read().decode())
# #关闭连接
# transport.close()


# 4.基于密钥的 ssh 登陆
# import paramiko
# from  io import StringIO
#
# private = StringIO('id_rsa_21')
#
# pkey = paramiko.RSAKey.from_private_key(private)
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='172.30.0.120', port=22, username='root', pkey=pkey)
# stdin, stdout, stderr = ssh.exec_command('df')
# print(stdout.read().decode())
# ssh.close()




# 5.SFTPClient的使用

# put 功能

# import  paramiko
#
# trans=paramiko.Transport(('172.30.0.120',22))
# trans.connect(username='root',password='iCourt12345')
#
# sftp=paramiko.SFTPClient.from_transport(trans)
#
# localpath='id_rsa_21'
# remotepath='/tmp/id'
#
# sftp.put(localpath,remotepath)
# trans.close()



# 下载功能
# import  paramiko
#
# trans=paramiko.Transport(('172.30.0.120',22))
# trans.connect(username='root',password='iCourt12345')
#
# sftp=paramiko.SFTPClient.from_transport(trans)
#
# localpath='id_rsa_21'
# remotepath='/tmp/id'
#
# sftp.get(remotepath='/root/anaconda-ks.cfg',localpath='anaconda')
# trans.close()





#  综合函数实现：

# transport封装实现
import paramiko


class ssh(object):
    def __init__(self, hostdata):
        """
        初始化连接信息和ftp方法
        :param hostdata: 连接信息字段
        """
        self.ip = hostdata['ip']
        self.port = hostdata['port']
        self.user = hostdata['user']
        self.passwd = hostdata['passwd']
        self.transport = paramiko.Transport((self.ip, self.port))
        self.transport.connect(username=self.user, password=self.passwd)
        self.obj = paramiko.SSHClient()
        self.obj._transport = self.transport
        self.objsftp = self.obj.open_sftp()

    def run_cmd(self, cmd):
        """
        执行命令方法
        :param cmd: 需要执行的命令
        :return:
        """
        stdin, stdout, stderr = self.obj.exec_command(cmd)
        return stdout.read()

    def run_cmdlist(self, cmdlist):
        """
        执行命令方法列表
        :param cmdlist: 命令列表
        :return:
        """
        self.resultList = []
        for cmd in cmdlist:
            stdin, stdout, stderr = self.obj.exec_command(cmd)
            self.resultList.append(stdout.read())
        return self.resultList

    def get(self, remotepath, localpath):
        """
        下载文件方法(两个路径都要指定文件名)
        :param remotepath: 服务器路径
        :param localpath:  本地路径
        :return:
        """
        self.objsftp.get(remotepath, localpath)

    def put(self, localpath, remotepath):
        """
        上传文件方法(两个路径都要指定文件名)
        :param localpath: 本地路径
        :param remotepath: 服务器路径
        :return:
        """
        self.objsftp.put(localpath, remotepath)

    def close(self):
        """
        关闭方法
        :return:
        """
        self.objsftp.close()
        self.transport.close()


# 函数的使用
if __name__ == '__main__':
    hostdata = {
        'ip': '192.168.163.129',
        'port': 22,
        'user': 'root',
        'passwd': 'zhujingzhi',
    }
    host = ssh(hostdata)  # 实例化远程函数给数据库里面的IP 端口 用户名 密码信息
    v = host.run_cmd('df -h')  # 执行单个命令
    vstr = v.decode(encoding='utf-8', errors='strict')  # bytes转字符串
    v1 = host.run_cmdlist(['ls', 'df'])  # 执行命令列表
    print(hostdata['ip'])
    print(vstr)
    v = host.get('/root/anaconda-ks.cfg', 'D:\\采集\\a.cfg')  # 下载文件
    v = host.put('D:\\采集\\a.cfg', '/opt/a.cfg')  # 上传文件
    host.close()　



