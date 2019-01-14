import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
l =tk.Label(test, bg='yellow', text='')
l.pack()
counter = 0
def qwe():
    global counter
    l.config(text='do'+ str(counter))
    counter+=1
menubar = tk.Menu(test)
filemenu =tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=qwe)
filemenu.add_command(label='Open', command=qwe)
filemenu.add_command(label='Save', command=qwe)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=test.quit)
test.config(menu=menubar)
test.mainloop()