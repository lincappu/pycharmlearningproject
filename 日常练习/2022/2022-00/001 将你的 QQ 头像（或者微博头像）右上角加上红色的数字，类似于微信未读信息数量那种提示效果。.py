# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from PIL  import  Image

# Image模块：

im=Image.open('./21.jpg','r')  # 这个 mode 必须是 r，文件对象必须已二进制模式打开
print(im)
print(im.mode)
print(im.format)
print(im.size) #图片信息
print(im.info)




box = (100, 100, 300, 300)
region = im.crop(box)                   ##将im表示的图片对象拷贝到region中，大小为box
region.show()


# im.save('211.jpg')






