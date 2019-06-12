# -*- coding: utf-8 -*-
import random
import json, urllib
from urllib import urlencode
usr_and_pass = ['user', '123456']
name = raw_input('请输入用户名：')
passd = raw_input('请输入密码：')
def Guess_number():
    sNumber = random.randint(1, 1000)
    while True:
        try:
            print '游戏开始,猜数范围1--1000，您有10次机会'
            for guessTaken in range(1, 11): #猜10次
                guess = int(raw_input('>>>'))
                if guessTaken < 10:
                    if guess < sNumber:
                        print'您输入的数字太小了！'
                    elif guess > sNumber:
                        print'您输入的数字太大了！'
                    if guess == sNumber:
                        print'恭喜你猜对了，你一共猜了 '+str(guessTaken) + ' 次'
                        exit()
                else:
                    print '您已经输入10次了，游戏结束'
                    exit()
        except ValueError, e:
            print '输入有误,请重新输入'
def purchase():
    print'=======游戏开始,您有10金币====='
    print'\t商品展示'
    print'1、果汁：5元，2、可乐：3元，\n3、雪碧：3元'
    start = 10
    a = 0
    while True:
        try:
            s_id = int(raw_input('您要购买的商品ID：>>>'))
            if s_id == int(1):
                a += 5
            elif s_id == int(2):
                a += 3
            elif s_id == int(3):
                a += 3
            else:
                print'没有此商品'
            over = int(raw_input('1：继续，2：结束>>>'))
            if over == 2:
                if a > 10:
                    no = int(input("您的金币不足,是否重新选择(1:是，2:否)"))
                    if no == 1:
                        a = 0
                    elif no == 2:
                        exit()
                else:
                    b = start - a
                    print '您一共花费', a, '元，找零', b, '元'.decode('utf-8')
                    exit()
        except ValueError, e:
            print '输入有误,请重新输入'
def Discount():
    start = int(raw_input('输入商品价格>>'))
    over = start * 0.8
    print '您的商品八折后的价格为', over
    exit()
def main():
    appkey = '64b58a95d3328324b726f53d3031d805'
    request1(appkey,'GET')
def request1(appkey, m='GET'):
    city = raw_input('输出城市>>>')
    print '正在查询，请稍后。。。'
    url = 'http://op.juhe.cn/onebox/weather/query'
    params = {
        'cityname' : city, #要查询的城市，如：温州、上海、北京
        'key' : appkey, #应用APPKEY(应用详细页查询)
        'dtype' : '', #返回数据的格式,xml或json，默认json
    }
    params = urlencode(params)
    if m =='GET':
        f = urllib.urlopen('%s?%s' % (url, params))
    else:
        f = urllib.urlopen(url, params)
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res['error_code']
        if error_code == 0:
            date_day = json.dumps(res['result']['data']['realtime']['date']).decode('unicode-escape')
            result = json.dumps(res['result']['data']['realtime']['weather']).decode('unicode-escape')
            result = result.encode('utf-8')
            result = json.loads(result)
            result = json.dumps(result)
            result = eval(result)
            date_day = eval(date_day)
            tq = result['info'].encode('utf-8').decode('unicode-escape')
            print '日期：',date_day,'天气：',tq,'温度：',result['temperature']
            exit()
        else:
            print '%s:%s' % (res['error_code'], res['reason'])
            exit()
    else:
        print 'request api error'
        exit()
def ml():
    print'1：猜字游戏\n2：购买游戏\n3：天气查询\n4：折扣测试'
    while True:
        try:
            id = int(raw_input('请输入目录id：'))
            if id == int(1):
                Guess_number()
            elif id == int(2):
                purchase()
            elif id == int(3):
                if __name__ == '__main__':
                        main()
            elif id == int(4):
                Discount()
            else:
                print'输入错误，没有此ID!!!!'
        except ValueError, e:
            print '请输入正确ID!!!!!!!'
if name == usr_and_pass[0]:
    if passd == usr_and_pass[1]:
        print'登陆成功'
        ml()
    else:
        print '账户或密码不正确...'
else:
    print '账户或密码不正确...'