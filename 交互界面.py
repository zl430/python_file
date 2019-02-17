
__author__ = 'freedom'
#import test
from tkinter import *
class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.lab1 = Label(frame,text = "User:")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(frame)
        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(frame,text = "Pass:")
        self.lab2.grid(row = 1,column = 0)
        self.ent2 = Entry(frame,show = "*")
        self.ent2.grid(row = 1,column = 1,sticky = W)
        self.button = Button(frame,text = "登陆",command = self.Submit)
        self.button.grid(row = 2,column = 1,sticky = E)
        self.button = Button(frame,text = "注册",command = self.Submit)
        self.button.grid(row = 2,column = 2,sticky = E)
        self.lab3 = Label(frame,text = "")
        self.lab3.grid(row = 3,column = 0,sticky = W)
        self.button2 = Button(frame,text = "退出",command = frame.quit)
        self.button2.grid(row = 3,column = 3,sticky = E)
    def Submit(self):
        s1 = self.ent1.get()
        s2 = self.ent2.get()
        if s1 == '' and s2 == '':
            self.lab3["test"] = "输入错误"
        else:
            if s1 == 'name' and s2 == 'passw':
                self.lab3["text"] = "登陆成功"
            else:
                self.lab3["text"] = "登陆失败"
            self.ent1.delete(0,len(s1))
            self.ent2.delete(0,len(s2))
root = Tk()
root.title("账户测试")
app = Reg(root)
root.mainloop()

'''


old = {}
new = {}
f = open('user.txt', 'r').readlines()
for line in f:
    (key, value) = line.strip().split(':')
    old[key] = value
print('---------------')
print('|注册新用户：1|')
print('---------------')
print('|用户登陆  ：2|')
print('---------------')
d = input('请输入序号：')
def user_new():
    name = input('请输入用户名：')
    if name == '':
        print('用户名不能为空')
    else:
        password1 = input('请输入密码：')
        chk = password1.isdigit()
        if chk == True:
            if password1 == '':
                print('密码不能为空')
            else:
                password2 = input('请再次输入密码：')
                if password1 == password2:
                    new[name] = password2
                    w = open('user.txt', 'a')
                    for (key,value) in new.items():
                        w.write('%s:%s\n' % (key, value))
                    print('用户注册成功')
                else:
                    print('两次密码不一致')
        else:
            print('请输入数字类型密码')
            user_new()
def user_old(name):
    password = input('请输入密码：')
    if password == '':
        print('密码不能为空')
        exit()
    else:
        if old[name] != password:
            conn = 1
            while conn < 3:
                password = input('密码错误，请重新输入：')
                if old[name] == password:
                    print('登陆成功')
                    exit()
                else:
                    if conn == 2:
                        print('密码错误，账户已锁定。')
                        v = open('user_new.txt', 'a')
                        v.write('%s\n' % name)
                        exit()
                    else:
                        conn += 1
        else:
            print('登陆成功')
            exit()
def user_check():
    name = input('请输入用户名：')
    if name == '':
        print('用户名不能为空')
        exit()
    else:
        file = open('user_new.txt', 'r').readlines()
        for i in file:
            print(i)
            print(name)
            if i == name:
                print('用户已锁定，暂时不能使用')
                exit()
            else:
                user_old(name)
if int(d) == 1:
    user_new()
elif int(d) == 2:
    user_check()


'''