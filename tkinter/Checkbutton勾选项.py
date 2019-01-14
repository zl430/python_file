import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
l =tk.Label(test, bg='yellow', width=15, text='请选择答案') #textvariable 传入文本字符
l.pack()
def qwe():
    if(var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love pyhton')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love shell')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(test, text='python', variable=var1, onvalue=1, offvalue=0, command=qwe)
c2 = tk.Checkbutton(test, text='shell', variable=var2, onvalue=1, offvalue=0, command=qwe)
c1.pack()
c2.pack()
test.mainloop()