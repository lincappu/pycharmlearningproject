# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : FLS
# @Software : PyCharm
# @Time     : 2023/3/28 11:28
# @Project  : pycharmlearningproject
# @File     : invoke库.py


'''
tox、nox 和 invoke：
同样是任务自动化工具，invoke 与我们之前介绍过的 tox/nox 在侧重点上有所不同：
tox/nox 主要是在打包、测试、持续集成等方面的自动化（当然它们能做的还不止于此）
invoke 则更具普遍性，可以用在任何需要“执行任务”的场景，可以是无相关性的任务组，也可以是有顺序依赖的分步骤的工作流

这个文件需要被命名为 tasks.py

'''





'''
任务的分解与组合
通常一个大任务可以被分解成一组小任务，反过来，一系列的小任务也可能被串连成一个大任务。在对任务作分解、抽象与组合时，这里有两种思路：
对内分解，对外统一：只定义一个 @task 的任务，作为总体的任务入口，实际的处理逻辑可以抽象成多个方法，但是外部不感知到它们
多点呈现，单点汇总：定义多个 @task 的任务，外部可以感知并分别调用它们，同时将有关联的任务组合起来，调用某个任务时，也执行其它相关联的任务

第一种思路很容易理解，实现与使用都很简单，但是其缺点是缺少灵活性，难于单独执行其中的某个/些子任务。适用于相对独立的单个任务，通常也不需要 invoke 就能做到（使用 invoke 的好处是，拥有命令行的支持）。
第二种思路更加灵活，既方便单一任务的执行，也方便多任务的组合执行。实际上，这种场景才是 invoke 发挥最大价值的场景。

那么，invoke 如何实现分步任务的组合呢？可以在 @task 装饰器的“pre”与“post”参数中指定，分别表示前置任务与后置任务：

@task
def clean(c):
    c.run("echo clean")

@task
def message(c):
    c.run("echo message")

@task(pre=[clean], post=[message])
def build(c):
    c.run("echo build")
clean 与 message 任务作为子任务，可以单独调用，也可以作为 build 任务的前置与后置任务而组合使用：

>>> inv clean
clean
>>> inv message
message
>>> inv build
clean
build
message
这两个参数是列表类型，即可设置多个任务。另外，在默认情况下，@task 装饰器的位置参数会被视为前置任务，接着上述代码，我们写一个：

@task(clean, message)
def test(c):
    c.run("echo test")
然后执行，会发现两个参数都被视为了前置任务：

>>> inv test
clean
message
test
3.3 模块的拆分与整合
如果要管理很多相对独立的大型任务，或者需要多个团队分别维护各自的任务，那么，就有必要对 tasks.py 作拆分与整合。

例如，现在有多份 tasks.py，彼此是相对完整而独立的任务模块，不方便把所有内容都放在一个文件中，那么，如何有效地把它们整合起来管理呢？

invoke 提供了这方面的支持。首先，只能保留一份名为“tasks.py”的文件，其次，在该文件中导入其它改名后的任务文件，最后，使用 invoke 的 Collection 类把它们关联起来。

我们把本文中第一个示例文件改名为 task1.py，并新建一个 tasks.py 文件，内容如下：

# 文件名：tasks.py
from invoke import Collection, task
import task1

@task
def deploy(c):
    c.run("echo deploy")

namespace = Collection(task1, deploy)
每个 py 文件拥有独立的命名空间，而在此处，我们用 Collection 可以创建出一个新的命名空间，从而实现对所有任务的统一管理。效果如下：

>>> inv -l
Available tasks:

  deploy
  task1.greet
  task1.hello
>>> inv deploy
deploy
>>> inv task1.hello
Hello world!
>>> inv task1.greet 武汉
武汉加油!

关于不同任务模块的导入、嵌套、混合、起别名等内容，还有不少细节，请查阅官方文档了解。






命令空间：
每个py文件就是一个独立的空间，所有的任务都会加入这个空间，这个空间是为命令的隐试空间，但必须要有 就是上面的 c

'''


# 也可以作为命令行工具使用  cli命令













# 命令空间： 模块之间的组合：
from invoke  import task,Collection
import tasks1

@task
def deploy(c):
    c.run('echo deploy')

ns=Collection(tasks1,deploy) # 将task1的中任务和deploy任务联和起来，放进同一个命令空间中执行，
# ns.add_task(tasks1,deploy) # 或者是这种写法







