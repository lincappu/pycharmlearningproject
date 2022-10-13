# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  requests
from lxml import etree
import json
import  time




#
# headers={'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#
# response=requests.get(url='http://tieba.baidu.com/f?kw=miss',headers=headers)
# content=response.content.decode('utf-8')
# print(type(content))
# print(content)



# with open('tieba','r') as tieba_f:
#     content=tieba_f.read()
#
#
# html=etree.HTML(content,etree.HTMLParser())
# last_page=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a')
# print(last_page)
#
#
#
# page_urls=[]
#
# i=1
# while(i*50<all_num):
#     page_url=('http://tieba.baidu.com/f?kw=miss&ie=utf-8&pn='+str((i*50))).strip('"')
#     page_urls.append(page_url)
#     i+=1
#
#
# with open('tiebapage.json','w',encoding='utf-8') as f:
#     json.dump(page_urls,f)



url=[]
name=[]


with open('tiebapage.json', 'r', encoding='utf-8') as f:
    page_urls=json.load(f)

for  page in page_urls:
    headers={'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    response=requests.get(url=page,headers=headers)
    content=response.content.decode('utf-8')
    content=content.replace('<!--','').replace('-->','')

    html=etree.HTML(content,etree.HTMLParser())
    href=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    name=html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')

    for h in href:
        # url.append(h)
        print(h)
    # for n in name:
    #     name.append(n)
    #     print(name)
    # print(url)
    # print(name)










