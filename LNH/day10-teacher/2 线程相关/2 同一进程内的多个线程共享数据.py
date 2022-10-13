from threading import Thread

n=100

def task():
    global n
    n=0

if __name__ == '__main__':
    t=Thread(target=task)
    t.start()
    t.join()
    print('主',n)