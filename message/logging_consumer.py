from kafka import KafkaConsumer
import json
import os
import django
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()

from message.models import Message
from django.contrib.auth.models import User

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers = 'localhost:9092',
    group_id = 'logging-group',
    auto_offset_reset = 'earliest',
    value_deserializer = lambda v : json.loads(v.decode('utf-8'))
)


for msg in consumer:
    event = msg.value
    print("LOG:", event)
    with open("logs.txt", "a") as f:
        f.write(str(event) + "\n")