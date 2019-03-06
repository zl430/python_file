import tkinter
import sys
import re
import mysql.connector
top = tkinter.Tk()
top.geometry('400x170+350+150')
top.wm_title('综合实例')
top.resizable(width=False, height=False)
def validateText():
    val = entry1.get()
    pwd = entry2.get()
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
# def anw_button():
def anw_button(db_host=ip[0], db_user=us[0], db_pass=pd[0], db_port=pt[0], db_data=db[0]):
    '''
    mydb = mysql.connector.connect(
        host="10.113.4.189",       # 数据库主机地址
        user="root",    # 数据库用户名
        passwd="123456",  # 数据库密码
        port="66",
        database="py_test"
    )
    '''
    db_user_name = entry1.get()
    mydb = mysql.connector.connect(
        host=str(db_host),   # 数据库主机地址a
        user=str(db_user),    # 数据库用户名
        passwd=str(db_pass),  # 数据库密码
        port=str(db_port),
        database=str(db_data)
    )
    mycursor = mydb.cursor()    #创建游标
    # mycursor.execute("select * FROM py_table;")
    mycursor.execute("select * FROM py_table where name =  " + db_user_name)
    results = mycursor.fetchall()
    if results[0][0] != "":
        db_user_pwd = results[0][1]
        if str.upper(entry1.get()) == db_user_name and str.upper(entry2.get()) == db_user_pwd:
            label3['text'] = '登陆成功'
            top.destroy()   #停止运行top.mainloop()，关闭窗口
            import dnspod_login_add
            dnspod_login_add
        else:
            label3['text'] = '用户名或密码错误，请重新输入！'
def registered():
    top.destroy()
    import zc
    zc
def down_zc():
    label3['text'] = '注册功能已关闭'
#---------------------------------窗口主体---------------------------------------------
label1 = tkinter.Label(top, text='用户名:', font=('宋体', '18'))
label1.grid(row=0, column=0)
label2 = tkinter.Label(top, text='密码:', font=('宋体', '18'))
label2 .grid(row=1, column=0)
v = tkinter.StringVar()
entry1 = tkinter.Entry(top, font=('宋体', '18'), textvariable = v, validate = 'focusout', validatecommand = validateText)

entry1.grid(row=0, column=1)
entry1.focus_force()
entry2 = tkinter.Entry(top, font=('宋体', '18'), show = '*')

entry2.grid(row=1, column=1)
button1 = tkinter.Button(top, text='登陆', font=('宋体', '18'), command = anw_button)
button1.grid(row=2, column=0, padx=50, pady=10)
# button2 = tkinter_file.Button(top, text='注册', font=('宋体', '18'), command = sys.exit)
button2 = tkinter.Button(top, text='注册', font=('宋体', '18'), command = registered)
button2.grid(row=2, column=1, padx=80, pady=10)
label3 = tkinter.Label(top, text='信息提示区', font=('华文新魏', '16'), relief = 'ridge', width = 30)
label3.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='s')
top.mainloop()