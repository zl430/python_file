# -*- coding: cp936 -*-
import random
import json, urllib
import requests
from urllib import urlencode
usr_and_pass = ['user1', '123456']
name = raw_input('�������û�����')
passd = raw_input('���������룺')
def d1():
    sNumber = random.randint(1, 1000)
    print '.................'
    print sNumber
    print '��Ϸ��ʼ,������Χ1--1000������10�λ���'
    for guessTaken in range(1, 11): #��10��
        guess = int(raw_input('>>>'))
        if guess < sNumber:
            print'�����������̫С�ˣ�'
        elif guess > sNumber:
            print'�����������̫���ˣ�'
        if guess == sNumber:
            print'��ϲ��¶��ˣ���һ������ '+str(guessTaken) + ' ��'
            break
def d2():
    print'.................'
    print'=======��Ϸ��ʼ,����10���====='
    print'\t��Ʒչʾ'
    print'1����֭��5Ԫ��2�����֣�3Ԫ��\n3��ѩ�̣�3Ԫ'
    start = 10
    a = 0
    while True:
        s_id = int(raw_input('��Ҫ�������ƷID��>>>'))
        if s_id == int(1):
            a += 5
        elif s_id == int(2):
            a += 3
        elif s_id == int(3):
            a += 3
        else:
            print'û�д���Ʒ'
        over = int(raw_input('1��������2������>>>'))
        if over == 2:
            if a > 10:
                no = int(input("���Ľ�Ҳ���,�Ƿ�����ѡ��(1:�ǣ�2:��)"))
                if no == 1:
                    a = 0
                elif no == 2:
                    break
            else:
                b = start - a
                print("��һ������", a, "Ԫ������", b, "Ԫ")
                break
def d4():
    start = int(raw_input('������Ʒ�۸�>>'))
    over = start * 0.8
    print '������Ʒ���ۺ�ļ۸�Ϊ', over
def main():
    appkey = '64b58a95d3328324b726f53d3031d805'
    request1(appkey,'GET')
def request1(appkey, m='GET'):
    city = raw_input('�������>>>')
    print '���ڲ�ѯ�����Ժ󡣡���'
    url = 'http://op.juhe.cn/onebox/weather/query'
    params = {
        'cityname' : city, #Ҫ��ѯ�ĳ��У��磺���ݡ��Ϻ�������
        'key' : appkey, #Ӧ��APPKEY(Ӧ����ϸҳ��ѯ)
        'dtype' : '', #�������ݵĸ�ʽ,xml��json��Ĭ��json
    }
    # params = urlencode(params)
    r = requests.get(url, params=params)

    print r.text
    # if m =='GET':
    #     f = urllib.urlopen('%s?%s' % (url, params))
    # else:
    #     f = urllib.urlopen(url, params)
    # content = f.read()
    # res = json.loads(content)
    # if res:
    #     error_code = res['error_code']
    #     if error_code == 0:
    #         print res['result']
    #         # print json.dumps(res['result'], ensure_ascii=False, encoding='cp936')
    #         ssssss = str(res['result'])
    #         print ssssss
    #         print json.dumps(ssssss).decode('unicode-escape')
    #         print type(res['result'])
    #     else:
    #         print '%s:%s' % (res['error_code'], res['reason'])
    # else:
    #     print 'request api error'
def ml():
    print'1��������Ϸ\n2��������Ϸ\n3���¶Ȳ�ѯ\n4���ۿ۲���'
    id = int(raw_input('������Ŀ¼id��'))
    if id == int(1):
        d1()
    elif id == int(2):
        d2()
    elif id == int(3):
        if __name__ == '__main__':
                main()
    elif id == int(4):
        d4()
    else:
        print'id���벻��ȷ'
if name == usr_and_pass[0]:
    if passd == usr_and_pass[1]:
        print'��½�ɹ�'
        ml()
    else:
        print '�˻������벻��ȷ...'
else:
    print '�˻������벻��ȷ...'