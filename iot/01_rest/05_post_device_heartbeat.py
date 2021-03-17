#!/usr/bin/python3

import requests
import json
import configparser 

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')

apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/heartbeat'
headers = { 
    "CK":projectKey,
}   
payload={"pulse":"1000"} # ms

response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
print(response.text)
