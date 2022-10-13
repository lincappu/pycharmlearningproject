# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import requests
import json
import jq

# Turing API  图形机器人
TURING_KEY = '0d545503ff654db2b5a0fb60890ebaee'
TURING_URL = 'http://openapi.tuling123.com/openapi/api/v2'
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}

data = {
	"reqType": 0,
	"perception": {
		"inputText": {
			"text": "上海今天的天气怎么样"
		},
		"selfInfo": {
			"location": {
				"city": "上海",
				"province": "上海",
				"street": "五角场"
			}
		}
	},
	"userInfo": {
		"apiKey": TURING_KEY,
		"userId": '726027'
	}
}

data = json.dumps(data).encode('utf-8')
res = requests.request(method='POST', url=TURING_URL, data=data, headers=HEADERS)

# 另外一种方式就是直接在指定参数的时候指定 json 的 data，这样他会自动将数据转化为 json格式，
# 并用编辑器默认的编码格式进行编码
# res=requests.request(method='POST',url=TURING_URL,json=data,headers=HEADERS)


print(type(res.text))
response_dict = json.loads(res.text)
print(type(response_dict))
print(response_dict)
print(response_dict['results'][0]['values']['text'])

#  判断返回的结果是否正确
# if response_dict['results']:
