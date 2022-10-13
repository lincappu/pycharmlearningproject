# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  getpass


'''
getpass模块提供了平台无关的在命令行下输入密码的方法; 该模块主要提供:

两个函数: getuser, getpass
一个报警: GetPassWarning(当输入的密码可能会显示的时候抛出，该报警为UserWarning的一个子类)
备注: 上面为密码显示时抛出的报警


getpass.getuser()
该函数返回登陆的用户名,不需要参数
该函数会检查环境变量LOGNAME,USER,LNAME 和USERNAME, 以返回一个非空字符串。如果这些变量的设置为空的话，会从支持密码的数据库中获取用户名，否则会触发一个找不到用户的异常！


getpass.getpass([prompt[, stream]])
会显示提示字符串, 关闭键盘的屏幕回显，然后读取密码
可带提示符, 不带提示符，则会输入默认提示符'Password: '
在Linux/Unix系统, 提示符会写入到类文件流中，默认写入到/dev/tty, 如果写入不了的话，会写入到sys.stderr中。如果调getpass()函数时显示密码时，会抛出一个GetPassWarning报警，该报警从sys.stdin中读取

备注: 通过IDLE中来调getpass函数，会显示输入的密码，必须在Python Shell或Windows下的CMD才不会显示密码



【示例】


'''

