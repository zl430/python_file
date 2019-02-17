# -*- coding:utf-8 -*-
# Author:Steven Kang

import os,sys,getpass  #导入os,sys,getpass 模块
u = 0                   #用户的循环次数
while u < 3:
    username = input("请输入您的用户名:")           #使用input 让用户输入并赋值给username变量
    lock_file = open('user_new.txt','r+')             #打开account_lock文件，权限是读取更新，并赋值给lock_f变量
    lock_list = lock_file.readlines()                    #使用.readlines的方法逐行读取account_lock文件，并赋值给lock_list变量

    for lock_line in lock_list:                      #使用for循环读取account_lock的内容
        lock_line = lock_line.strip('\n')            #使用.strip()的方法去点换行符
        if username == lock_line:
            print('用户 %s 已经锁定，请联系您的系统管理员' % username)  #如果存在打印输出
            sys.exit(1)                                    #跳出循环
    user_file = open('user.txt','r')                    #打开account文件，权限是读取更新，并赋值给user_f变量
    user_list = user_file.readlines()                    #使用.readlines的方法逐行读取account文件，并赋值给user_list变量
    for user_line in user_list:                      #使用for循环读取account的内容
        (user,passwd) = user_line.strip('\n').split()   #分别获取账号和密码信息
        if username == user:                         #使用if判断用户输入的用户是否在normal_user中存在
            p = 0                                    #输入密码的循环次数
            while p < 3:                            #只要用户登录异常不超过3次就不断循环
                password = getpass.getpass('请输入您的密码：')       #使用getpass模块的.getpass方法让用户输入密码（输入的时候不会显示）
                if password == passwd:              #使用if判断用户输入的密码在normal_user中是否存在(相等)
                    print('欢迎 %s 登录系统' %username)              #用户名密码全部相等（存在）打印欢迎登录信息
                    sys.exit(0)                         #跳出循环
                else:
                    if p != 2:
                        print('对不起，%s 的密码错误，请重新输入，您还有 %d 次机会'%(username,2 - p))
                p += 1                              #密码输入错误后，循环值增加1
            else:
                lock_file.write(username + '\n')      #用户名密码输入次数超过3次的用户添加到account_lock文件中
                #lock_f.write('%s \n' %username)
                sys.exit('对不起 %s 用户已经锁定，请联系管理员'% username)
        else:
            pass                                   #当用户没匹配时，跳过并继续循环
    else:
        if u != 2:                                 #i=2时，是最后一次机会，不用在提示还剩余0次机会了
            print('对不起，%s 输入错误，请重新输入，您还有 %d 次机会' %(username, 2 - u))
    u += 1                                         #当用户输入错误时，循环值增加1
else:
    sys.exit('因为您的错误输入，程序已经退出，请重新运行')   #用户输入三次错误后，异常退出
lock_f.close()          #关闭lock_f文件