# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox #引用子模块
import re
import sys
import mysql.connector
win = tkinter.Tk()
win.title('用户注册')
win.geometry('400x170+350+150')
def validateText():
    val = entry1.get()
    if re.findall('^[0-9a-zA-Z_]{1,}$', str(val)):
        return True
    else:
        label3['text'] = '用户名只能包含字母、数字、下划线'
        return False
#--------------------------获取数据库信息-----------------------------------
file = open('mysql.conf', 'r')
f = file.readlines()
l = " ".join(f)
ip = re.findall(r"host=(.\S+)", l)
us = re.findall(r"user=(.\S+)", l)
pd = re.findall(r"passwd=(.\S+)", l)
pt = re.findall(r"port=(.\S+)", l)
db = re.findall(r"database=(.\S+)", l)
#--------------------------登陆数据库验证用户-----------------------------------
def db_check():
    db_host = ip[0]
    db_user = us[0]
    db_pass = pd[0]
    db_port = pt[0]
    db_data = db[0]
    mydb = mysql.connector.connect(
        host=str(db_host),   # 数据库主机地址a
        user=str(db_user),    # 数据库用户名
        passwd=str(db_pass),  # 数据库密码
        port=str(db_port),
        database=str(db_data)
    )
    mycursor = mydb.cursor()    #创建游标
    u_name = entry1.get()
    u_pass = entry2.get()
    if u_name != "" and u_pass != "":
        mycursor.execute("INSERT INTO py_table (name, password) VALUES (%s, %s)", (u_name, u_pass))
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")
        label3['text'] = u_name, '注册成功'
    else:
        label3['text'] = '不允许为空值'
#------------------------------------------------------------------------------------
label1 = tkinter.Label(win, text='用户名:', font=('宋体', '18'))
label1.grid(row=0, column=0)
label2 = tkinter.Label(win, text='密码:', font=('宋体', '18'))
label2 .grid(row=1, column=0)
v = tkinter.StringVar()
entry1 = tkinter.Entry(win, font=('宋体', '18'), textvariable = v, validate = 'focusout', validatecommand = validateText)

entry1.grid(row=0, column=1)
entry1.focus_force()
entry2 = tkinter.Entry(win, font=('宋体', '18'), show = '*')

entry2.grid(row=1, column=1)
button1 = tkinter.Button(win, text='注册', font=('宋体', '18'), command = db_check)
button1.grid(row=2, column=0, padx=50, pady=10)
button2 = tkinter.Button(win, text='退出', font=('宋体', '18'), command = sys.exit)
button2.grid(row=2, column=1, padx=80, pady=10)
label3 = tkinter.Label(win, text='信息提示区', font=('华文新魏', '16'), relief = 'ridge', width = 30)
label3.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='s')
def cs():
    print(tkinter.messagebox.askquestion(title='Hi', message='成功的'))
    tkinter.Button(win, text='注册', command=cs).pack()
win.mainloop()