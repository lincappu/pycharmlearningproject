# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import time

from kafka import KafkaConsumer
from kafka import KafkaProducer


def start_producer():
    producer = KafkaProducer(bootstrap_servers='172.16.71.3:9092')
    for i in range(0, 100):
        msg = 'msg is' + str(i)
        producer.send('a_top2', msg.encode('utf-8')).get(timeout=200)
        time.sleep()


def start_consumer():
    print("starting")
    consumer = KafkaConsumer('a_top2', group_id='my_group_1',client_id='my_client_1',auto_offset_reset='latest', enable_auto_commit=True, bootstrap_servers='172.16.71.3:9092')
    # print(consumer.config)
    for msg in consumer:
        print('starting')
        print(msg)
        # print("topic = %s" % msg.topic)  # topic default is string
        # print("partition = %d" % msg.offset)
        # print("value = %s" % msg.value.decode())  # bytes to string
        # print("timestamp = %d" % msg.timestamp)
        # print("time = ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.timestamp / 1000)))


if __name__ == '__main__':
    start_producer()
    start_consumer()
