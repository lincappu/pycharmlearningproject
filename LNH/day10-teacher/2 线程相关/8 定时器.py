# from threading import Timer
#
#
# def hello(id):
#     print("hello, world",id)
#
# t = Timer(1, hello,args=(30,))
# t.start()  # after 1 seconds, "hello, world" will be printed


from threading import Timer
import random,time


class Code():
    def  __init__(self):
        self.make_cache()

    def make_cache(self,interval=5):
        self.cache=self.make_code()
        print(self.cache)

        s