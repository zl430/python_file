#coding=utf-8
import requests
import re
import json
import sys
def add(dns_id, dns_name, dns_value):
    name = '/Domain.List'
    url = 'https://dnsapi.cn' + name
    domain = 'zuolei0430.top'
    data = 'login_token=84133,988bace08bcfff565c50a58ab356acf0&format=json'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    r = requests.post(url, data, headers=headers)
    over = r.text
    # if len(sys.argv) != 4:
    #     print('参数：dnsid name value')
    #     res = json.loads(over)
    #     domains = res['domains']
    #     for d in domains:
    #         print(d['id'], d['status'], d['name'])
    #     exit(1)
    aa = re.findall(r"domains", over)
    # print(aa)
    # domainid = sys.argv[1]
    # name = sys.argv[2]
    # value = sys.argv[3]
    domainid = dns_id
    name = dns_name
    value = dns_value
    print(domainid, name, value)
    jl = '/Record.Create'
    url1 = 'https://dnsapi.cn' + jl
    w = requests.post(url1, data + '&domain_id=' + domainid + '&sub_domain=' + name + '&record_type=A&record_line=%E9%BB%98%E8%AE%A4&value=' + value, headers=headers)
    add1 = w.text
    # res = json.loads(add1)
    # aaa = res['status']
    # print(aaa['code'])
    bb = re.findall(r'successful', add1)
    if bb != []:
        return True
    else:
        return False
def dns_del(dns_id, dns_name, dns_value):
    name = '/Record.List'
    url = 'https://dnsapi.cn' + name
    domainid = dns_id
    name = dns_name
    data = 'login_token=84133,988bace08bcfff565c50a58ab356acf0&format=json'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    r = requests.post(url, data + '&domain_id=' + domainid + 'sub_domain=' + name + '&record_type=A', headers=headers)
    over = r.text
    res = json.loads(over)
    records = res['records']
    # if len(sys.argv) != 3:
    #     for d in records:
    #         print(d['id'], d['value'])
    #     exit(1)
    value = dns_value
    jl = '/Record.Remove'
    del_url = 'https://dnsapi.cn' + jl
    dd = requests.post(del_url, data + '&domain_id=' + domainid + '&record_id=' + value, headers=headers)
    del_over = dd.text
    bb = re.findall(r'successful', del_over)
    print(del_over)
    print(bb)
add('71244700', 'www', '1.1.1.2')
# dns_del('71244700', 'www', '111')