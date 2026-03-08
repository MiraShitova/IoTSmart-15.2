import json
import paho.mqtt.client as mqtt

to_collect = []

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    if data['fill_level'] > 70:
        if data['id'] not in [b['id'] for b in to_collect]:
            to_collect.append(data)
            print(f"🚛 Додано в маршрут: {data['id']} ({data['fill_level']}%)")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("smart_city/waste/#")

print("Backend запущено. Чекаю на повні баки...")
client.loop_forever()