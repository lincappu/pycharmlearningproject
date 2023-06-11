#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/21 15:37
# @Project  : pycharmlearningproject
# @File     : prometheus相关.py

'''
主要涉及组件的安装与更新，服务的设置。

'''

import sys
from pathlib import Path
import time

import paramiko

remote_ip = {
    'mexico-cdh-prod': {
        # 'ip': ['172.16.0.234','172.16.0.143','172.16.0.146','172.16.0.39','172.16.0.207'],
        'user': 'root',
        'password': 'Lexin@901',
        'port': 22,
    },
    'mexico-mrs-prod': {
        'ip': ['172.16.0.12','172.16.0.180','172.16.0.10','172.16.0.213','172.16.0.252','172.16.0.171','172.16.0.14','172.16.0.221'],
        # 'ip': ['172.16.0.168'],
        'user': 'root',
        'password': 'QGjklm123485.',
        'port': 22,
    },
    "temp": {
        'ip': [],
        'user': '',
        'password': '',
        'port': 22,
    },
}

BASE_PATH = '/opt/prometheus/'
module = {
    "node_exporter": {
        "version": "-1.5.0",
        "platform": ".linux-amd64.tar.gz",
        "path": BASE_PATH + "node_exporter",
        "download_url": "https://nas.biencash.net/nas/api/public/dl/1oPEFV-8",
        "service_down_url": "https://nas.biencash.net/nas/api/public/dl/wzCR7k5l",
        "service_file_path": "/usr/lib/systemd/system/node_exporter.service",
    }
}


def normpath(path):
    """
    由于windows和linux操作系统不同，路径格式会出现不统一的情况，反斜杠不处理的话会出现很多问题
    替换windows路径中的\
    :param path:
    :return:
    """
    if isinstance(path, Path):
        path = str(path)
    return path.replace('\\', '/')


#  判断远程文件是否存在
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



def check_service(service):
    pass



# exec_command执行的结果并返回错误信息
def exec_result(stdin, stdout, stderr):
    if stdout.channel.recv_exit_status() != 0:  # exit_code就是linux的exit_code
        for line in stderr.readlines():
            print(line.strip())
        sys.exit(1)
    # else:
    #     print(stdout.read().decode('utf-8'))



# invoke_shell的方式执行任务
def command_exec_invoke(ip,user,password,cmd,recv_end_prompt='',recv_size=102400,port=22):
    if ip is None or user is None or cmd is None:
        print('执行命令传入的参数有误请，重新输入： %s ' %(ip,user,password))
        sys.exit(1)
    remote_ssh = get_remote_ssh_by_jump(ssh_ip=ip, ssh_user=user,ssh_password=password,ssh_port=port)
    remote_transport = remote_ssh.get_transport()
    sftp = paramiko.SFTPClient.from_transport(remote_transport)
    shell = remote_ssh.invoke_shell()
    results = ""
    shell.send(cmd + '\n')
    while not shell.recv_ready():
        time.sleep(0.02)
    while shell.recv_ready():
        results += shell.recv(recv_size).decode('utf-8')
    print(results)




def get_remote_ssh_by_jump(ssh_ip, ssh_user, ssh_password, ssh_port=22):
    jump_ssh_ip = '110.238.83.48'
    jump_ssh_port = 22
    jump_ssh_username = 'myrds-only'
    jump_ssh_password = 'owGNFLOk73fEW'
    jump_server = paramiko.SSHClient()
    jump_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jump_server.connect(hostname=jump_ssh_ip, port=jump_ssh_port, username=jump_ssh_username, password=jump_ssh_password)
    jump_transport = jump_server.get_transport()
    jump_channel = jump_transport.open_channel(kind='direct-tcpip', dest_addr=(ssh_ip, ssh_port),src_addr=(jump_ssh_ip, jump_ssh_port))
    remote_host = paramiko.SSHClient()
    remote_host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_host.connect(hostname=ssh_ip, port=ssh_port, username=ssh_user, password=ssh_password,sock=jump_channel)
    return remote_host



