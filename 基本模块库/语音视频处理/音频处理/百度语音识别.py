# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

'''
利用百度的语音识别功能，将语音转成文字
'''


from aip import AipSpeech
# 定义常量
APP_ID = '24589844'
API_KEY = 'ewlw9wBl1Mf1j506zGLCOm8D'
SECRET_KEY = 'LYXqrO58CI9DNA84AAoctqyiPKmrhBGb'


client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_content(filepath):
    with open(filepath,'rb') as fp:
        return fp.read()

res=client.asr(speech=get_content('16k16bit.wav'),
               format='wav',
               rate=16000)

# print(res['result'][0])

# 先进行检查转义结果
# while res['err_no'] !=0:
#     print('转义错误 %s'.format(res['err_msg']))
    # 循环录

# 或者是
# if res['err_msg'] == 'success.':
#     return res
# else:
#     print('')



# if 'result' in res:
#     text=res['result'][0][:-1]



# 语音合成： 将文字转成语音

result=client.synthesis('你好百度，这是我的测试文档，请你完整读出来。','zh',1,{'vol':5,
                                       'spd':2,
                                       'per':0})
if not isinstance(result,dict):
    with open('output2.wav','wb') as f:
        f.write(result)



