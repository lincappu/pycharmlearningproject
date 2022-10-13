'''
展示进度条的功能：
1、普通进度条
'''

import  sys
import os
import time
import tqdm
import progressbar



# 终端输出刷新的问题,
# for i in range(10):
#     print(i,end=' ')   #  终端有换行就会自动刷新，所以要去掉换行。
#     sys.stdout.flush()  # 只有mac 才需要，window不管有没有都会刷新
#     time.sleep(1)


# 1、普通进度条：其实就是计算出一个进度，然后按百分比展示，同时用图形展示
def process_bar():
    for i in range(0,101):
        print('\r',end='')
        print('Downloading progress: {}%'.format(i),"#"*(i//2),end='')
        sys.stdout.flush()
        time.sleep(0.1)

# 2、带时间戳的进度条
def process_bar_time():
    scale=50
    print('开始执行'.center(scale//2,'-'))
    start_time=time.perf_counter()
    for i in range(scale+1):
        a="*"*i
        b="."*(scale-i)
        c=(i/scale) * 100
        dur=time.perf_counter()-start_time
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
        time.sleep(0.1)
    print('\n')
    print('执行结束'.center(scale // 2, '-'))

# 3、TQDM进度条，专门生成进度条的工具包，可以切换进度条的风格。
def tqdm_bar():
    for i in tqdm.tqdm(range(1,101)):
        time.sleep(0.5)
    time.sleep(0.5)


# 4、process进度条，阶段展示的进度条
def progress_bar():
    def test():
        time.sleep(0.1)
    pbar=progressbar.ProgressBar()
    for i in pbar(range(100)):
        test()

def progress_bar2(): # 定义步长
    total=100
    def test():
        time.sleep(0.1)
    pbar=progressbar.ProgressBar().start()
    for i in pbar(range(100)):
        pbar.update((int(i/(total-1)) * 100))
        test()
    pbar.finish()


def progress_bar3(): # 自定义步长  自定义显示格式
    total=100
    def test():
        time.sleep(0.1)
    widgets=['Process: ',progressbar.Percentage(),' ',progressbar.Bar(),' ', progressbar.Timer(),' ', progressbar.ETA(), ' ',progressbar.FileTransferSpeed()]
    pbar=progressbar.ProgressBar(widgets=widgets,maxval=total).start()
    for i in range(total):
        pbar.update( i+1)
        test()
    pbar.finish()
'''
widgets可选参数含义：
'Progress: ' ：设置进度条前显示的文字
Percentage() ：显示百分比
Bar('#') ： 设置进度条形状
ETA() ： 显示预计剩余时间
Timer() ：显示已用时间
'''


# 5、 alive-progress  会动的进度条
from  alive_progress import alive_bar,alive_it
'''
def alive_bar(total=None, *, calibrate=None, **options)
total：总任务数量     实际数目会有比total，大 、小，相等，为0 的情况。显示的会有差异。
calibrate：动画的帧率，越小帧率越高，一般用默认的1e6就可以

**options是进度条的可选项，里面选项的写法和函数参数写法一样。说明如下：
① 外观类
title(string)：进度条开头的标题
length(int)：渲染进度条的长度
spinner (Union[None, str, object])：进度条旁边等待动画的渲染主题样式。类型包括主题名称(spinner)字符串，或自定义主题。（主题样式将在之后演示）
bar (Union[None, str, object])：进度条主题样式。包括主题名称(bar)字符串，或自定义主题。（主题样式将在之后演示）
theme (str)：主题样式，一个同时设置bar和spinner的主题。（主题样式将在之后演示）
title_length (int)：强制标题长度，超过则忽略多余部分并显示一个省略号
spinner_length (int)：强制等待动画的长度，建议默认
② 控制类
ctrl_c (bool)：在终端使用Ctrl+C终止程序后，是否在结尾输出终止错误
disable (bool)：是否禁用进度条
enrich_print (bool)：在进度内使用print时，若为是则实时输出，若为否则在结束后一次性输出
force_tty (Optional[int|bool])：是否在不能渲染和抓取log的终端中强制渲染，建议默认自动识别
receipt (bool)：是否在进度结束后保留进度条的结果
receipt_text (bool)：在进度结束后是否继续保留进度条的描述信息
refresh_secs (int)：强制规定刷新的周期，建议使用默认就好

③ 文本类
dual_line (bool)：是否将进度条描述信息显示在第二行
monitor (bool|str)：设置进度监视器的文本样式（默认152/200 [76%]）。设置的书写格式：
{count}/{total} [{percent}%]
elapsed (bool|str)：设置计时器的文本样式（默认in 12s）。设置的书写格式：in {elapsed}s
stats (bool|str)：设置进度速度的文本样式（(123.4/s, eta: 12s)）。设置的书写格式：
{rate}, eta: {eta}
monitor_end (bool|str)、elapsed_end (bool|str)、stats_end (bool|str)：在进度条结束时显示这些布局的样式，书写方式与上述相同


def alive_it(it, total=None, *, finalize=None, calibrate=None, **options)
it：迭代变量
finalize：当进度结束时执行的函数
其他的和alive_bar一致

'''

item=range(100)
def alive_progress_bar():
    with  alive_bar(100,force_tty=True) as bar:
        for i in item:
            time.sleep(0.1)
            # bar() # 步长默认是1
            if i== 10 or i==250 or i==500:
                print('FOUND')  # 可以在动画显示中间打出日志
            bar(1) # 步长一次增加 5，这个要计算好total要和item的次数相等。



# # alive_it:
# # 1. 直接以迭代器的的for循环方式写出
# for i in alive_it(range(10), title='test'):
#     # code
#     pass
# # 2. 以变量的循环方式写出,若想使用在进度条内的说明，需要在类内的属性bar.text进行设置
# bar = alive_it(range(100), receipt=False)
# for i in bar:
#     bar.text = f' ->Wow, it works!'
#     time.sleep(0.02)



#  6、 PySimpleGUI 可视化进度条,  这个可能pycharm无法展示
import  PySimpleGUI as sg

mylist = [1,2,3,4,5,6,7,8]
for i ,item in enumerate(mylist):
    sg.one_line_progress_meter("this is my progress",i+1,len(mylist),'-key-')
    time.sleep(1)



# 7、qt5这种可视化的， 可以实现在页面的进度条功能。



if __name__ == '__main__':
    pass

    # process_bar()
    # process_bar_time()
    # tqdm_bar()
    # progress_bar()
    # progress_bar2()
    # progress_bar3()
    # alive_progress_bar()


