#基于用户名密码连接，远程执行命令
import paramiko

# 总结：
#
# paramiko包含两个核心组件：SSHClient和SFTPClient。
#
# SSHClient的作用类似于Linux的ssh命令，是对SSH会话的封装，该类封装了传输(Transport)，通道(Channel)及SFTPClient建立的方法(open_sftp)，通常用于执行远程命令。
# SFTPClient的作用类似与Linux的sftp命令，是对SFTP客户端的封装，用以实现远程文件操作，如文件上传、下载、修改文件权限等操作。
# Paramiko中的几个基础名词：
#
# Channel：是一种类Socket，一种安全的SSH传输通道;
# Transport：是一种加密的会话，使用时会同步创建了一个加密的Tunnels(通道)，这个Tunnels叫做Channel;
# Session：是client与Server保持连接的对象，用connect()/start_client()/start_server()开始会话。
# Paramiko的基本使用
#
# 1. SSHClient常用的方法介绍
#
# (1) connect()：实现远程服务器的连接与认证，对于该方法只有hostname是必传参数。
#
# 常用参数
# hostname 连接的目标主机
# port=SSH_PORT 指定端口
# username=None 验证的用户名
# password=None 验证的用户密码
# pkey=None 私钥方式用于身份验证
# key_filename=None 一个文件名或文件列表，指定私钥文件
# timeout=None 可选的tcp连接超时时间
# allow_agent=True, 是否允许连接到ssh代理，默认为True 允许l
# ook_for_keys=True 是否在~/.ssh中搜索私钥文件，默认为True 允许
# compress=False, 是否打开压缩
#
# (2) set_missing_host_key_policy()：设置远程服务器没有在know_hosts文件中记录时的应对策略。目前支持三种策略：
# 设置连接的远程主机没有本地主机密钥或HostKeys对象时的策略，目前支持三种：
#
# AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
# WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
# RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项
# (3) exec_command()：在远程服务器执行Linux命令的方法。
#
#
# (4) open_sftp()：在当前ssh会话的基础上创建一个sftp会话。该方法会返回一个SFTPClient对象。
#
# 利用SSHClient对象的open_sftp()方法，可以直接返回一个基于当前连接的sftp对象，可以进行文件的上传等操作.
#
# sftp = client.open_sftp()
# sftp.put('test.txt','text.txt')





# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务
ssh.connect(hostname='172.26.31.231', port=22, username='root', password='iCourt12345')

# 执行命令
while True:
    cmd=input('>>: ').strip()
    if len(cmd) ==0:continue
    if  cmd == 'quit' or cmd == 'exit': break
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    print(result.decode('utf-8'))
    # 关闭连接
ssh.close()


# 123.56.157.199:22022

# root
# HLH199300.

#基于密钥登录
# import paramiko
#
# private_key = paramiko.RSAKey.from_private_key_file(r'C:\\id_rsa')
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='123.56.157.199', port=22022, username='root', pkey=private_key)
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# # 关闭连接
# ssh.close()


#上传下载
# import paramiko
#
# transport = paramiko.Transport(('123.56.157.199', 22022))
# transport.connect(username='root', password='HLH199300.')
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# # 将location.py 上传至服务器 /tmp/test.py
# sftp.put(r'C:\\id_rsa', '/tmp/test.rsa')
# # 将remove_path 下载到本地 local_path
# # sftp.get('remove_path', 'local_path')
#
# transport.close()




