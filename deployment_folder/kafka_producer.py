import numpy as np 
import pickle
import json
import logging
from kafka import KafkaProducer
import time

with open ('/Users/rishilboddula/Desktop/MLOPS/Fraud-Credit-Card-detection-MLOPS/config/data_pkl_files/x_test_data.pkl','rb') as f:
    df=pickle.load(f)
producer=KafkaProducer(bootstrap_servers='10.5.59.49:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#bootstrap_servers='localhost:9092'- Tells where Kafka brokers are located 
#value_serializer-Kafka messages are binary, so you must serialize Python objects before sending.value_serializer is a function that converts your Python object into bytes.
topic='credit_card_fraud'
for row in df:
    txn=row.tolist()
    producer.send(topic,value=txn)
    time.sleep(500)
producer.flush()