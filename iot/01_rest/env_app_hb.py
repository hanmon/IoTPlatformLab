#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import numpy as np
import time
import json
import configparser 
import board
import adafruit_dht
import picamera
from pigpiod import getPmsData
from ch_tts_function import playSpeech

config = configparser.ConfigParser()
config.read('../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
dht11Id   = config.get('device-key', 'dht11Id')
pmsId=config.get('device-key', 'pmsId')
cameraId=config.get('device-key', 'cameraId')


apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
apiURLCam = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/snapshot'
apiURLHb = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/heartbeat'

headers = { 
    "CK":projectKey,
    "Content-Type": "application/json",
} 

headers2 = {
    "CK":projectKey,
    "accept":"application/json",
}

headers_hb = {
    "CK":projectKey
} 

dhtDevice = adafruit_dht.DHT11(board.D18)
camera = picamera.PiCamera()
while True:
    #get DHT11 values
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print("Temp:{:.1f}C / Humidity:{}% ".format(temperature_c, humidity))
    #get PMS values
    PM1,PM25,PM10=getPmsData()
    #payload=[{"id":sensorId, "value":[v]}]
    payload=[{"id":dht11Id,"value":[temperature_c,humidity]},{"id":pmsId,"value":[PM1,PM25,PM10]}]
    print(payload)
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    print(response.text)
    #play speech of PM2.5 value
    playSpeech("PM2點5的值為"+str(PM25),"tc");
    #take a photo
    time.sleep(2)    # Camera warm-up time
    camera.capture('test.jpg')
    files = {"img": ("test", open("test.jpg", "rb"), "image/jpeg"), "meta":(None, json.dumps({"id":cameraId,"value":["Raspberry pi camera"]}), 'application/json')}
    response = requests.post(apiURLCam, files=files, headers=headers2)
    print(response.text)
    payload={"pulse":"1000"}
    response = requests.post(apiURLHb, headers=headers_hb, data=json.dumps(payload))
    print(response.text)
    time.sleep(10)
