import requests
import tkinter as tk
import sys
class index():
    def d(self):
        pass
        # name = entry1.get()
        # password = entry2.get()
        # url = 'http://127.0.0.1:66/login'
        # data = {'username': name, 'password': password}
        # over = requests.post(url, data, timeout=30)
        # a = over.text
        # if a == '1':
        #     label3['text'] = '登陆成功'
        # else:
        #     label3['text'] = '登陆失败'
    def z(self):
        pass
        # name = entry1.get()
        # password = entry2.get()
        # url = 'http://127.0.0.1:66/login'
        # data = {'username': name, 'password': password}
        # over = requests.post(url, data, timeout=30)
        # a = over.text
        # if a == '1':
        #     label3['text'] = '登陆成功'
        # else:
        #     label3['text'] = '登陆失败'
    def login(self):
        win = tk.Tk()
        win.title('requessts')
        win.geometry('400x200')
        win.resizable(width=False, height=False)
        label1 = tk.Label(win, text='用户名:', font=('宋体', '18'))
        label1.grid(row=0, column=0)
        label2 = tk.Label(win, text='密  码:', font=('宋体', '18'))
        label2 .grid(row=1, column=0)
        entry1 = tk.Entry(win, font=('宋体', '18'))
        entry1.grid(row=0, column=1)
        entry1.focus_force()
        entry2 = tk.Entry(win, font=('宋体', '18'), show = '*')
        entry2.grid(row=1, column=1)
        button1 = tk.Button(win, text='登陆', font=('宋体', '18'), command = self.d)
        button1.grid(row=3, column=0, padx=50, pady=10)
        button2 = tk.Button(win, text='注册', font=('宋体', '18'), command = sys.exit)
        button2.grid(row=3, column=1, padx=80, pady=10)
        label3 = tk.Label(win, text='信息提示区', font=('华文新魏', '16'), relief = 'ridge', width = 30)
        label3.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='s')
        win.mainloop()
a = index
a.login()