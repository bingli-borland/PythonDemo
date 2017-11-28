'''
Created on 2017年11月27日

@author: Administrator
'''
# coding: utf-8
from kafka import KafkaConsumer

consumer = KafkaConsumer('result', bootstrap_servers='192.168.2.129:9092')
for msg in consumer:
    print((msg.value).decode('utf-8'))