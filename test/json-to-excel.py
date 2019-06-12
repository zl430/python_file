# import tkinter
# from tkinter import filedialog
# import os
# top = tkinter.Tk()
# top.geometry('600x200')
# top.wm_title('Json->TO->Excel')
# top.resizable(width=False, height=False)
# pwd_dir = os.getcwd()
# pwd_dir = pwd_dir.replace('\\', '\\\\')
# print(pwd_dir)
# def on_dir():
#     answer = filedialog.askdirectory(parent=top,
#                                  initialdir=os.getcwd(),
#                                  title="Please select a folder:")
#     label1['text'] = answer
#     return answer
# def to_dir():
#     answer = filedialog.askdirectory(parent=top,
#                              initialdir=os.getcwd(),
#                              title="Please select a folder:")
#     label2['text'] = answer
#     return answer
# def cmd():
#     pass
# #---------------------------------窗口主体---------------------------------------------
# label1 = tkinter.Label(top, text='表头数量:', font=('宋体', '18'))
# label1.grid(row=3, column=1, padx=0, pady=10, sticky='w')
# entry = tkinter.Entry(top, font=('宋体', '18'))
# entry.grid(row=3, column=1, padx=120, pady=10, sticky='w')
# button1 = tkinter.Button(top, text='选择目录', font=('宋体', '18'), command = on_dir)
# button1.grid(row=1, column=1, padx=480, pady=10, sticky='w')
# button2 = tkinter.Button(top, text='选择目录', font=('宋体', '18'), command = to_dir)
# button2.grid(row=2, column=1, padx=480, pady=10, sticky='w')
# button3 = tkinter.Button(top, text='生成', font=('宋体', '18'), command = cmd)
# button3.grid(row=3, column=1, padx=500, pady=10, sticky='w')
# label1 = tkinter.Label(top, text='excel文件目录', font=('华文新魏', '16'), relief = 'ridge', width = 40)
# label1.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='w')
# label2 = tkinter.Label(top, text='json文件目录', font=('华文新魏', '16'), relief = 'ridge', width = 40)
# label2.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='w')
# top.mainloop()
import json
file = open("C:\\Users\\zuolei\\Downloads\\BigSwordTreeList-NEW.json")
f = file.read()
f = json.loads(f)
f = json.dumps(f, indent=4)
print(f)
print(f['1']['weaponSequence'])
print(type(f))