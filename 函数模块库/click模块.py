#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/6/16 17:05
# @Project  : pycharmlearningproject
# @File     : click模块.py

'''
最简单的用法就是定义python可执行的命令行工具

command：使函数hello成为命令行接口
option：增加命令行选项
echo：输出结果，使用echo进行输出是为了更好的兼容性，因为python 2中的print是个语句，python 3中的print 是一个函数
default： 设置命令行参数的默认值
help：参数说明
type：参数类型，可以是string、int、float等
prompt：当在命令行中没有输入相应的参数时，会更具prompt提示用户输入
nargs：指定命令行参数接受的值的个数
required：是否为必填参数




扩展用法
场景一：我们限定用户输入的值，那么就需要使用Click模块中的Choice函数，Choice的参数是一个列表，该列表中列出所有可能的值。

@click.command()
@click.option('-c',required=True,type=click.Choice(['start','stop']))   # 限定-c的值为start，或者stop，required表示是否为必填参数
def getcommand(c):
    click.echo('command is %s' % c )

if __name__ == '__main__':
    getcommand()


场景二：应用程序从命令行读取密码。　
使用标准库中的argparse模块只能像输入普通参数一样输入密码。这种方式存在一定安全隐患，例如输入的密码会保存在history中，查看命令历史列表就能获取密码
在Click中，这个问题就能完美的解决，只需要是这prompt为True，那么我们就能交互式输入密码，设置hide_input为True，就能隐藏密码，设置confirmation_prompt为True，就可以进行密码的两次验证，使用起来非常便捷。

@click.command()
@click.option('-p',prompt='Your Password',hide_input=True,confirmation_prompt=True)
def getpassword(p):
    click.echo('Your Password is : %s' % p)

if __name__ == '__main__':
    getpassword()

'''

import time

import click


@click.command()
def main():
    click.echo('这是最简单的eho的功能')


# @click.command()
# @click.option("-i", "--id", required=True, help="input an id")
# @click.option("-n", "--num", type=int, help="input  a number", show_default=True)
# def main(id, num):
#     click.echo(f"your {id=} {num=}")


# 做一个小例子，根据用户的输入然后查询然后展示
@click.command()
@click.option('-u', '--username', type=str, help='输入用户名', required=True)
def main(username):
    click.echo(f'search user {username}')
    time.sleep(5)

    info = f"不好意思人太多了，久等了，您的信息来了。\n{'*' * 50}\n用户名 {username}\n" \
               f"密码: {123456}\n登录网站: 'abcqqcom' \n{'*' * 50}️\n目前密码唯一的不要修改哦！\n该条消息不用回复了，谢谢。"

    click.echo(info)






if __name__ == '__main__':
    main()
