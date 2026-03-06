from kafka import KafkaProducer
import json
import datetime
producer = KafkaProducer(
    bootstrap_servers = "localhost:9092",value_serializer = lambda v: json.dumps(v).encode('utf-8'))
def send_message_created(user,data):
    event = {
        'event' : 'message.created',
        "timestamp" : datetime.datetime.utcnow().isoformat(),
        'data' : {
            'user' : user,
            'message' : data
        }
    }
    producer.send('messages',event)