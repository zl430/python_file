import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
l =tk.Label(test, bg='yellow', width=15, text='请选择答案') #textvariable 传入文本字符
l.pack()
def qwe():
    l.config(text='您选的答案是： '+ var.get()) #l.config 修改Labe中的参数,此处修改text参数值
var = tk.StringVar()
r1 = tk.Radiobutton(test,text='A：is a',variable=var,value='A',command=qwe)
r1.pack()
r2 = tk.Radiobutton(test,text='B：is b',variable=var,value='B',command=qwe)
r2.pack()
r3 = tk.Radiobutton(test,text='C：is c',variable=var,value='C',command=qwe)
r3.pack()
test.mainloop()

