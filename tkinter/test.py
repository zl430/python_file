import tkinter as tk
import pickle
import tkinter.messagebox #引用子模块
test = tk.Tk()
test.title('管理终端测试页面')
test.geometry('470x350')
canvas = tk.Canvas(test,height=150,width=470)
image_file = tk.PhotoImage(file='hy.png')
image =canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')
tk.Label(test,text='username:').place(x=105,y=160)
tk.Label(test,text='password:').place(x=105,y=200)
name = tk.StringVar()
# name.set('xxxxxx@xxxxx.com')
entry_usr_name = tk.Entry(test,textvariable=name).place(x=190,y=160)
password = tk.StringVar()
entry_usr_pass = tk.Entry(test,textvariable=password,show='*').place(x=190,y=200)
def usr_login():
    user_name=name.get()
    user_pwd =password.get()
    try:
        with open('user_info.pickle','rb') as user_file:
            user_info=pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as user_file:
            user_info={'admin':'admin'}
            pickle.dump(user_info,user_file)
    if user_name in user_info:
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo(title='欢迎登陆', message='登陆成功'+ user_name)
        else:
            tk.messagebox.showerror(title='错误', message='登陆失败')
    else:
        u_up = tk.messagebox.askyesno(message='没有可用的用户，是否注册')
        if u_up:
            usr_up()
test.mainloop()