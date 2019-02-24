# encoding=utf-8
import tkinter as tk
import re
import mysql.connector
import select_sql
from tkinter import ttk
chk_win = tk.Tk()
chk_win.geometry('800x500')
chk_win.wm_title('详细信息')
def chk_user():
    label['text'] = "user"
    import chart
    chart
def chk_pass():
    label['text'] = "pass"
#--------------------------获取数据库信息-----------------------------------
file = open('E:/Git/file/python_file/db_mysql.conf', 'r')
f = file.readlines()
l = " ".join(f)
ip = re.findall(r"host=(.\S+)", l)
us = re.findall(r"user=(.\S+)", l)
pd = re.findall(r"passwd=(.\S+)", l)
pt = re.findall(r"port=(.\S+)", l)
db = re.findall(r"database=(.\S+)", l)
#--------------------------登陆数据库验证用户-----------------------------------
def zc_rs():
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
button1 = tk.Button(chk_win, text='用户信息', font=('宋体', '18'), command=chk_user)
button1.grid(row=2, column=0, padx=50, pady=10, sticky='w')
button2 = tk.Button(chk_win, text='密码查询', font=('宋体', '18'), command=chk_pass)
button2.grid(row=3, column=0, padx=50, pady=10, sticky='w')
button3 = tk.Button(chk_win, text='注册人数', font=('宋体', '18'), command=zc_rs)
button3.grid(row=4, column=0, padx=50, pady=10, sticky='w')
label = tk.Label(chk_win, text='信息提示区', font=('宋体', '16'), relief = 'ridge', width = 15)
label.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky='s')
chk_win.mainloop()