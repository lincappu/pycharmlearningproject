# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from PIL import Image, ImageDraw, ImageFont, ImageColor


def add_num(img):
    draw=ImageDraw.Draw(img)

    myfont=ImageFont.truetype("./OpenSans-Regular.ttf",size=40)
    fillcolor=ImageColor.colormap.get("red")
    width,heigth=img.size
    draw.text((width-30,0),"1",font=myfont,fill=fillcolor)

    img.save("result.jpg","jpeg")

    return 0


if __name__ == '__main__':
    image=Image.open('1267.jpeg')
    add_num(image)

