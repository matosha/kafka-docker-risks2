import requests,json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

head=["Accept application/json"]
response=requests.get("https://api.msrc.microsoft.com/cvrf/v2.0/updates",  headers={"Accept":"application/json"})
print(response.json())
for i in range(0,10):
        producer.send('tenable', json.dumps(response.json()).encode('utf-8'))
