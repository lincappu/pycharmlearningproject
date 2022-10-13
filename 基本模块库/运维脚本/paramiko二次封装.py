# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS
import sys

import paramiko
import argparse

host = {
	'host': '172.16.1.146',
	'port': 10222,
	'user': 'root',
	'password': 'wbBiloHn7#Khpibk'
}


class SSHConnection:

	def __init__(self, host_config):
		self.host = host_config['host']
		self.port = host_config['port']
		self.user = host_config['user']
		self.password = host_config['password']

		self._transport = paramiko.Transport((self.host, self.port))
		self._transport.connect(username=self.user, password=self.password)
		self._sftp = paramiko.SFTPClient.from_transport(self._transport)

		self._ssh = paramiko.SSHClient()
		self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		self._ssh._transport = self._transport

	# 关闭通道
	def close(self):
		self._sftp.close()
		self._transport.close()

	# 上传文件到远程主机
	def upload(self, local_path, remote_path):
		self._sftp.put(local_path, remote_path)

	# 从远程主机下载文件到本地
	def download(self, remote_path, local_path, ):
		self._sftp.get(remote_path, local_path)

	# 在远程主机上创建目录
	def mkdir(self, target_path, mode=511):  # 这个是权限的 o777 是八进制的类型的，要转换为 10 进制
		self._sftp.mkdir(target_path, mode)

	# 删除远程主机上的目录
	def rmdir(self, target_path):
		self._sftp.rmdir(target_path)

	# 查看目录下文件以及子目录（如果需要更加细粒度的文件信息建议使用listdir_attr）
	def listdir(self, target_path):
		return self._sftp.listdir(target_path)

	# 删除文件
	def remove(self, target_path):
		self._sftp.remove(target_path)

	# 查看目录下文件以及子目录的详细信息（包含内容和参考os.stat返回一个FSTPAttributes对象，对象的具体属性请用__dict__查看）
	def listdirattr(self, target_path):
		list_dir = []  # 如果没有这一行，而且下面的命令没有执行，retur 执行了，就会出现未定义而引用的情况。
		try:
			list_dir = self._sftp.listdir_attr(target_path)
		except BaseException as e:
			print(e)
		return list_dir

	# 获取文件详情
	def stat(self, remote_path):
		return self._sftp.stat(remote_path)

	def exec_cmd(self, cmd):
		stdin, stdout, stderr = self._ssh.exec_command(cmd)
		result = stdout.read()
		print(result)
		return result


# 使用示例
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='ssh/sftp执行脚本', usage='%(prog)s [options]',epilog='祝你用的愉快',)

	parser.add_argument('-H','--host',nargs='?',dest='listhost',help='主机/多个主机用","分割')
	parser.add_argument('-f','--file',nargs='?',dest='filehost',help='主机文件列表')
	parser.add_argument('-m', '--command', nargs='?', dest='command', help='执行命令')
	parser.add_argument('-I', '--init', nargs='?', dest='init', help='自动分区挂盘')
	parser.add_argument('-A', '--add', nargs='?', dest='add_rsa', help='添加信任')
	parser.parse_args()

	if len(sys.argv)==1:
		parser.print_help()
	else:
		args=parser.parse_args()
		cmd=args.command

