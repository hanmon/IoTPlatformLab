#!/usr/bin/python3

import requests
import json
import time
import configparser 

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
cameraId   = config.get('device-key', 'cameraId')

apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/snapshot'

headers = { 
    "CK":projectKey,
    "accept":"application/json",
}   

files = {"img": ("test", open("/home/pi/test.jpg", "rb"), "image/jpeg"), "meta":(None, json.dumps({"id":cameraId,"value":["Raspberry pi camera"]}), 'application/json')}

response = requests.post(apiURL, files=files, headers=headers)
print(response.text)
