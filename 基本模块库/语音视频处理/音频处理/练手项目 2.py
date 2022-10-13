# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

'''
通过原因识别将原因转成文字，然后将文字识别为鼠标的操作
语音识别和鼠标键盘的操作

流程：pyaudio-->百度语音-->> pyMouse将文字转换位操作
或者是：
流程：pyaudio-->百度语音-->> pyKeyboard 语音输入文字
'''


import   pyaudio
import wave
import tqdm
import speech_recognition as sr
from aip import AipSpeech
from  pymouse import PyMouse
from pymouse import  PyMouseEvent
from  pykeyboard import PyKeyboard
import time你

# 百度 STT
APP_ID = '24589844'
API_KEY = 'ewlw9wBl1Mf1j506zGLCOm8D'
SECRET_KEY = 'LYXqrO58CI9DNA84AAoctqyiPKmrhBGb'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# Turing API  图形机器人
TURING_KEY = '0d545503ff654db2b5a0fb60890ebaee'
TURING_URL = 'http://openapi.tuling123.com/openapi/api/v2'
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}


def record_audio(wave_out_path,record_second):
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000

    p=pyaudio.PyAudio()
    stream=p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

    wf=wave.open(wave_out_path,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    print('**** start recording')
    for i in  tqdm(range(0,int(RATE/CHUNK*record_second))):
        data=stream.read(CHUNK)
        wf.writeframes(data)
    print('***Done')


    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()



def aip_get_asrresult():

    with open("recording.wav", 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })

    if result['err_msg'] != 'success.':
        print('百度转义失败 {}\n'.format(result))
        return ''
    else:
        result_text = result['result'][0]
        return result_text


def mouse_control(dir_tr):
    MOVE_DX=5 # 每次移动行数
    m=PyMouse()
    horizontal = 0
    vertical = 0

    if dir_tr.find("上") != -1: # 向上移动
        vertical = MOVE_DX
        #print("vertical={0}, 向上".format(vertical))
    elif dir_tr.find("下") != -1: # 向下移动
        vertical = 0 - MOVE_DX
        #print("vertical={0}, 向下".format(vertical))
    elif dir_tr.find("左") != -1: # 向左移动
        horizontal = 0 - MOVE_DX
        #print("horizontal={0}, 向左".format(horizontal))
    elif dir_tr.find("右") != -1: # 向右移动
        horizontal = MOVE_DX

    m.scroll(vertical, horizontal)


def keyboard(text):
    k=PyKeyboard()
    k.tap_key(text)




if __name__ == '__main__':
    while True:
        # 请说出语音指令，例如["向上", "向下", "向左", "向右"]
        print("\n\n==================================================")
        print("Please tell me the command(limit within 3 seconds):")
        # print("Please tell me what you want to identify(limit within 10 seconds):")
        record_audio('output.wav', 3)  # 录制语音指令
        print("Identify On Network...")
        asr_result = aip_get_asrresult()  # 识别语音指令
        if len(asr_result) != 0:  # 语音识别结果不为空，识别结果为一个list
            print("Identify Result:", asr_result)
            print("Start Control...")
            mouse_control(asr_result)  # 根据识别结果控制页面滚动
            print("Control End...")
            if asr_result.find("退出") != -1:  # 如果是"退出"指令则结束程序
                break;
            time.sleep(1) # 延时1秒


























