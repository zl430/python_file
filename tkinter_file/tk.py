import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
e = tk.Entry(test,show='*')    #show='*' 输入字符显示为‘*’号，None（明文）显示输入字符
e.pack()
def insert_porint():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end',var)
b1 = tk.Button(test,text='insert_porint',width=15,height=1,command=insert_porint)
b1.pack()
b2 = tk.Button(test,text='insert_end',width=15,height=1,command=insert_end)
b2.pack()
t = tk.Text(test,height=2)
t.pack()
test.mainloop()