# remote_ssh = get_remote_ssh_by_jump('172.30.10.52', 'root', 'TtoIwvhFOHXz4eLF')
# stdin,stdout,stderr= remote_ssh.exec_command('ls -la  /root')
# print(stdout.read().decode('utf-8'))


# 下载指定版本的组件
# def  download_module_version(module_name,module_version):



def install_module(module_name, ip_group):
    if module_name not in ('node_exporter',):
        print('%s 组件名输入错误！ 请输入正确的组件名' % module_name)
        sys.exit(1)

    for ip in remote_ip[ip_group]['ip']:
        module_full_remote_version_path = BASE_PATH + module_name + module[module_name]['version']
        module_full_remote_name = module_full_remote_version_path + module[module_name]['platform']
        # if check_remote_path(sftp, BASE_PATH, is_mkdir=True) and check_remote_path(sftp, module_full_remote_version_path,is_mkdir=True):
            # 异步执行
            # # 下载组件包
            # # sftp.put('./' + module_full_name, module_full_remote_name, confirm=True)
            # downlaod_module_command = f"cd {BASE_PATH}; wget {module[module_name]['download_url']} -O {module_full_remote_name}"
            # stdin, stdout, stderr = remote_ssh.exec_command(downlaod_module_command)
            # exec_result(stdin, stdin, stderr)
            # # 解压组件包
            # extract_command = f"tar -zxf {module_full_remote_name}  --strip-components 1  -C {module_full_remote_version_path}"
            # stdin, stdout, stderr = remote_ssh.exec_command(extract_command)
            # exec_result(stdin, stdin, stderr)
            # # 软链到对应版本的组件包
            # ln_command = f"ln -s {module_full_remote_version_path}  {module[module_name]['path']}"
            # stdin, stdout, stderr = remote_ssh.exec_command(ln_command)
            # exec_result(stdin, stdin, stderr)
            #
            # # 下载module的service的服务配置文件
            # downlaod_command = f"cd {BASE_PATH}; wget {module[module_name]['service_down_url']} -O {module[module_name]['service_file_path']}"
            # stdin, stdout, stderr = remote_ssh.exec_command(downlaod_command)
            # exec_result(stdin, stdin, stderr)
            # # 启动组件服务
            # start_command = f"systemctl daemon-reload; systemctl  restart node_exporter; systemctl status node_exporter"
            # stdin, stdout, stderr = remote_ssh.exec_command(downlaod_command)
            # exec_result(stdin, stdin, stderr)

            #修改同步执行：

        mkdir_com = f"if [ ! -d {BASE_PATH} ];then mkdir {BASE_PATH} ;fi; if [ ! -d {module_full_remote_version_path} ];then mkdir {module_full_remote_version_path}; fi;"
        install_com = f"cd {BASE_PATH}; wget  --no-check-certificate  {module[module_name]['download_url']} -O {module_full_remote_name};tar -zxf {module_full_remote_name}  --strip-components 1  -C {module_full_remote_version_path};ln -s {module_full_remote_version_path}  {module[module_name]['path']}"
        startsvc_com = f"cd {BASE_PATH}; wget  --no-check-certificate  {module[module_name]['service_down_url']} -O {module[module_name]['service_file_path']};systemctl daemon-reload;systemctl enable node_exporter;systemctl  start node_exporter; systemctl status node_exporter"

        command_exec_invoke(ip=ip,user=remote_ip[ip_group]['user'],password=remote_ip[ip_group]['password'],cmd=mkdir_com)
        time.sleep(5)
        command_exec_invoke(ip=ip,user=remote_ip[ip_group]['user'],password=remote_ip[ip_group]['password'],cmd= install_com )
        time.sleep(5)
        command_exec_invoke(ip=ip,user=remote_ip[ip_group]['user'],password=remote_ip[ip_group]['password'],cmd=startsvc_com)
        time.sleep(5)

install_module('node_exporter', 'mexico-mrs-prod')



