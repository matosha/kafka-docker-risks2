import requests,json
from kafka import KafkaConsumer

consumer = KafkaConsumer('hackernews', bootstrap_servers=['localhost:9092'])

print("getty")
for message in consumer:
    consumer.commit() 
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))