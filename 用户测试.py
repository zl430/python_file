#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zuolei'
old = {}
new = {}
f = open('user.txt', 'r').readlines()
for line in f:
    (key, value) = line.strip().split(':')
    old[key] = value
print('---------------')
print('|注册新用户：1|')
print('---------------')
print('|用户登陆  ：2|')
print('---------------')
d = input('请输入序号：')
def user_new():
    name = input('请输入用户名：')
    if name == '':
        print('用户名不能为空')
    else:
        password1 = input('请输入密码：')
        chk = password1.isdigit()
        if chk == True:
            if password1 == '':
                print('密码不能为空')
            else:
                password2 = input('请再次输入密码：')
                if password1 == password2:
                    new[name] = password2
                    w = open('user.txt', 'a')
                    for (key,value) in new.items():
                        w.write('%s:%s\n' % (key, value))
                    print('用户注册成功')
                else:
                    print('两次密码不一致')
        else:
            print('请输入数字类型密码')
            user_new()
def user_old(name):
    password = input('请输入密码：')
    if password == '':
        print('密码不能为空')
        exit()
    else:
        if old[name] != password:
            conn = 1
            while conn < 3:
                password = input('密码错误，请重新输入：')
                if old[name] == password:
                    print('登陆成功')
                    exit()
                else:
                    if conn == 2:
                        print('密码错误，账户已锁定。')
                        v = open('user_new.txt', 'a')
                        v.write('%s\n' % name)
                        exit()
                    else:
                        conn += 1
        else:
            print('登陆成功')
            exit()
def user_check():
    name = input('请输入用户名：')
    if name == '':
        print('用户名不能为空')
        exit()
    else:
        file = open('user_new.txt', 'r').readlines()
        for i in file:
            print(i)
            print(name)
            if i == name:
                print('用户已锁定，暂时不能使用')
                exit()
            else:
                user_old(name)
if int(d) == 1:
    user_new()
elif int(d) == 2:
    user_check()