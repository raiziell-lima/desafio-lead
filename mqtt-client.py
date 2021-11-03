import paho.mqtt.client as mqtt
import json
import os

MQTT_BROKER = "192.168.0.109"
PORT = 1883
USERNAME = "mqtt-test"
PASSWORD = "mqtt-test"
TOPIC = "topico/teste"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    payload = json.loads(msg.payload)
    if payload["comando"] == 1:
        os.system("C:\\Windows\\notepad.exe")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(USERNAME, PASSWORD)
client.connect(MQTT_BROKER, PORT)

client.loop_forever()
