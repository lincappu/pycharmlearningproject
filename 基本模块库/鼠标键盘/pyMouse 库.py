# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from  pymouse import PyMouse
from  pykeyboard import PyKeyboard



# 实例化一个鼠标键盘对象
m=PyMouse()
k=PyKeyboard()


# 屏幕中央，   鼠标坐标起始点是左下方，（0，0）
x_dim,y_dim=m.screen_size()
x,y=int(x_dim/2),int(y_dim/2)  # 必须是整数

# print(x_dim,y_dim)
# print(x,y)

# 移动到屏幕中央
# m.move(x,y)

# 点击屏幕中央,某个位置
# m.click(x,y)

# 返回鼠标的位置
# res= m.position()
# print(res)

# 中键垂直滚动 10 个单位
# m.scroll(1,0) # 默认是垂直，水平：向上和右


# 拖拽鼠标到当前位置
# m.drag(900,500)


# 按下 H 建,释放 H 健
# k.press_key('H')
# k.release_key('H')


# tap_key 来接受按下和释放,只是按下次数和间隔时间秒,特殊按键
# k.tap_key('H')
# k.tap_key('1',n=2,interval=2)
# k.tap_key(k.tab_key)
# k.tap_key(k.alt_key)
# k.tap_key(k.numpad_keys[5],n=3)




#  小例子：随机点击屏幕固定位置
import  numpy as np
import time
import random



# def auto_click(position=0,blank=10):
#     """
#     :param position: 鼠标移动并点击的位置，tuple(x,y)
#     :param blank:鼠标下次移动最少的时间间隔，int
#     """
#
#     time_random=random.random()*10
#     time.sleep(time_random)
#
#     mouse = PyMouse()
#     x_ = position[0]
#     y_ = position[1]
#     mouse.click(x_, y_,button=1)  # 移动并且在(x,y)位置左击1次
#     time.sleep(4)                 # 设置两次点击的间隔为4秒
#     mouse.click(x_, y_, button=1)  # 移动并且在(x,y)位置左击1次
#     time.sleep(2)
#     return mouse
#
#
#
# if __name__ == '__main__':
#     position_list = [(146, 71), (199, 71), (250, 71), (303, 71),
#                      (374, 71), (1564, 1020), (1714, 1020), (1830, 1020)]
#     # 两次鼠标移动最小的时间
#     time_blank = 3
#
#     print('三国杀自动点击脚本开始执行，你有30s的时间调整至三国杀的页面，本次点击的坐标如下：\n{}\n'.format(position_list))
#     for i in range(30,0,-1):
#         str_ = '脚本开始倒计时：第{}秒'.format(i)
#         print(str_)
#         time.sleep(1)
#     print('\n自动点击脚本开始>>>>>\n')
#
#     while True:
#         np.random.shuffle(position_list)
#
#         for i in position_list:
#             mouse=auto_click(i,blank=time_blank)
#
#             mouse.click(170, 1065, button=1)





















