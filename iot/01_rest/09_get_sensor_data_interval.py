#讀取設備感測器時間區間內多筆感測資料
import requests
import json
import configparser

sensorId='Temperature'
config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/sensor/' + sensorId + '/rawdata'
#Concate HTTP GET query strings
apiURL = apiURL + '?' + 'start=2021-03-17T07:00:00Z' + '&end=2021-03-17T09:00:00Z'
#Change value of my_headers to your project Key
my_headers = {
    'CK':projectKey,
    }
r=requests.get(apiURL,headers=my_headers)
print(r.text)

