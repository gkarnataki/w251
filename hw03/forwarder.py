import numpy as np
import cv2
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="facetopic"

REMOTE_MQTT_HOST="50.23.130.138"
REMOTE_MQTT_PORT="1883"
REMOTE_MQTT_TOPIC="remotefacetopic"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc:" + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(remoteclient, userdata, msg):
    try:
        print("mesage received")
        msg = msg.payload
        remoteclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
        remoteclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=1, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])

local_client = mqtt.Client()
local_client.on_connect = on_connect_local
local_client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_client.on_message = on_message


local_client.loop_forever()
