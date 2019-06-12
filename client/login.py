import tkinter
import requests
import re
top = tkinter.Tk()
top.geometry('400x170+350+150')
top.wm_title('综合实例')
top.resizable(width=False, height=False)
def validateText():
    val = entry1.get()
    if re.findall('^[0-9a-zA-Z_]{1,}$', str(val)):
        return True
    else:
        label3['text'] = '用户名只能包含字母、数字、下划线'
        return False
#-----------------------------------------------------------
def anw_button():
        name = entry1.get()
        password = entry2.get()
        url = 'http://127.0.0.1:66/login'
        # url = 'http://117.50.24.60:66/login'
        data = {'username': name, 'password': password}
        over = requests.post(url, data)
        print(url, data)
        a = over.text
        if a == '1':
            label3['text'] = '登陆成功'
            # top.destroy()
        elif a == '2':
            label3['text'] = '账户已锁定'
        elif a == '0':
            label3['text'] = '账户不存在'
        else:
            label3['text'] = '登陆失败'
def registered():
    top.destroy()
    import create_user
    create_user
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