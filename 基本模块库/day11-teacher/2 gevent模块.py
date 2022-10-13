#pip3 install gevent
from gevent import monkey;monkey.patch_all() #写到文件的首部
import gevent
import time
from threading import current_thread

def eat(name):
    print('%s eat 1 %s' %(name,current_thread().getName()))
    time.sleep(2)
    # gevent.sleep(5)
    print('%s eat 2 %s' %(name,current_thread().getName()))
    return 10

def play(name):
    print('%s play 1 %s' %(name,current_thread().getName()))

    time.sleep(3)
    # gevent.sleep(7)
    print('%s play 2 %s' %(name,current_thread().getName()))

    return 20

start=time.time()
g1=gevent.spawn(eat,name='egon')
g2=gevent.spawn(play,'alex')

# print(g1,g2)

# g1.join()
# g2.join()
gevent.joinall([g1,g2])
# print(g1.value)
# print(g2.value)
print(time.time()-start)