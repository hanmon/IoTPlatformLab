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
#串接HTTP GET查詢字串，以問號起頭，包括開始與結束時間，格式為 ISO 8601,例如:2016-07-14T23:55:00Z
#開始與結束時間中間以'&'連接,每次查詢上限為500筆
apiURL = apiURL + '?' + 'start=2021-03-17T07:00:00Z' + '&end=2021-03-17T09:00:00Z'
#改為你自己的projec/device key
my_headers = {
    'CK':projectKey,
    }
#送出HTTP GET
r=requests.get(apiURL,headers=my_headers)
#印出回應資訊，為JSON格式，可利用linux管線命令導向到jq程式作排版
print(r.text)

