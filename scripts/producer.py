'''
Created on 2017年11月27日

@author: Administrator
'''
# coding: utf-8
import csv
import time
from kafka import KafkaProducer

# 实例化一个KafkaProducer示例，用于向kafka投递消息
producer = KafkaProducer(bootstrap_servers='192.168.2.129:9092')
# 打开数据文件
cxvfile = open("../data/user_log.csv", "r", encoding='UTF-8')
# 生成用于读取csv文件的reader
reader = csv.reader(cxvfile)
for line in reader:
    gender = line[9] # 性别在每行日志代码的第9个元素
    if gender == 'gender':
        continue # 去掉第一行表头
    time.sleep(0.1) # 每隔0.1秒发送一个一行数据
    # 发送数据， topic为sex
    producer.send('sex', line[9].encode('utf-8'))