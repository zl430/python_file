#coding=utf-8
import requests
import json
class dnspod_api_chk():
    requests_url = 'https://dnsapi.cn'
    data = 'login_token=84133,988bace08bcfff565c50a58ab356acf0&format=json'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    def __init__(self, dns_id, dns_name, value):
        self.domainid = dns_id
        self.dns_name = dns_name
        self.dns_value = value
    def dns_add(self):
        r = requests.post(self.requests_url + '/Domain.List', self.data, headers=self.headers)
        if self.domainid == None and self.dns_name == None and self.dns_value == None:
            print('参数：dnsid name value')
            domains = json.loads(r.text)['domains']
            for d in domains:
                print(d['id'], d['status'], d['name'])
            exit(1)
        w = requests.post(self.requests_url + '/Record.Create', self.data + '&domain_id=' + self.domainid + '&sub_domain=' + self.dns_name + '&record_type=A&record_line=%E9%BB%98%E8%AE%A4&value=' + self.dns_value, headers=self.headers)
        res = json.loads(w.text)['status']
        if res['code'] == '1':
            return True
        else:
            return res['code']
    def dns_del(self):
        r = requests.post(self.requests_url + '/Record.List', self.data + '&domain_id=' + self.domainid + '&sub_domain=' + self.dns_name + '&record_type=A', headers=self.headers)
        res = json.loads(r.text)['records']
        if self.domainid == None and self.dns_value == None:
            for d in res:
                print(d['id'], d['value'])
            exit(1)
        dd = requests.post(self.requests_url + '/Record.Remove', self.data + '&domain_id=' + self.domainid + '&record_id=' + self.dns_value, headers=self.headers)
        res = json.loads(dd.text)['status']
        if res['code'] == '1':
            return True
        else:
            return res['code']
qwe = dnspod_api_chk('71244700', 'www', '1.1.1.1')
qwe.dns_add()