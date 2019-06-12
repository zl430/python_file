# -*- coding: utf-8 -*-
import random
import requests
import json
usr_and_pass = ['user1', '123456']
name = input("请输入用户名：")
passd = input("请输入密码：")
def d1():
    sNumber = random.randint(1, 1000)
    print(".................")
    print("游戏开始,猜数范围1--1000，您有10次机会")
    for guessTaken in range(1, 11): #猜10次
        guess = int(input(">>>"))
        if guess < sNumber:
            print('您输入的数字太小了！')
        elif guess > sNumber:
            print('您输入的数字太大了！')
        if guess == sNumber:
            print('恭喜你猜对了，你一共猜了 '+str(guessTaken) + ' 次')
            break
def d2():
    print(".................")
    print("=======游戏开始,您有10金币=====")
    print("\t商品展示")
    print("1、果汁：5元，2、可乐：3元，\n3、雪碧：3元")
    start = 10
    a = 0
    while True:
        s_id = int(input("您要购买的商品ID：>>>"))
        if s_id == int(1):
            a += 5
        elif s_id == int(2):
            a += 3
        elif s_id == int(3):
            a += 3
        else:
            print("没有此商品")
        over = int(input("1：继续，2：结束>>>"))
        if over == 2:
            if a > 10:
                no = int(input("您的金币不足,是否重新选择(1:是，2:否)"))
                if no == 1:
                    a = 0
                elif no == 2:
                    break
            else:
                b = start - a
                print("您一共花费", a, "元，找零", b, "元")
                break
def d3():
    city = input("输入城市>>>")
    print("正在查询，请稍后。。。")
    appkey = "64b58a95d3328324b726f53d3031d805"
    url = "http://apis.juhe.cn/simpleWeather/query"
    params = {
        "cityname": city, #要查询的城市，如：温州、上海、北京
        "key": appkey, #应用APPKEY(应用详细页查询)
        "dtype": "", #返回数据的格式,xml或json，默认json
    }
    print(url, params)
    r = requests.get(url, params=params)
    print(r)
    print(r.text)
def d4():
    start = int(input("输入商品价格>>"))
    over = start * 0.8
    print("您的商品八折后的价格为", over)
def ml():
    print("1：猜字游戏\n2：购买游戏\n3：温度查询\n4：折扣测试")
    id = int(input("请输入目录id："))
    print(id)
    if id == int(1):
        d1()
    elif id == int(2):
        d2()
    elif id == int(3):
        d3()
    elif id == int(4):
        d4()
    else:
        print("id输入不正确")
if name == usr_and_pass[0]:
    if passd == usr_and_pass[1]:
        print("登陆成功")
        ml()
    else:
        print("账户或密码不正确...")
else:
    print("账户或密码不正确...")