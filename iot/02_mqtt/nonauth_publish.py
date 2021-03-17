#!/usr/bin/python3

import paho.mqtt.publish as publish

host = "iot.eclipse.org"
topic = "$SYS/broker/version"
payload = "hello mqtt"

print("topic: {}, message: {}".format(topic, payload))

publish.single(topic, payload, hostname=host)

