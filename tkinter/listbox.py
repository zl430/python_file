import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
var1 = tk.StringVar()

l =tk.Label(test,bg='yellow',width=4,textvariable=var1) #textvariable 传入文本字符
l.pack()
def insert():
    value =lb.get(lb.curselection())#curselection 光标指定位置
    var1.set(value)

b1 = tk.Button(test,text='insert',width=15,height=1,command=insert)
b1.pack()
var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(test,listvariable=var2)  #listvariable 传入列表
lb.pack()
test.mainloop()

