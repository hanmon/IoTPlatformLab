#!/usr/bin/python3

import requests
import json
import configparser 

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')

apiURL = 'http://iot.cht.com.tw/iot/v1/device'
headers = { 
    "CK":projectKey,
}   
response = requests.get(apiURL, headers=headers)
print(response.text)

#ret = json.loads(response.text)
#print(ret[0]['id'], ret[0]['name'])
