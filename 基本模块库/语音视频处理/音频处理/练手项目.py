# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import json
import time
import wave

import pyaudio
import requests
import speech_recognition as sr
from aip import AipSpeech

# 实现的功能：
# pyaudio（录音）--> 百度语音（Speech-to-Text）--> 图灵机器人（语义分析及应答）--> 百度语音（Text-to-Speech）--> PyAudio（音频播放）

# 百度 STT
APP_ID = '24589844'
API_KEY = 'ewlw9wBl1Mf1j506zGLCOm8D'
SECRET_KEY = 'LYXqrO58CI9DNA84AAoctqyiPKmrhBGb'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# Turing API  图形机器人
TURING_KEY = '0d545503ff654db2b5a0fb60890ebaee'
TURING_URL = 'http://openapi.tuling123.com/openapi/api/v2'
HEADERS = {'Content-Type': 'application/json;charset=UTF-8'}


# use  speechRecongition to record

def record(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something：")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())


# 用百度 STT将语音转成成文本
def listen():
    with open("recording.wav", 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })

    if result['err_no'] != 0:
        print('百度转义失败 {}\n'.format(result))
        return 'break'

    else:
        result_text = result['result'][0]
        return result_text


# 使用图灵聊天机器人
def robot(text=''):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": ""
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

    data['perception']['inputText']['text'] = text
    response = requests.request(method='post', url=TURING_URL, json=data, headers=HEADERS)
    response_dict = json.loads(response.text)

    result = response_dict["results"][0]["values"]["text"]
    print("the AI said: " + result)
    print(type(result))
    return result


def speak(text=''):
    result = client.asr(text.encode('utf-8'), 'zh', 1, {
        'spd': 2,
        'vol': 10,
        'per': 0,
    })

    if not isinstance(result, dict):
        with open('output.wav', 'wb') as f:
            f.write(result)


# play audio wav file
def play():
    wf = wave.open('output.wav', 'rb')
    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()
    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()
    p.terminate()


while True:
    record()
    request = listen()
    if request == 'break':
        continue
    response = robot(request)
    print(response)
    speak(response)
    play()
