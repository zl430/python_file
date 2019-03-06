# encoding=utf-8
import tkinter as tk
from tkinter import ttk
dns_add = tk.Tk()
dns_add.title('dnspod记录添加')
dns_add.geometry('800x200')
dns_add.resizable(width=False, height=False)
def dns_del_jl():
    dns_id = entry_del1.get()
    dns_name = entry_del2.get()
    dns_value = entry_del3.get()
    if dns_id != "" and dns_name != "" and dns_value:
        from API import dnspod_add
        dnspod_add.dns_del(dns_id, dns_name, dns_value)
        label['text'] = '删除成功'
    else:
        label['text'] = '不允许为空值'
def dns_add_jl():
    dns_id = entry_add1.get()
    dns_name = entry_add2.get()
    dns_value = entry_add3.get()
    if dns_id != "" and dns_name != "" and dns_value:
        from API import dnspod_class
        ad = dnspod_class.dnspod_api_chk(dns_id, dns_name, dns_value)
        over = ad.dns_add()
        if over == True:
            label['text'] = '添加成功'
            print('添加成功')
        else:
            label['text'] = '添加失败,错误代码' + over
            print('添加失败')
    else:
        label['text'] = '不允许为空值'
# tree = ttk.Treeview(dns_add)
label = tk.Label(dns_add, text='信息提示区', font=('华文新魏', '16'), relief = 'ridge', width = 25)
label.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='w')
# button1 = tk.Button(dns_add, text='用户查询', command=user_chk)
# button1.grid(row=2, column=0, padx=15, pady=10, sticky='w')
# button2 = tk.Button(dns_add, text='密码查询', command=pass_chk)
# button2.grid(row=2, column=0, padx=115, pady=10, sticky='s')
#-------------------------添加记录------------------------
label_add1 = tk.Label(dns_add, text='domain_id:', font=('宋体', '18'))
label_add1.grid(row=1, column=1, padx=0, pady=10, sticky='w')
label_add2 = tk.Label(dns_add, text='name:', font=('宋体', '18'))
label_add2 .grid(row=1, column=1, padx=245, pady=10, sticky='w')
label_add3 = tk.Label(dns_add, text='value:', font=('宋体', '18'))
label_add3 .grid(row=1, column=1, padx=435, pady=10, sticky='w')
entry_add1 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_add1.grid(row=1, column=1, padx=120, pady=10, sticky='w')
entry_add2 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_add2.grid(row=1, column=1, padx=310, pady=10, sticky='w')
entry_add3 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_add3.grid(row=1, column=1, padx=510, pady=10, sticky='w')
button_add2 = tk.Button(dns_add, text='添加', command=dns_add_jl)
button_add2.grid(row=1, column=1, padx=650, pady=10, sticky='s')
#------------------------删除记录------------------------
label_del1 = tk.Label(dns_add, text='domain_id:', font=('宋体', '18'))
label_del1.grid(row=2, column=1, padx=0, pady=10, sticky='w')
label_del2 = tk.Label(dns_add, text='name:', font=('宋体', '18'))
label_del2 .grid(row=2, column=1, padx=245, pady=10, sticky='w')
label_del3 = tk.Label(dns_add, text='value:', font=('宋体', '18'))
label_del3 .grid(row=2, column=1, padx=435, pady=10, sticky='w')
entry_del1 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_del1.grid(row=2, column=1, padx=120, pady=10, sticky='w')
entry_del2 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_del2.grid(row=2, column=1, padx=310, pady=10, sticky='w')
entry_del3 = tk.Entry(dns_add, font=('宋体', '18'), width = 10)
entry_del3.grid(row=2, column=1, padx=510, pady=10, sticky='w')
button_del2 = tk.Button(dns_add, text='删除', command=dns_del_jl)
button_del2.grid(row=2, column=1, padx=650, pady=10, sticky='s')
dns_add.mainloop()