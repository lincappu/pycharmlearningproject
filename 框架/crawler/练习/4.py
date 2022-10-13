# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


"""
    爬取hao123网站的网络游戏排行榜
    http://wy.hao123.com/top
"""
import requests
from lxml import etree


def load_context():
    """ 获取http://wy.hao123.com/top网页内容 """

    # 定义HTTP请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
    # url地址
    url = "http://wy.hao123.com/top"

    # 使用requests的get方法获取网页内容
    rsp_ctx = requests.get(url, headers=headers)
    # 返回网页内容
    return rsp_ctx.text


def parse_context(c):
    html = etree.HTML(c,etree.HTMLParser())

    divs=html.xpath("//div[@class='list1 margin-right']|//div[@class='list1 ']")


    with open('hao123.csv', 'w', encoding='utf-8') as f:
        for div in divs:
            title = div.xpath('./div[@class="tlt"]')[0].text

            print(title)
            f.write(title+'\n')

            games=div.xpath('.//li')
            print(games)
            for idx, game in enumerate(games):
                game_name=game.xpath('./p/a')[0].text
                game_type=game.xpath('./em')[0].text

                f.write('\t'+str(idx+1)+ "," + game_name + "," + game_type + '\n')
    print("ok")









res=load_context()
parse_context(res)

