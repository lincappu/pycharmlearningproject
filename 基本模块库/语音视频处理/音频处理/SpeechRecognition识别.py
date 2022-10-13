# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import  speech_recognition as sr



# 播放录音文件
def  play_file():
    r=sr.Recognizer()

    test=sr.AudioFile('16k16bit.wav')
    test2=sr.AudioFile('harvard.wav')
    test3=sr.AudioFile('jack.wav')

    # 播放录音文件
    with test3 as source:
        audio=r.record(source)

    #仅获取音频的前 4 秒
    # with test as source:
    #     audio=r.record(source,duration=2)

    print(type(audio))

    res=r.recognize_google(audio_data=audio)
    # res2=r.recognize_google(audio_data=audio,language='zh-CN',show_all=True)
    print(res)



# 将说的转成文本
def speech_to_text():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('say somethons....')
        audio=r.listen(source)
    try:
        message = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return message


# 类似于 pyaudio 的功能，将说的保存成文件
def  speech_to_audio():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('say something....')
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    with open('output.wav','wb') as f:
        f.write(audio.get_wav_data())

# speech_to_audio()


# 查看所有扬声器
mic=sr.Microphone()
print(mic.list_microphone_names())

