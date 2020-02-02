import paho.mqtt.client as client
import s3fs
from random import randint

LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "remotefacetopic"

def on_connect_local(client, userdata, flags, rc):
    client.subscribe(LOCAL_MQTT_TOPIC)


def save_to_s3(msg):
    p='%Y-%m-%d %H:%M:%S'
    f = open("/mnt/s3files/hw03/face_" + str(randint(0, 1000000)) + ".png", "w+")
    f.write(msg)
    f.close()


def on_message(client, userdata, msg):
    try:
        #print("remote client - message received...", msg.payload)
        save_to_s3(msg.payload)
    except:
        print("unexpected error", sys.exc_info()[0])



local_client = client.Client()
local_client.on_connect = on_connect_local
local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_client.on_message = on_message

local_client.loop_forever()
