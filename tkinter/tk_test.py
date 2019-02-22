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
name.set('xxxxxx@xxxxx.com')
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
def usr_up():
    def ser_up_to_db():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('user.info.pickle','rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if np != npf:
            tk.messagebox.showerror(title='错误',message='密码输入有误')
        elif nn in exist_user_info:
            tk.messagebox.showerror(title='错误',message='该用户不能使用')
        else:
            exist_user_info[nn] = np
            with open('user_info.pickle','wb') as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo('注册成功')
            test_ser_up.destroy()
    test_ser_up = tk.Toplevel(test) #tk.Toplevel 窗口上的窗口
    test_ser_up.geometry('300x300')
    test_ser_up.title('欢迎注册')
    new_name = tk.StringVar()
    new_name.set('xxxxxxx@xxxxxxx.com')
    tk.Label(test_ser_up,text='username:').place(x=45,y=50)
    entry_new_name= tk.Entry(test_ser_up,textvariable=new_name)
    entry_new_name.place(x=115,y=50)
    new_pwd = tk.StringVar()
    tk.Label(test_ser_up,text='password:').place(x=45,y=90)
    entry_new_pwd= tk.Entry(test_ser_up,textvariable=new_pwd,show='*')
    entry_new_pwd.place(x=115,y=90)
    new_pwd_confirm = tk.StringVar()
    tk.Label(test_ser_up,text='password:').place(x=45,y=130)
    entry_usr_pwd_confirm = tk.Entry(test_ser_up,text=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=115,y=130)
    btn_comfirm_usr_up = tk.Button(test_ser_up,text='ser_up',command=ser_up_to_db)
    btn_comfirm_usr_up.place(x=150,y=150)
    btn_comfirm_usr_up.pack()
btn_login = tk.Button(test,text='登陆',command=usr_login).place(x=135,y=250)
# btn_up = tk.Button(test,text='注册',command=usr_up).place(x=270,y=250)
btn_up = tk.Button(test,text='联系管理员',command=usr_up).place(x=270,y=250)
test.mainloop()