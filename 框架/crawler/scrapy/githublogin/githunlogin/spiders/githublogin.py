# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


# import scrapy
# import time
# from .password import password
#
#
# class GithubLoginSpider(scrapy.Spider):
#     name = 'github_login'
#     # allowed_domains = ['dddd']
#     start_urls = ['https://github.com/session']
#
#     def parse(self, response):
#         formdata={
#             'authenticity_token':'6tgk+7akA02mQR+Gfi2pOppfYijKHNybxYN+TTu6JkOGKrKWXbf+n6tmV3lYwzZSAGTyTZMtrUv8R5UvozHaHQ==',
#             'commit': 'Sign in',
#             'ga_id': '1895867995.1493545217',
#             'login': 'lincappu@163.com ',
#             'password': 'Lin.62498',
#             'required_field_c6b2:': '',
#             'timestamp': str(int(time.time()) * 1000),
#             'timestamp_secret': 'a1323d73b8c81ec971bca409b34e5644313ffa4e3f6ad515f0074d547e81eb78',
#             'utf8': 'v',
#             'webauthn-iuvpaa-support': 'unsupported',
#             'webauthn-support': 'supported',
#         }
#
#         cook="_ga=GA1.2.1895867995.1493545217; _device_id=5dc25f34cce84837b019fa11ed9db231; _octo=GH1.1.1486440725.1557055279; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; logged_in=no; _gh_sess=%2FRbp9l%2B5VGUaeMnYiWlF7XmyRIzXlVXxW0F8wCR890JdSRBe2U0gTXR8EIsJwBN%2FbPM%2F%2BtQiSsGx2hmHcVV%2F%2FbHhz3bu6n%2FV2iL0xJa%2BK7LiLunQfWnpltAQC%2FManfljsobihHaSifCJQqDZ%2ByoIuwDLAzZFPUglHG4Z9c3Z8nZ%2Fzt6hH6w6FT%2F0EHMD5f09eW4C9rH4mI4BBEqLlDRXiwBHS7t0Ml9RFbg1McFUFIZQyuQarpmdM7zqT8A%2B3pJwrKy%2F0TC3RcSFnAPbCNo%2FuA%3D%3D--5HzVz3uSkKCZVjMQ--7A1uP6YNsoNtWSOXL5piKQ%3D%3D"
#
#         yield

import  re
import requests
import  time


url = 'https://github.com/login'
login_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

login_response = requests.get(url, headers=login_headers)



authenticity_token = re.findall('<input type="hidden" data-csrf="true" name="authenticity_token" value="(.*?)" />',
                                login_response.text,
                                re.S)[0]

timestamp_secret = re.findall('<input class="form-control" type="hidden" name="timestamp_secret" value="(.*?)" />',
                              login_response.text,
                              re.S)[0]

formdata={
    'authenticity_token':authenticity_token,
    'commit': 'Sign in',
    'ga_id': '1895867995.1493545217',
    'login': 'lincappu@163.com',
    'password': 'Lin.62498',
    'required_field_c6b2:': '',
    'timestamp': str(int(time.time()) * 1000),
    'timestamp_secret': timestamp_secret,
    'utf8': '✓',
    'webauthn-iuvpaa-support': 'unsupported',
    'webauthn-support': 'supported',
}




cook="_ga=GA1.2.1895867995.1493545217; _device_id=5dc25f34cce84837b019fa11ed9db231; _octo=GH1.1.1486440725.1557055279; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; logged_in=no; _gh_sess=%2FRbp9l%2B5VGUaeMnYiWlF7XmyRIzXlVXxW0F8wCR890JdSRBe2U0gTXR8EIsJwBN%2FbPM%2F%2BtQiSsGx2hmHcVV%2F%2FbHhz3bu6n%2FV2iL0xJa%2BK7LiLunQfWnpltAQC%2FManfljsobihHaSifCJQqDZ%2ByoIuwDLAzZFPUglHG4Z9c3Z8nZ%2Fzt6hH6w6FT%2F0EHMD5f09eW4C9rH4mI4BBEqLlDRXiwBHS7t0Ml9RFbg1McFUFIZQyuQarpmdM7zqT8A%2B3pJwrKy%2F0TC3RcSFnAPbCNo%2FuA%3D%3D--5HzVz3uSkKCZVjMQ--7A1uP6YNsoNtWSOXL5piKQ%3D%3D"

session_url = 'https://github.com/session'
session_response = requests.post(
    session_url,
    data=formdata,
    cookies=login_response.cookies
)


print(session_response.status_code)
print(session_response.cookies)


emails_response = requests.get('https://github.com/settings.py/emails', cookies=session_response.cookies)  # 登录成功后，以后的访问都要带上cookies。
print('lincappu@163.com' in emails_response.text)