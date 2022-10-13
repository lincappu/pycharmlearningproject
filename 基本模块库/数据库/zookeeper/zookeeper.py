# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import json
import time
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.client import DataWatch
from kazoo.client import ChildrenWatch
from kazoo.client import Transaction
from kazoo import exceptions
import threading
import os
import multiprocessing
import random
import sys


#
# zk=KazooClient(hosts="47.110.87.5:2181")
# zk.start()
# print(zk.get_children('/zl1'))
# id=zk.create("/zk1",value=b"zktest",acl=None,ephemeral=True, sequence=True, makepath=True)
#
# print(id)
# print()
'''
该类是kazoo模块的最主要的一个类，用于连接zookeeper服务器，参数：

`hosts`：指定ZooKeeper的ip和端口，可以是以逗号分隔的多个ZooKeeper服务器IP和端口，客户端会随机选择一个来连接。
`timeout`：会话超时时间，在连接断开后就开始计算，如果在此会话时间内重新连接上的话，该连接创建的临时节点就不会移除。默认会话超时最小是2倍的tickTime(在zk服务器配置文件中设置），最大是20倍的tickTime。会话过期由ZooKeeper集群，而不是客户端来管理。客户端与集群建立会话时提供该超时值，集群使用这个值来确定客户端会话何时过期，集群在指定的超时时间内没有得到客户端的消息时发生会话过期，会话过期时集群将删除会话的所有临时节点，立即通知所有(观察节点)客户端。
`client_id`：传递一个双元素数组：[会话id, 密码]。客户端取得ZooKeeper服务句柄时，ZooKeeper创建一个会话，由一个64位数标识，这个数将返回给客户端。如果连接到其他服务器，客户端将在连接握手时发送会话ID。出于安全考虑，服务器会为会话ID创建一个密码，ZooKeeper服务器可以校验这个密码。这个密码将在创建会话时与会话ID一同发送给客户端。与新的服务器重新建立会话的时候，客户端会和会话ID一同发送这个密码。
`read_only`：创建一个只读的连接。
`randomize_hosts`：随机选择zk服务器连接。
'''
# print(zk.state)
# zk.start()
# print(zk.state)
# print(zk.connected)
# print(zk.stop())
# print(zk.state)
# print(zk.close())
# print(zk.state)


# 节点操作和zk 属性获取
'''k节点(znode)可以分为如下四类：

`PERSISTENT`：持续的，相比于EPHEMERAL，不会随着client session的close/expire而消失
`PERSISTENT_SEQUENTIAL`：顺序的，会自动在节点名后面添加一个自增计数，格式为%010d
`EPHEMERAL`：临时节点，生命周期依赖于client session，对应session close/expire后其znode也会消失，临时节点不能有子节点
`EPHEMERAL_SEQUENTIAL`
该方法可能触发如下异常：

`NodeExistsError`：当要创建的节点已经存在时
`NoNodeError`：当makepath为False且祖先节点不存在时
`NoChildrenForEphemeralsError`：父节点为临时节点，在一个临时节点下面创建子节点会报该异常
`ZookeeperError`：节点值太大，zk默认节点值限制为1M
`ZookeeperError`：服务器返回一个非0状态码'''

# zk.create("/zk1",value=b"zktest",acl=None,ephemeral=False, sequence=False, makepath=False)

# value=zk.get("/zk1")
# nodes=zk.get_children("/zk1")
# print(value,nodes)
#
# zk.set('/zk1',b'nihao')
# value=zk.get("/zk1")
# print(value)
#
# res=zk.get_children('/')
# print(res)

# print(zk.command(cmd=b'conf'))
# print(zk.hosts)
# print(zk.client_id)
# print(zk.chroot)



# listener  监听事件机制：监听连接的状态 三个状态﻿ CONNECTE   ﻿SUSPENDED  LOST，执行连接监控。
# def do_something():
#     pass
# def  my_listener(state):
#     if state==KazooState.LOST:
#         do_something()
#         print('ZK LOST')
#     elif state==KazooState.CONNECTED:
#         do_something()
#         print('ZK CONNECTED')
#     else:
#         do_something()
#         print('ZK SUSPEND')
#
#
#
# zk.add_listener(my_listener)
# zk.start()
# print(zk.state_listeners)
# zk.stop()

