import tkinter as tk
import tkinter.messagebox #引用子模块
test = tk.Tk()
test.title('my test')
test.geometry('200x150')
def cs():
    # tk.messagebox.showinfo(title='Hi', message='aaaaaaaaa')
    # tk.messagebox.showwarning(title='Hi', message='bbbbbbbbb')
    # tk.messagebox.showerror(title='Hi', message='error')                 #showinfo   showwarning   showerror  功能类似，图标不一样
     print(tk.messagebox.askquestion(title='Hi', message='aaaaaaaaa'))           #askquestion 返回值   return 'yes' or  'no'
    # print(tk.messagebox.askyesno(title='Hi', message='aaaaaaaaa'))         #askyesno   返回值   return   True,False
    # print(tk.messagebox.askokcancel(title='Hi', message='aaaaaaaaa'))     #同 askquestion

tk.Button(test, text='弹窗测试', command=cs).pack()
test.mainloop()