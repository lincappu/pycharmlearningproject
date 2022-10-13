# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  argparse

parser=argparse.ArgumentParser(description='功能：输入数字计算数字的和',
							   usage='python3 %(prog)s [option]',
							   epilog='祝你用的愉快',
							   )

# 位置参数是必须要填的
# parser.add_argument('sum1',type=int,nargs='+',default=0,help='传入的数字')
# args=parser.parse_args()  #  执行这条命令后才能真正添加进参数
# print(args)
# print(args.sum1)
# print(sum(args.sum1))

# 位置参数有多个的情况：
# parser.add_argument('sum2',type=int,nargs='+',default=0,help='传入的数字')
# args=parser.parse_args()
# print(args.sum1,args.sum2)  # [1, 2] [3]，就是最后一个变量只有一个参数，多的参数都给前面。


'''
设置参数的类型,并且要接受多个数值：
add_argument中有type参数可以设置传入参数的数据类型。我们看到代码中有type这个关键词，该关键词可以传入list, str, tuple, set, dict等。例如我们把上面的type=str，改成type=int,这时候我们就可以进行四则运算。
'''
# parser.add_argument('sum',type=int,nargs='+',help='输入的数字')
# 参数nargs：
# nargs='*' 　表示参数可设置零个或多个
# nargs='+' 表示参数可设置一个或多个
# nargs='?'　表示参数可设置零个或一个
# args=parser.parse_args()
# print(args.sum)
# print(sum(args.sum))



'''
位置参数改成关键字参数（其实是可选参数--）  --是长参数格式，也是默认显示的格式，-是短参数格式
在命令行中传入参数时候，传入的参数的先后顺序不同，运行结果往往会不同，这是因为采用了位置参数，改写成关键字参数
'''
# parser.add_argument('-f','--first',type=str,help='姓')
# parser.add_argument('-s','--second',type=str,help='名')
# args=parser.parse_args()
# print(args.first+args.second)


'''
参数默认值
add_argument中有一个default参数。有的时候需要对某个参数设置默认值，即如果命令行中没有传入该参数的值，程序使用默认值。如果命令行传入该参数，则程序使用传入的值
'''
# parser.add_argument('--first',type=str,default='张',help='姓')
# parser.add_argument('--second',type=str,default='三',help='名')
# args=parser.parse_args()
# print(args.first+args.second)


'''
必需参数  这个只是在可选参数的必须参数，
add_argument有一个required参数可以设置该参数是否必需。
'''
parser.add_argument('--first',type=str,default='张',help='姓')
parser.add_argument('--second',type=str,required=True,help='名')
args=parser.parse_args()
print(args.first+args.second)


'''
# ArgumentParser类的理解：

class ArgumentParser(_AttributeHolder, _ActionsContainer):
    """Object for parsing command line strings into Python objects.

    Keyword Arguments:
        - prog -- The name of the program (default: sys.argv[0])
        - usage -- A usage message (default: auto-generated from arguments)
        - description -- A description of what the program does
        - epilog -- Text following the argument descriptions
        - parents -- Parsers whose arguments should be copied into this one
        - formatter_class -- HelpFormatter class for printing help messages
        - prefix_chars -- Characters that prefix optional arguments
        - fromfile_prefix_chars -- Characters that prefix files containing
            additional arguments
        - argument_default -- The default value for all arguments
        - conflict_handler -- String indicating how to handle conflicts
        - add_help -- Add a -h/-help option
    """

    def __init__(self,
                 prog=None,
                 usage=None,
                 description=None,
                 epilog=None,
                 version=None,
                 parents=[],
                 formatter_class=HelpFormatter,
                 prefix_chars='-',
                 fromfile_prefix_chars=None,
                 argument_default=None,
                 conflict_handler='error',
                 add_help=True):
prog - 程序的名字（默认：sys.argv[0]）
usage - 描述程序用法的字符串（默认：从解析器的参数生成）
description - 参数帮助信息之前的文本（默认：空）
epilog - 参数帮助信息之后的文本（默认：空）
parents - ArgumentParser 对象的一个列表，这些对象的参数应该包括进去
formatter_class - 定制化帮助信息的类
prefix_chars - 可选参数的前缀字符集（默认：‘-‘）
fromfile_prefix_chars - 额外的参数应该读取的文件的前缀字符集（默认：None）
argument_default - 参数的全局默认值（默认：None）
conflict_handler - 解决冲突的可选参数的策略（通常没有必要）
add_help - 给解析器添加-h/–help 选项（默认：True）




ArgumentParser.add_argument方法：

ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
定义应该如何解析一个命令行参数。下面每个参数有它们自己详细的描述，简单地讲它们是：

name or flags - 选项字符串的名字或者列表，例如foo 或者-f, --foo。
action - 在命令行遇到该参数时采取的基本动作类型。
nargs - 应该读取的命令行参数数目。
const - 某些action和nargs选项要求的常数值。
default - 如果命令行中没有出现该参数时的默认值。
type - 命令行参数应该被转换成的类型。
choices - 参数可允许的值的一个容器。
required - 该命令行选项是否可以省略（只针对可选参数）。
help - 参数的简短描述。
metavar - 参数在帮助信息中的名字。
dest - 给parse_args()返回的对象要添加的属性名称。




重点介绍：
action: 这个参数算是一个重头戏而且可以继承 argparse.Action 定制自己的 action 。先介绍几个这个参数常用的变量

复制代码
'store' - 只是保存参数的值。这是默认的动作。例如：

>>>
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args('--foo 1'.split())
Namespace(foo='1')
'store_const' - 保存由const关键字参数指出的值。（注意const关键字参数默认是几乎没有帮助的None。）'store_const'动作最常用于指定某种标记的可选参数。例如：

>>>
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_const', const=42)
>>> parser.parse_args('--foo'.split())
Namespace(foo=42)
'store_true'和'store_false' - 它们是'store_const' 的特殊情形，分别用于保存值True和False。另外，它们分别会创建默认值False 和True。例如：

>>>
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('--bar', action='store_false')
>>> parser.add_argument('--baz', action='store_false')
>>> parser.parse_args('--foo --bar'.split())
Namespace(bar=False, baz=True, foo=True)
'append' - 保存一个列表，并将每个参数值附加在列表的后面。这对于允许指定多次的选项很有帮助。示例用法：

>>>
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='append')
>>> parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2'])
'append_const' - 保存一个列表，并将const关键字参数指出的值附加在列表的后面。（注意const关键字参数默认是None。）'append_const' 动作在多个参数需要保存常量到相同的列表时特别有用。例如：

>>>
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--str', dest='types', action='append_const', const=str)
>>> parser.add_argument('--int', dest='types', action='append_const', const=int)
>>> parser.parse_args('--str --int'.split())
Namespace(types=[<type 'str'>, <type 'int'>])


'count' - 计算关键字参数出现的次数。例如，这可用于增加详细的级别：
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count')
>>> parser.parse_args('-vvv'.split())
Namespace(verbose=3)
'help' - 打印当前解析器中所有选项的完整的帮助信息然后退出。默认情况下，help动作会自动添加到解析器中。参见ArgumentParser以得到如何生成输出信息。

'version' - 它期待version=参数出现在add_argument()调用中，在调用时打印出版本信息并退出：
>>>
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
>>> parser.parse_args(['--version'])
PROG 2.0

'''


# 这个和 sys 模块的联系：
# import  sys
#
# print(sys.argv)
# print(sys.exit(1))
# print(sys.version)
# print(sys.path)
# print(sys.stdin)
# print(sys.stdout)
# print(sys.stderror)





