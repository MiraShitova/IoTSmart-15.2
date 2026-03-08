import paho.mqtt.client as mqtt
import json
import random
import time

MQTT_BROKER = "localhost"
TOPIC_PREFIX = "smart_city/waste/"

containers = [
    {"id": f"bin_{i}", "lat": 50.45 + random.uniform(-0.01, 0.01), "lng": 30.52 + random.uniform(-0.01, 0.01)}
    for i in range(1, 11)
]

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

print("Симуляция запущена...")

try:
    while True:
        for bin in containers:
            data = {
                "id": bin["id"],
                "fill_level": random.randint(0, 100),
                "lat": bin["lat"],
                "lng": bin["lng"],
                "status": "OK"
            }
            client.publish(f"{TOPIC_PREFIX}{bin['id']}", json.dumps(data))
            print(f"Отправлено: {bin['id']} - {data['fill_level']}%")
        
        time.sleep(10)
except KeyboardInterrupt:
    client.disconnect()