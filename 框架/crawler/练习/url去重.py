# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import requests,re
import time
from collections import Counter
count = 3
recount = 0
allcount = 1
r = re.compile(r'href=[\'"]?(http[^\'">]+)')
seed = 'http://httpbin.org/'
queue = [seed]
used = set()   # 设置一个集合，保存已经抓取过的URL
storage = {}

while len(queue) > 0 and count > 0 :
    try:
        url = queue.pop(0)
        html = requests.get(url).text
        storage[url] = html  #将已经抓取过的URL存入used集合中
        used.add(url)
        new_urls = r.findall(html)   # 将新发行未抓取的URL添加到queue中
        for new_url in new_urls:
            allcount += 1
            if new_url not in used and new_url not in queue:
                queue.append(new_url)
            else:
                print("重复："+url)
                recount += 1
        count -= 1
    except Exception as e :
        print(url)
        print(e)

print("重复网站："+str(recount))
print("总网站："+str(allcount))
url_count = Counter(queue)
for url,count in url_count.most_common(10):
    print(url,count)
