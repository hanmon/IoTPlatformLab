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
    "Content-Type": "application/json",
}   

payload={"name":"Hygrometer","desc":"My Hygrometer","type":"general","uri":"http://a.b.c.d/hygrometer","lat":24.95,"lon":121.16,"attributes":[{"key":"label","value":"Hygrometer"},{"key":"region","value":"Taiwan"}]}

response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
print(response.text)

