import json
import requests, json
url = 'http://129.211.101.32:81/api_jsonrpc.php'
headers = {"Content-Type": "application/json"}
login = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "admin",
        "password": "zuolei@$.#2580."
    },
    "auth": None,
    "id": 1,
}
auth = requests.post(url, data=json.dumps(login), headers=(headers))
auth = auth.json()
print(auth)
#-------------------------------获取主机ID-----------------------------------------
host_get = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid", "name", "host", "status"],
        "filter": {"ip": ["129.211.109.212", "129.211.105.64"]}
    },
    "auth": "" + auth['result'] + "",
    "id": 1,
}
hostid_get = requests.post(url, data=json.dumps(host_get), headers=(headers))
hostid_get = hostid_get.json()
print(host_get)
print(hostid_get['result'][0])
hostid = hostid_get['result'][0]['hostid']
print(hostid)
print(hostid, hostid_get['result'][1]['hostid'])
#-------------------------------获取groupid-------------------------------------------
group_get = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Zabbix servers"
            ]
        }
    },
    "auth": "" + auth['result'] + "",
    "id": 1
}
groupid_get = requests.post(url, data=json.dumps(group_get), headers=(headers))
print(group_get)
groupid_get = groupid_get.json()
print(groupid_get['result'][0])
groupid = groupid_get['result'][0]['groupid']
print(groupid)
#-------------------------------获取模板---------------------------------------------
template_get = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Template OS Linux",
            ]
        }
    },
    "auth":""+auth['result']+"",
    "id": 1
}
templateid_get = requests.post(url, data=json.dumps(template_get), headers=(headers))
templateid_get = templateid_get.json()
templateid = templateid_get['result'][0]['templateid']
print(templateid)
#-------------------------------创建主机----------------------------------------------
host_create = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "192.168.1.1",
        "name": "test_api",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "" + groupid + ""
            }
        ],
        "templates": [
            {
                "templateid": "" + templateid + ""
            }
        ],
    },
    "auth": "" + auth['result'] + "",
    "id": 1,
}
host_create_id = requests.post(url, data=json.dumps(host_create), headers=(headers))
host_create_id = host_create_id.json()
print(host_create_id)