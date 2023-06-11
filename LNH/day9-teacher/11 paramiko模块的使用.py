# 基于用户名密码连接，远程执行命令
import paramiko
import time
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException,SSHException


'''总结：
paramiko是openssh的开源实现，实现了sshv2的协议

paramiko包含两个核心组件：SSHClient和SFTPClient。
SSHClient的作用类似于Linux的ssh命令，是对SSH会话的封装，该类封装了传输(Transport)，通道(Channel)及SFTPClient建立的方法(open_sftp)，通常用于执行远程命令。
SFTPClient的作用类似与Linux的sftp命令，是对SFTP客户端的封装，用以实现远程文件操作，如文件上传、下载、修改文件权限等操作。
Paramiko中的几个基础名词：

invoke_shell使用SSH的Shell通道，exec_command使用SSH的Exec通道。Shell通道类似模仿客户端使用的终端软件SSH登录至服务端，然后进行命令操作。而Exec通道则是模仿客户端把操作命令作为SSH参数直接发送至服务端执行。类似于GNU-Linux的如下命令：
ssh username@host command 
而Paramiko中有专门的Exec通道类：stdout，利用它，就可以一次性接收服务端回显。

Channel：是一种类Socket，一种安全的SSH传输通道;
Transport：是一种加密的会话，使用时会同步创建了一个加密的Tunnels(通道)，这个Tunnels叫做Channel;
Session：是client与Server保持连接的对象，用connect()/start_client()/start_server()开始会话。
Paramiko的基本使用

1. SSHClient常用的方法介绍
    (1) connect()：实现远程服务器的连接与认证，对于该方法只有hostname是必传参数。
        常用参数
        hostname 连接的目标主机
        port=SSH_PORT 指定端口
        username=None 验证的用户名
        password=None 验证的用户密码
        pkey=None 私钥方式用于身份验证
        key_filename=None 一个文件名或文件列表，指定私钥文件
        timeout=None 可选的tcp连接超时时间
        allow_agent=True, 是否允许连接到ssh代理，默认为True 允许l
        ook_for_keys=True 是否在~/.ssh中搜索私钥文件，默认为True 允许
        compress=False, 是否打开压缩

    (2) set_missing_host_key_policy()：设置远程服务器没有在know_hosts文件中记录时的应对策略。目前支持三种策略：
        设置连接的远程主机没有本地主机密钥或HostKeys对象时的策略，目前支持三种：
        AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
        WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
        RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项
    (3) exec_command()：在远程服务器执行Linux命令的方法。
    (4) open_sftp()：在当前ssh会话的基础上创建一个sftp会话。该方法会返回一个SFTPClient对象。
        利用SSHClient对象的open_sftp()方法，可以直接返回一个基于当前连接的sftp对象，可以进行文件的上传等操作.
        sftp = client.open_sftp()
        sftp.put('test.txt','text.txt')

'''

# 创建SSH对象
# ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务
# ssh.connect(hostname='172.26.31.231', port=22, username='root', password='iCourt12345')

# 执行命令
# while True:
#     cmd = input('>>: ').strip()
#     if len(cmd) == 0: continue
#     if cmd == 'quit' or cmd == 'exit': break
#     stdin, stdout, stderr = ssh.exec_command(cmd)
#     # 获取命令结果
#     result = stdout.read()
#     print(result.decode('utf-8'))
#     # 关闭连接
# ssh.close()



# 基于密钥登录
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


# stdin的用法：比如改密码的过程
# stdin,stdout,stderr = ssh.exec_command("passwd")
# stdin.write("old_password\nnew_password\nnew_password\n")    #因为密码要确认，所以要输两遍
# out,err = stdout.read(),stderr.read()
# if err != '':
#   print err
# else:
#   print out

'''
阻塞于非阻塞：
首先stdout是阻塞的， 只要stdout有信息就会一直等待，而stderr是非阻塞的，正常情况下可以将stdout重定向到stderr中，就可以实现

1、 同步阻塞：
    exec_command 拿到每个stdout的结果才会结束
2、同步非阻塞
    exec_command( 1>2&)
3、对于使用nohup的命令 最完善的写法如（cd /tmp; nohuo ./a.sh  1>2&  &  sleep 5)   
        &就是结束，不需要再加； 
        1>2& 重定向了stdout， a.sh会立刻返回，不会等待脚本里面的命令，
        get_pty=True加上这个另开线程，否则如果a.sh里面还有命令或者脚本可能不执行，但是有这个就会有stdout的输出 如果没有这个参数就不会有输出。
        还有一种用法就是如果还有需要大
4、 exec_timeout加这个参数，如果遇到特别大的时间也会有问题，只能作为强制结束使用，不让其成为僵死进程
    

'''


