#coding=utf-8
import requests
import json
url = "http://apis.juhe.cn/cnoil/oil_city"
headers = {"Content-Type": "application/json"}
data = {'dtype': '', 'key': '47d3ea28a8fd5fb9bea00249cb039396'}
data2 = {"mobile": "17600817185", "tpl_id": "148870", "tpl_value": "#code#=1235231"}
r = requests.get(url, data).text
r = json.loads(r)
over = r["result"][0]["92h"]
print("北京市今日92号汽油油价：", over)
