import tkinter
from tkinter import filedialog
import os
top = tkinter.Tk()
top.geometry('600x200')
top.wm_title('Excel->TO->json')
top.resizable(width=False, height=False)
pwd_dir = os.getcwd()
pwd_dir = pwd_dir.replace('\\', '\\\\')
print(pwd_dir)
def on_dir():
    answer = filedialog.askdirectory(parent=top,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:")
    label1['text'] = answer
    return answer
def to_dir():
    answer = filedialog.askdirectory(parent=top,
                             initialdir=os.getcwd(),
                             title="Please select a folder:")
    label2['text'] = answer
    return answer
def cmd():
    header = entry.get()
    on = label1['text']
    to = label2['text']
    on = on.replace('/', '\\')
    to = to.replace('/', '\\')
    for parent, dirnames, filenames in os.walk(on):
        for filename in filenames:
            print(filename)
            name = os.path.splitext(filename)[0]
            # os.chdir("D:\\test")
            print(pwd_dir)
            # sysStr = "C:\\Users\\zuolei\\Desktop\\表文件\\excel2json\\excel2json.exe --excel "+on+'\\' +filename+"  --json " +to+'\\' + name+'.json'+" --header " + header
            sysStr = pwd_dir+'\\excel2json.exe --excel ' + on+'\\' + filename+"  --json " + to+'\\' + name+'.json'+ " --header " + header
            print(sysStr)
            os.system(sysStr)
#---------------------------------窗口主体---------------------------------------------
label1 = tkinter.Label(top, text='表头数量:', font=('宋体', '18'))
label1.grid(row=3, column=1, padx=0, pady=10, sticky='w')
entry = tkinter.Entry(top, font=('宋体', '18'))
entry.grid(row=3, column=1, padx=120, pady=10, sticky='w')
button1 = tkinter.Button(top, text='选择目录', font=('宋体', '18'), command = on_dir)
button1.grid(row=1, column=1, padx=480, pady=10, sticky='w')
button2 = tkinter.Button(top, text='选择目录', font=('宋体', '18'), command = to_dir)
button2.grid(row=2, column=1, padx=480, pady=10, sticky='w')
button3 = tkinter.Button(top, text='生成', font=('宋体', '18'), command = cmd)
button3.grid(row=3, column=1, padx=500, pady=10, sticky='w')
label1 = tkinter.Label(top, text='excel文件目录', font=('华文新魏', '16'), relief = 'ridge', width = 40)
label1.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='w')
label2 = tkinter.Label(top, text='json文件目录', font=('华文新魏', '16'), relief = 'ridge', width = 40)
label2.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='w')
top.mainloop()