'''﻿
watcher 机制，有两种 watch 机制，
`dataWatch`：针对节点的创建、修改、删除，都会触发该watch（同时创建、删除节点也会触发该节点的父节点的childrenWatch）
`childrenWatch`：针对子节点的创建、删除，才会触发该watch  
send_event: 若需要zk返回event，那么需要将send_event设为True,才可以在watch函数传入event位置参数,
'''
# 1. 最简单的是使用装饰器方式来实现,
# zk=KazooClient(hosts="47.110.87.5:2181")
# zk.start(timeout=5)
# @DataWatch(client=zk,path='/xj')  # 这个 event不用传入,下面自动就能获取到的。
# def changed(data, stat, event):
#     print("--------------DataWatch---------------")
#     print( "data:", data)
#     print( "stat:", stat)
#     if event:
#         print( "event:", event)
#
# zk.create("/xj", b"value1")
# time.sleep(2)
# zk.set("/xj", b"value2")
# time.sleep(2)
# zk.delete("/xj")
# time.sleep(2)


# zk.create('/xj')
# @ChildrenWatch(client=zk,path='/xj',send_event=True)  # 这个位置要传这个 event 下面才能拿到的，否则拿不到，和 datawatch 不一样，
# def childWatch(children,event):
#         print('---------------ChildWatch----------------')
#         print( "children:",children)
#         print('catch event:',event)
#
# zk.create("/xj/a")
# time.sleep(2)
# zk.create("/xj/b")
# time.sleep(2)
# zk.delete("/xj/a")
# time.sleep(2)


'''
装饰器还有一种方式：这种方式是在 watch中写zk 的地址
'''
# datawatch：

# zk=KazooClient(hosts="47.110.87.5:2181")
# zk.start()
#
# def call():
#     print("开始先执行这个函数")
#
# @DataWatch(client=zk,path='/xj',func=call()) # 这个回调是指，执行 watch 函数之前先执行的函数
# def changed(data, stat, event):
#     print("--------------DataWatch---------------")
#     print( "data:", data)
#     print( "stat:", stat)
#     print( "event:", event)
#
# print("开始执行")
# zk.create("/xj", b"value1")
# time.sleep(2)
# zk.set("/xj", b"value2")
# time.sleep(2)
# zk.delete("/xj")
# time.sleep(2)


# ChildrenWatch监控子节点的变化，子节点的增加删除，操作。来执行
# zk=KazooClient(hosts="47.110.87.5:2181")
# zk.start()
#
# def call():
#     print("开始先执行这个函数")
#
# @ChildrenWatch(client=zk,path='/config',func=call())
# def watch_child(children):
#     print("开始执行 watch 函数")
#     global  children_node
#     children_node=children
#
#     print(children_node)
#
# time.sleep(1)
# # zk.create('/config/a')
# time.sleep(2)
#
# zk.create('/config/a')
# time.sleep(2)


# children  watcher 和 threading 的 event 的结合使用
# zk=KazooClient(hosts="47.110.87.5:2181")
# zk.start()
#
# def get_path(path,event):
#
#     print('%s %s 开始执行' %(threading.current_thread().name,threading.current_thread().ident))
#     while not event.isSet():
#         print("%s  还没有创建节点" %threading.current_thread().name)
#         time.sleep(2)
#
#     event.wait()
#
#     while event.isSet():
#         print(" %s  节点已经创建了，开始删除" %threading.current_thread().name)
#
#         sleep_time=random.uniform(1,10)
#         print("sleep_time is  %s " %sleep_time)
#         time.sleep(sleep_time)
#
#         if zk.exists(path=path):
#             zk.delete(path=path)
#             event.clear()
#             print(" %s path 已经删除了"  %threading.current_thread().name)
#         else:
#             print("%s 节点已经被删除了啊啊啊啊啊啊。。。" %threading.current_thread().name)
#

