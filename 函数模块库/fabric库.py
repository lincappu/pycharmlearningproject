#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/26 21:26
# @Project  : pycharmlearningproject
# @File     : fabric库.py

'''
版本不兼容：
1.X是命令行模式
2.x是python模式
3.x是个人版

fabric是在paramiko再次封装的实现。

1、Connection 参数详解
        self,
        host,           # 主机 ip
        user=None,      # 用户名
        port=None,      # ssh 端口，默认 22
        config=None,    # 登录配置文件
        gateway=None,   # 连接网关
        forward_agent=None,     # 是否开启 agent forwarding
        connect_timeout=None,   # 设置超时
        connect_kwargs=None,    # 设置密码登录 connect_kwargs={"password": "123456"}
                                # 还是密钥登录 connect_kwargs={"key_filename": "/home/myuser/.ssh/id_rsa"}
        inline_ssh_env=None,

run参数的有：
    command是要执行的命令字符串
    warn当命令执行异常退出时默认是抛出UnexpectedExit异常,如果设置warn则不会抛出错误而是改为抛出警告
    hide可选的值为
        "out"/"stdout" 打印远端的stdout输出的结果
        "err"/"stderr" 打印远端的stderr输出的结果
        "both"/Truestdout或者stderr输出的结果都打印
        None所有都打印(默认)
        False都不打印
    disown 相当于nohup command &
    env其值为一个字典,用于定义命令执行时的环境变量
    encodingstdout和stderr的文本编码
    watchers定义监控,一般用于自动填写stdin.




登录方式：
    指定私钥
    参数字段connect_kwargs.key_filename
    参数配置示例
      connect_kwargs={
          "key_filename":"<path>"
      }
    指定私钥且私钥有密码
    参数字段connect_kwargs.key_filename,connect_kwargs.passphrase
    参数配置示例
      connect_kwargs={
          "key_filename":"<path>",
          "passphrase":"132"
      }
    命令行参数设置--prompt-for-passphrase=132
    密码登录
    参数字段connect_kwargs.password
    参数配置示例
      connect_kwargs={
          "password":"12421"
      }
    命令行参数设置--prompt-for-login-password=12421




2、conn对象属性
        run        # 执行远程命令，如：run('uname -a')
        cd        # 切换远程目录，如：cd('/root'); with conn.cd('/root'),继承这个状态
        put        # 上传本地文件到远程主机，如：put('/root/test.py','/root/test.py')
        get        # 获取服务器上文件，如：get('/root/test.py')
        sudo     # sudo方式执行远程命令，如： sudo('service docker start')
        local    # 执行本地命令，如：conn.local('ls')
'''


from fabric2  import Connection,Config
from fabric2 import SerialGroup

#不用print自动回显结果
# results=Connection(host='110.238.83.48',user='myrds-only',port=22,connect_kwargs={'password':'owGNFLOk73fEW'}).run('sleep 10 ;ls /tmp')
# connection的参数
# print(results.stdout)
# print(results.stderr)
# print(results.command)
# print(results.env)
# print(results.encoding)
# print(results.exited)
# print(results.failed)
# print(results.hide)
# print(results.ok)
# print(results.pty)
# print(results.return_code)
# print(results.shell)
# print(results.hide)

# con=Connection('deploy@web1:2202') # 主机可以这种形式。


# con=Connection(host='110.238.83.48',user='myrds-only',port=22,connect_kwargs={'password':'owGNFLOk73fEW'},connect_timeout=30)
# 串行阻塞执行:
# con.run('sleep 10')
# con.run('pwd')
# con.run('ls /tmp')



'''批量操作 ： 多个主机执行同一个命令，
for host in ('root@1','root@2'):
     con=Connection(host=host,connect_kwargs={"password":'123'}).run('ls')
     print(con.stdout)
上面的问题
1、如果是不同功能的组合，则for循环太多
2、如果将结果集聚合的话，需要额外的操作
3、for是同步执行的，效率慢，并且没有异常处理机制，中间出错就跳出了，

fabric引入的Group的概念：
SeriaGroup  串行执行
ThreadingGroup并发执行
'''

# 这种适用于相同的密码
pool=SerialGroup('root@110.238.83.4822','root@159.138.158.213:22',connect_kwargs={'password':'123456'})
# pool.run('ls')
# #或者是
# for p in  pool:
#     p.run('ls')
# 或者是with方法
# if __name__ == "__main__":
#     with Group('remote1', 'remote2') as group:
#         results = group.run('echo helloworld', hide=True)
#         for conn, result in results.items():
#             msg = f"conn {conn.host} Ran {result.command!r} on {result.connection.host}, got stdout:\n{result.stdout}"
#             print(msg)


# 交互，如要输入密码，或者yes  处理方式有几种。
from invoke  import Responder
sudopass=Responder(
    pattern=r'\[sudo\] password',
    response='Lexin@2022\n') #\n  这里是模拟回车的效果
con=Connection(host='159.138.158.213',user='fabric',port=22,connect_kwargs={'password':'Lexin@2022'},connect_timeout=30)
con.run('sudo whoami',pty=True,watchers=[sudopass]) # wachers
# import getpass
# sudo_pass=getpass.getpass('nidepass:')
# config=Config(overrides={'sudo':{'password':"5QwTbbCvEowGNW!A"}})
# con2=Connection(host='110.238.83.48',user='myrds-only',port=22,connect_kwargs={'password':'owGNFLOk73fEW'},connect_timeout=30,config=config)
# con2.sudo('ls /root',pty=True)


# 上传、下载， 就直接put 和get  一定要带文件名，不能直接写目录，put是home目录， 要cd的话要先执行 cd命令，然后with cd（’/root‘） 这样来执行



'''
执行本地命令：
1、要么是con.lcoal()
2、要么是
import  invoke
invoke.run()
这样执行的是本地的命令

'''