# 上传下载
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


# 在本机通过堡垒机连接，本质上是通过socket的方式连接远程主机 先连jump，然后开个个channel，这个channel就是隧道也就是一个socket，然后remote的机器paramiko绑定这个socket来访问
def get_remote_ssh_by_jump(remote_ssh_ip, remote_ssh_username, remote_ssh_password, remote_ssh_port=22):
    jump_ssh_ip = '110.238.83.48'
    jump_ssh_port = 22
    jump_ssh_username = 'myrds-only'
    jump_ssh_password = 'owGNFLOk73fEW'
    jump_server = paramiko.SSHClient()
    jump_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump_server.connect(hostname=jump_ssh_ip, port=jump_ssh_port, username=jump_ssh_username, password=jump_ssh_password)
    jump_transport = jump_server.get_transport()
    jump_channel = jump_transport.open_channel(kind='direct-tcpip', dest_addr=(remote_ssh_ip, remote_ssh_port),
                                               src_addr=(jump_ssh_ip, jump_ssh_port))
    remote_host = paramiko.SSHClient()
    remote_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_host.connect(hostname=remote_ssh_ip, port=remote_ssh_port, username=remote_ssh_username, password=remote_ssh_password,
                        sock=jump_channel)
    return remote_host


# remote_ssh = get_remote_ssh_by_jump('172.30.10.52', 'root', 'TtoIwvhFOHXz4eLF')
# stdin, stdout, stderr = remote_ssh.exec_command('ls -la  /root')
# print(stdout.read().decode('utf-8'))

'''判断远程文件是否存在'''


def check_remote_path(sftp, remote_path, is_mkdir=False):
    remote_path = normpath(remote_path)
    try:
        sftp.lstat(remote_path)
        return True
    except FileNotFoundError:
        if is_mkdir:
            sftp.mkdir(remote_path)
        else:
            return False


# 另外一种方式是使用ssh命令
# stdin, stdout, stderr = client.exec_command('ls DIR')
# if stdout.readline() != '':
#     print("exist")
# else:
#     print("not exist")

# 解压远程服务器上的文件
# 1、使用exec_command
# extract_command = f"tar -zxf {module_full_remote_name} -C {BASE_PATH}"
# stdin, stdout, stderr = remote_ssh.exec_command(extract_command)
# 2、使用sftp和tarfile  这个是读到了内存中，不适合大文件。
# f = sftp.open(remote_tar_file)
# bytes_io = BytesIO(f.read())
# f.close()
# with  tarfile.open(fileobj=bytes_io, mode='r:gz') as tar:
#     tar.extractall(remote_tar_file)

# 同时执行多个命令
# for command in commands:  # 这个方式是异步执行的  exec_command执行一次后channel就关闭了，不能复用。
#     stdin, stdout, stderr = remote_ssh.exec_command(command)
# 如果是同步执行，要使用invoke_shell发的方法 使用get_pty()获取一个伪终端后，需要使用invoke_shell()激活这个伪终端，激活成功后在伪终端中就可以向操作本机一样操作远程主机即所谓的交互式shell。当退出伪终端后，channel将被关闭，无法被复用。

# ssh.connect()
# shell = ssh.invoke_shell()
# for command in commands:  # 这里命令之间并不是同步执行的， invoke_shell其实也做不到一条一条的执行命令，就是等上一条命令执行完再执行下一条，这种效果目前只能通过将命令写在一起才能实现加get_pty=true
#     shell.send(command + '\n')
#     while not shell.recv_ready():
#         pass
#     print(shell.recv(1024).decode())
# 会遇到的问题，超时问题(func_timeout 函数来解决) ，返回信息太多显示不全的问题。


# 完整封装：


