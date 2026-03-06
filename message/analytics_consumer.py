
import os
import django
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()
from kafka import KafkaConsumer
import json
# import django
from message.models import Message
from django.contrib.auth.models import User

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers = 'localhost:9092',
    group_id = 'analytics-group',
    auto_offset_reset = 'earliest',
    value_deserializer = lambda v : json.loads(v.decode('utf-8'))
)
d = {}
for msg in consumer:
    event = msg.value
    if(event['event'] == 'message.created') :
        data = event['data']
        d[data['user']] = d.get(data['user'],0) + 1
        print(f"{data['user']} sent {d[data['user']]} messages")