# -*- coding: utf-8 -*-
from tkinter import *


def main():
    #创建tk对象
    tk=Tk()
    #创建画布
    canvas=Canvas(tk,width=300,height=100)
    canvas.pack()
    #在画布上创建文字
    canvas.create_text(150,50,text="welcome to Tkinter",fill="red",font=("Times",20))
    '''
    #在画布上创建图片，tkinter只能显示gif文件
    myImage=PhotoImage(file="timg.gif")
    canvas.create_image(10,70,anchor=NW,image=myImage)#以(10,70)为西北角显示图像

    #move中的第一个参数表示移动canvas里的第几个对象
    def moverectangle(event):
        if event.keysym == "Up":
            canvas.move(3,0,-5)
        elif event.keysym=="Down":
            canvas.move(3,0,5)
        elif event.keysym=="Left":
            canvas.move(3,-5,0)
        elif event.keysym=="Right":
            canvas.move(3,5,0)
        else:
            canvas.move(3,5,5)

    canvas.create_rectangle(200,200,220,220,fill="red")
    #让tkinter监视KeyPress事件，当该事件发生时调用moverectangle函数
    #bind_all第2个参数是回调函数，不能接收参数传递，所以在函数内部建立回调函数
    canvas.bind_all("<KeyPress-Up>",moverectangle)
    canvas.bind_all("<KeyPress-Down>", moverectangle)
    canvas.bind_all("<KeyPress-Left>",moverectangle)
    canvas.bind_all("<KeyPress-Right>", moverectangle)
    canvas.bind_all("<KeyPress-Return>",moverectangle)
    '''

    tk.mainloop()
main()