class Sshremote(object):
    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.__k = None

    # 目前不使用反射的方式：
    # def run(self):
    #     cmd_str = self.cmd.split()[0]
    #     if hasattr(self, 'do_'+cmd_str):
    #         getattr(self, 'do_'+cmd_str)
    #     else:
    #         print('目前不支持该功能。')

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        try:
            transport.connect(username=self.user, password=self.passwd)
        except NoValidConnectionsError as e:
            print('连接失败： %s' % e)
        except AuthenticationException as e:
            print("认证失败： %s" % e)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def do_cmd(self, command):
        """
         执行shell命令,返回字典
         return {'color': 'red','res':error}或
         return {'color': 'green', 'res':res}
        :param command:
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command,get_pty=True,timeout=60)
        #exec_command都是一次性拿结果的，区别是如果有get_pty的话这个是shell的方式执行，stderr也是会返回的，否则就只能从stderr专门去。这个地方设置超时生效的前提是没有stdout输出，
        while not stdout.channel.exit_status_ready():
            result=stdout.read().decode('utf-8')
            print(result)
            if stdout.channel.exit_status_ready():
                print(stdout.read().decode('utf-8'))
                break


    def do_cmd_invoke(self, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()
        ssh._transport = self.__transport
        shell = ssh.invoke_shell()
        cmd_exit=command+";exit"
        results = ""
        shell.send(cmd_exit+ '\n')
        while  not shell.recv_ready(): # 保证下面取数据的时候，数据已经到达
            time.sleep(0.1)
        # 分批取造成的粘包问题3个解决方法，
        # 　a）发送实际数据前，server端先发数据大小，client端持续接收，并且最后一次不收1024，而收实际大小，但是像paramiko这种server端无法改造的不适用（老男孩pythonsocket编程就是这种解决思路）
        # 　b）明确结尾标示符，即做回显判断，每输入一条命令，都接收到“结尾标示符”为止，参考“pythonparamiko自动登录网络设备抓取配置信息”
        #  c）双线程,主线程做输入，子线程持续不断接收
        # 下面实验第2个, 就是发送一个预定义的命令来结束远程主shell，也就结束了数据接收，一般是exit。但这就需要在每个命令后面加一个exit或者是q
        while True:
            result=shell.recv(10240).decode('utf-8')
            print(result)
            if not result:  # 命令后面加了exit后 stdout就终端了，前提是之前的命令能正确执行完，否则执行不到exit命令，整个命令都会卡住的。
                break

    def upload(self, local_path, target_path):
        # 连接，上传
        try:
            self.connect()
            sftp = paramiko.SFTPClient.from_transport(self.__transport)
            sftp.put(local_path, target_path ,confirm=True)
            # print(os.stat(local_path).st_mode)
            # 增加权限
            # sftp.chmod(target_path, os.stat(local_path).st_mode)
            sftp.chmod(target_path, mode=0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀
            print('上传 %s 到 %s 上成功' %(target_path,self.host))
        except  Exception as e:
            print('ERROR: 上传 %s 到 %s 上失败 -- %s' %(target_path,self.host,e))

    def download(self, target_path, local_path):
        # 连接，下载
        try:
            self.connect()
            sftp = paramiko.SFTPClient.from_transport(self.__transport)
            sftp.get(target_path, local_path)
        except  Exception as e:
            print('ERROR: 下载 %s 上的 %s 文件失败 -- %s' % (self.host, target_path, e))

    # 销毁
    def __del__(self):
        self.close()

# unicode_utils.py
def to_str(bytes_or_str):
    """
    把byte类型转换为str
    :param bytes_or_str:
    :return:
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value



ssh=Sshremote(host='159.138.158.213',user='root',port=22,passwd='Lexin@2022')
# res=ssh.do_cmd('sleep 1;cat /var/log/hostguard/hostguard.log.10')
'''
res=ssh.do_cmd('sleep 1 ;cat /var/log/hostguard/hostguard.log.0')
res=ssh.do_cmd('cat /var/log/hostguard/hostguard.log.0;sleep 10')
这两种的区别：
核心的点还是有stdout的输出就认为在执行，否则就会计算timeout超时结束。
'''
# ssh.do_cmd_invoke('sleep 2 ;  cat /var/log/hostguard/hostguard.log.0')

ssh.upload('config.ini','/root/config.ini')

# print(res)