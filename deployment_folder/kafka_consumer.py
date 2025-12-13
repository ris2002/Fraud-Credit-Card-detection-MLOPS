import numpy as np 
import pickle
import json
import logging
from kafka import KafkaConsumer
import time
import requests

FAST_API_URL='http://127.0.0.1:8000/predict'
consumer=KafkaConsumer('credit_card_fraud',bootstrap_servers='10.5.59.49:9092',auto_offset_reset='earliest',enable_auto_commit=True,group_id='fraud-detector',value_deserializer=lambda x: json.loads(x.decode('utf-8')))
for msg in consumer:
    row=msg.value
    response=requests.post(FAST_API_URL,json={"data":row})
    print('Prediction:',response.json())

        
    




