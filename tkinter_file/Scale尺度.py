import tkinter as tk

test = tk.Tk()
test.title('my test')
test.geometry('200x150')
l =tk.Label(test, bg='yellow', width=15, text='请选择答案') #textvariable 传入文本字符
l.pack()
def qwe(v):
    l.config(text='您选的答案是： '+ v) #l.config 修改Labe中的参数,此处修改text参数值
s = tk.Scale(test, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200, showvalue=1, tickinterval=3, resolution=0.01, command=qwe) #ORIZONTAL 横向 、from默认可以直接使用，如果想把from作为普通值使用则写为 from_(from+下划线)
#showvalue=1 显示选择的值0为不显示1为显示, tickinterval=3三个长度显示一个单位, resolution=0.01保留两位小数,
s.pack()
test.mainloop()