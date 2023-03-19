import requests,json
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

head=["Accept application/json"]
response=requests.get("https://api.msrc.microsoft.com/cvrf/v2.0/updates",  headers={"Accept":"application/json"})
print(response.json())
for i in range(0,10):
        producer.send('msfeed', value=json.dumps(response.json()))
#for e in range(1000):
#    data = {'number' : e}
#    producer.send('hackernews', value=data)

