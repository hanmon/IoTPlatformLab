import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
#Change value of my_headers to your project Key
my_headers = {'CK':projectKey}
r=requests.get(apiURL,headers=my_headers)
print(r.text)
#Get a value of the first JSON object
j=json.loads(r.text)
print("The value of first JSON object:"+str(j[0]['value'][0]))
