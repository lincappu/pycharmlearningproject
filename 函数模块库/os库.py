# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import os

# os.name  目前已注册: 'posix', 'nt', 'java'.
# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True) 创建一个指向 src 的硬链接，名为 dst。
# os.curdir  返回当前目录: ('.')
# os.pardir  获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.walk('dirname')
# os.remove()  删除一个文件
# os.removedirs()  删除多个目录,就是级联删除
# os.rename("oldname","newname")  重命名文件/目录
# os.exit(code) 退出当前进程， 可以返回具体的 code 码
# os.stat('path/filename')  获取文件/目录信息
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'   java   ce 一共四种
# os.uanem() 返回系统的详细信息
# os.system("bash command")  运行shell命令，直接显示
# os.environ  获取系统环境变量    就是用户所有的环境变量
# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.split(path)  将path分割成目录和文件名二元组返回
# os.path.splitest(file)  按后缀分成两部分
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小
# os.path.getsize(file) 返回文件的大小，如果是文件夹则返回0
# os.access(file,mode)  mode 的值有：


print(os.name)

# os.ctermid()  返回与进程的控制终端对应的文件名 ,就是是哪个终端，就是/dev/tty 那几个
print(os.ctermid())
print(os.environ['HOME'])  # 一个表示字符串环境的 mapping 对象


# os.close(fd)  # 必须是用 os.open()打开的文件
# os.fsync(fd)  # 刷入磁盘
# os.ftruncate(fd,length=) # 将文件截断
# os.read(fd)
# os.write()

# 文件和目录：
# os.access(path=) # 测试uid 和 gid是否可访问文件
# os.chmod()  #










