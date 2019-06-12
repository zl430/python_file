# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox #引用子模块
import re
import sys
import requests
import mysql.connector
win = tkinter.Tk()
win.title('数据查询')
win.geometry('1000x600')
win.resizable(width=False, height=False)
def validateText():
    val = entry1.get()
    if re.findall('^[0-9a-zA-Z_]{1,}$', str(val)):
        return True
    else:
        label3['text'] = '用户名只能包含字母、数字、下划线'
        return False
def mailText():
    mail = entry3.get()
    if re.findall('^[0-9a-zA-Z_]{1,}@[0-9a-zA-Z_]{1,}.[a-z]{1,3}$', str(mail)):
        return True
    else:
        label3['text'] = '邮箱格式不符合'
        return False
def zc_over():
    tkinter.messagebox.showinfo(title='提示信息', message='注册成功')
def login():
    win.destroy()
    import login
    login()
#--------------------------登陆数据库验证用户-----------------------------------
def db_check():
    username = entry1.get()
    password = entry2.get()
    mail = entry3.get()
    print(username, password, mail)
    url = 'http://127.0.0.1:66/registered'
    data = {'username': username, 'password': password, 'mail': mail}
    over = requests.post(url, data, timeout=30)
    a = over.text
    if a == '1':
        label3['text'] = username, '注册成功'
        zc_over()
        win.destroy()
    elif a == '0':
        label3['text'] = username, '已存在'
    else:
        label3['text'] = '注册失败'
#------------------------------------------------------------------------------------
label1 = tkinter.Label(win, text='用户名:', font=('宋体', '18'))
label1.grid(row=0, column=0)
label2 = tkinter.Label(win, text='密  码:', font=('宋体', '18'))
label2 .grid(row=1, column=0)
label4 = tkinter.Label(win, text='邮  箱:', font=('宋体', '18'))
label4 .grid(row=2, column=0)
v = tkinter.StringVar()
entry1 = tkinter.Entry(win, font=('宋体', '18'), textvariable = v, validate = 'focusout', validatecommand = validateText)
entry1.grid(row=0, column=1)
entry1.focus_force()
entry2 = tkinter.Entry(win, font=('宋体', '18'), show='*')
entry2.grid(row=1, column=1)
entry3 = tkinter.Entry(win, font=('宋体', '18'))
entry3.grid(row=2, column=1)
button1 = tkinter.Button(win, text='注册', font=('宋体', '18'), command = db_check)
button1.grid(row=3, column=0, padx=50, pady=10)
button2 = tkinter.Button(win, text='退出', font=('宋体', '18'), command = sys.exit)
button2.grid(row=3, column=1, padx=80, pady=10)
# button2 = tkinter.Button(win, text='登陆', font=('宋体', '18'), command = login)
# button2.grid(row=3, column=1, padx=80, pady=10)
label3 = tkinter.Label(win, text='信息提示区', font=('华文新魏', '16'), relief = 'ridge', width = 30)
label3.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='s')
win.mainloop()