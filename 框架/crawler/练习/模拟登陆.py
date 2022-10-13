# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import  requests


header = {
    "referer": "https://www.itjuzi.com/login",
    "user-agent": "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
}

# data = {
#     "account": "13161066225",
#     "password": "lin.111555",
#     "type": "pswd"
# }

url ='https://www.itjuzi.com/user/login'

session = requests.Session()

session.post(url=url,headers=header,data=data)

response=session.get('https://www.itjuzi.com/user-center/note')
print(response.status_code)
print(response.content.decode('utf-8'))