#!/usr/bin/python3

import requests
import numpy as np
import time
import json
import configparser 

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
sensorId   = config.get('device-key', 'sensorId')

apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
headers = { 
    "CK":projectKey,
    "Content-Type": "application/json",
}   

v = str(int(np.random.random() *100))
t = str(time.strftime("%Y-%m-%dT%H:%M:%S"))
payload=[{"id":sensorId, "value":[v]}]
print(payload)

response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
print(response.text)

