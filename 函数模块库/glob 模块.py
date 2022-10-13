# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import glob


# 通配符	功能
# *	匹配0或多个字符
# **	匹配所有文件,目录，子目录和子目录里面的文件 (3.5版本新增)
# ？	匹配一个字符,这里与正则表达式? (正则?匹配前面表达式0次或者1次)
# []	匹配指定范围内的字符,如: [1-9]匹配1至9内的字符
# [!]	匹配不在指定范围内的字符

# 方法：
# glob.glob(pathname, *, recursive=False)
# 返回匹配 pathname 的可能为空的路径名列表，路径名必须为包含一个路径描述的字符串。 pathname 可以是绝对路径 (如 /usr/src/Python-1.5/Makefile) 或相对路径 (如 ../../Tools/*/*.gif)，并且可包含 shell 风格的通配符。 无效的符号链接可以包含在结果中 (与在 shell 中一样)。
# 如果 recursive 为真值，则模式 "**" 将匹配目录中的任何文件以及零个或多个目录、子目录和符号链接。 如果模式加了一个 os.sep 或 os.altsep 则将不匹配文件。
#
# 注解 在一个较大的目录树中使用 "**" 模式可能会消耗非常多的时间。
# 在 3.5 版更改: 支持使用 "**" 的递归 glob.
#
# glob.iglob(pathname, *, recursive=False)
# 返回一个 iterator，它会产生与 glob() 相同的结果，但不会实际地同时保存它们。
#
# glob.escape(pathname)
# 转义所有特殊字符 ('?', '*' 和 '[')。 这适用于当你想要匹配可能带有特殊字符的任意字符串字面值的情况。 在 drive/UNC 共享点中的特殊字符不会被转义，例如在 Windows 上 escape('//?/c:/Quo vadis?.txt') 将返回 '//?/c:/Quo vadis[?].txt'。



# 注意：glob 默认不匹配.开头的文件,如果有.开头的文件需要写成 glob.glob(".*.txt") 的格式



# for file in glob.glob('./*.py',recursive=True):
#     print(file)


# print(glob.glob('./os?.py'))


for file in glob.iglob('./*.py',recursive=True):
    print(file)



specials = '?*['

for char in specials:
    pattern = '**/*' + glob.escape(char) + '.txt'
    print('Searching for: {!r}'.format(pattern))
    for name in sorted(glob.glob(pattern,recursive=True)):
        print(name)
    print()