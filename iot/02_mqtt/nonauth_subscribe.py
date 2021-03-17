#!/usr/bin/python3

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {}".format(str(rc)))
    client.subscribe("$SYS/broker/version")

def on_message(client, userdata, msg):
    print("topic: {}, message: {}".format(msg.topic, str(msg.payload)))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()