# if __name__ == '__main__':
#     path='/xj'
#     print("主线程开始操作")
#     res_l=[]
#     event = threading.Event()
#
#     # 多进程的方式，这个肯定是不合适的，因为 join 的问题，一旦 join，主进程就会停止执行，等子进程执行完毕后才会继续执行，
#     # p=multiprocessing.Pool(2)
#     # for i in range(0,2):
#     #     res=p.apply_async(get_path,args=(path,event))
#     #     res_l.append(res)
#     # p.close()
#     # p.join()
#     # for res in res_l:
#     #     print(res.get())
#
#     for i in range(0,2):
#         p=threading.Thread(target=get_path,args=(path,event))
#         p.start()
#
#     time.sleep(6)
#     print("开始创建节点")
#     zk.create(path=path)
#     event.set()
#     print('主线程执行完成了')
#     print(event.isSet())
#



#这个例子不是用装饰器实现，使用单独创建的，其实也可以进行赋值，如childwatcher=ChildrenWatch(client=self._zk,path=zkpath,func=self._NodeChange)
class ZKWwatcTest():
    def __init__(self, host, port, timeout=10):
        self._nodename = ''
        self._host = host
        self._port = port
        self._timeout = timeout
        self._zk = KazooClient(hosts=self._host + ':' + self._port, timeout=self._timeout)
        self._zk.start()
        self._lastNodeList = []


    def start(self,zkpath):
        print('start')

        if  self._zk.exists(zkpath):
            self._lastNodeList = self._zk.get_children(zkpath)
        else:
            print("节点不存在")
            sys.exit(1)
        try:
            ChildrenWatch(client=self._zk,path=zkpath,func=self._NodeChange,send_event=True)
            DataWatch(client=self._zk,path=zkpath,func=self._DataChange)
            while True:
                time.sleep(60)   #
                print("ok")
        except Exception as e:
            print(e.message)

    def _NodeChange(self, children,event):  # 这两个是默认传进来的、childrenwatcher 自动有这个参数
        if len(children) > len(self._lastNodeList):
            for node in children:
                if node not in self._lastNodeList:
                    print(event)
                    print("新增加的节点为：", str(node))
                    self._lastNodeList = children
        else:
            for node in self._lastNodeList:
                if node not in children:
                    print(event)
                    print("删除的节点为：", str(node))
                    self._lastNodeList = children

    def _DataChange(self, data, stat):
        """
        处理节点的数据变化
        :param data:
        :param stat:
        :return:
        """
        print( "数据发生变化")
        print( "数据为：", data)
        # print("数据长度：", stat.dataLength)
        print("数据版本号version：", stat.version)
        print("cversion：", stat.cversion)
        print("子节点数量：", stat.numChildren)

def main():
    try:
        zkwt = ZKWwatcTest(host="47.110.87.5", port="2181")
        zkwt.start('/zktest')
    except Exception as err:
        print(err.message)


if __name__ == "__main__":
    try:

        print('kaishi')
        main()
    finally:
        sys.exit()




# def normal_test(zk_path,host,port,node_list):
#     zk=KazooClient(hosts=host+':'+port,timeout=10)
#     zk.start()
#
#     if not zk.exists(zk_path):
#         zk.create(path=zk_path,value=b'bar')
#
#     child_node_list=zk.get_children(zk_path,watch=None,include_data=False)
#
#     if not child_node_list:
#         for sub_node in  node_list:
#             zk.create(zk_path+'/'+sub_node,b'aaa')
#     else:
#         print('subnode list:{}'.format(child_node_list))
#
#     data,stat=zk.get(zk_path)
#     print('current node data:{}'.format(data))
#     print('data version:{}'.format(stat.version))
#     print('data length:{}'.format(stat.data_length))
#     print('children node numbers:{}'.format(stat.numChildren))
#
#
#
#     stat_new=zk.set(zk_path,value=b'foo')
#     print('node {0} is updated:{1}'.format(zk_path, stat_new))
#
#     zk.delete(zk_path, recursive=True)
#     try:
#         last = zk.get_children(zk_path)
#         print('children nodes :{}'.format(last))
#     except exceptions.NoNodeError:
#         print('no children nodes')
#
#     zk.stop()
#     zk.close()
#
# if __name__ == '__main__':
#     normal_test(zk_path='/app_conf', host='47.110.87.5', port='2181', node_list=['foo1', 'foo2', 'foo3'])



# 事务处理：
# zk.start()
# transacton=zk.transaction()
# transacton.create('/zk2',b'ok')
# transacton.set_data('/zk2',b'okokok')
# transacton.commit()
#
#
# res=zk.get('/zk2')
# print(res)



