#!/usr/bin/python3

import requests
import numpy as np
import time
import json
import configparser 
import Adafruit_DHT



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

#get real data
while 1:
    humidity,temperature=Adafruit_DHT.read_retry(11,18)
    if humidity is not None and temperature is not None:
        #t = str(time.strftime("%Y-%m-%dT%H:%M:%S"))
        payload=[{"id":"Temperature","value":[temperature]},{"id":"humidity","value":[humidity]}]
        print(payload)
        response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
        print(response.text)
        time.sleep(5)
    else:
        print("failed")

