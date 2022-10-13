# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

import pyaudio
import wave
from  tqdm import tqdm
import  time

'''
pyaudio 录制及播放音频信息
录制
播放
回调
tqdm是显示进度条
'''


# 录制
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

    # print('**** start recording')
    # for i in  tqdm(range(0,int(RATE/CHUNK*record_second))):
    #     data=stream.read(CHUNK)
    #     wf.writeframes(data)
    # print('***Done')

    # 第二种方式:
    freams=[]
    for i in range(0,int(RATE/CHUNK*record_second)):
        data=stream.read(CHUNK)  # 这个就是写入
        freams.append(data)
    wf.writeframes(b''.join(freams))

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()


# record_audio('output.wav',5)




# 播放
def  play_audio(filename):
    CHUNK=1024

    wf=wave.open(filename,'rb')
    p=pyaudio.PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)

    data=wf.readframes(CHUNK)
    datas=[]

    while len(data) > 0:
        # stream.write(data)  # 这个就是播放
        data=wf.readframes(CHUNK)
        datas.append(data)
    for d in tqdm(datas):
        stream.write(d)
    stream.stop_stream()
    stream.close()

    p.terminate()

# play_audio('16k16bit.wav')



#  wired 方式 就是边录制边播放
def record_and_play(record_second):
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=16000

    p=pyaudio.PyAudio()
    stream=p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  output=True,
                  frames_per_buffer=CHUNK)

    print('**** start recording')
    for i in  tqdm(range(0,int(RATE/CHUNK*record_second))):
        data=stream.read(CHUNK)
        stream.write(data)  # 这个是播放的设置
    print('***Done')

    stream.stop_stream()
    stream.close()
    p.terminate()

# record_and_play(60)



# wire 使用callback的方式来实现边录制边播放的方式
def  play_callback():
    WIDTH = 2
    CHANNELS = 1
    RATE = 16000

    p=pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        return (in_data,pyaudio.paContinue)

    stream=p.open(format=p.get_format_from_width(WIDTH),
                  channels=CHANNELS,
                  rate=RATE,
                  output=True,
                  input=True,
                  stream_callback=callback)

    stream.start_stream()
    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    p.terminate()

play_callback()


#  回调方式调用   当需要在执行其他程序时同时播放音频,可以使用回调的方式播放
def  play_audio_callback(filename):
    CHUNK=1024

    wf=wave.open(filename,'rb')
    p=pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data=wf.readframes(frame_count)
        return (data,pyaudio.paContinue)

    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),
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


