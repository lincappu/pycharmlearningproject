# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from PIL import Image,ImageFilter,ImageDraw
import os,sys

im1=Image.open('1.png')
im2=Image.open('2.png')

# # print(image.format,image.size,image.mode)
# # image.show()


# new_im=im.convert('')
'''
modes	描述
1	1位像素，黑和白，存成8位的像素
L	8位像素，黑白
P	8位像素，使用调色板映射到任何其他模式
RGB	3× 8位像素，真彩
RGBA	4×8位像素，真彩+透明通道
CMYK	4×8位像素，颜色隔离
YCbCr	3×8位像素，彩色视频格式
I	32位整型像素
F	32位浮点型像素'''
#new_im.show()


# new_im=Image.new('RGB',(128,128),"#FF0000")
# new_im.show()

# 复合操作：
# Image.blend(im1,im2,0.7).show()  # 后面的是透明度
# Image.alpha_composite(im2,im1).show()  # 直接覆盖



# 模糊操作
# image=image.filter(ImageFilter.BLUR)
# image.show()

# 将是哪个通道分离的图像
# r,g,b=image.split()
# r.show()
# g.show()
# b.show()

# 滤镜操作
# image=image.filter(ImageFilter.DETAIL)
# image.show()

# 逆时针旋转
# image=image.rotate(90)
# image.show()

#将文件转为 jpeg
# f,e=os.path.splitext('1267.jepg')
# print(f,e)
# print(f+'.jpg')

# 创建缩略图
# box=(100,100,400,400)
# region=image.crop(box)


# filter  细节处理
# out=im1.filter(ImageFilter.DETAIL)
# out.show()


# draw类：绘图类

im1=Image.open('1.png')
draw=ImageDraw.Draw(im1)
draw.line((0, 100, im1.size[0], 0), fill=255)
im1.save('211.png')
im1.close()









