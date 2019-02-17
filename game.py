"""
@Author: 舍名利
@Blog  : www.cnblogs.com/shemingli
@GitHub: github.com/GratefulHeartCoder
@Date  : 2018/4/2
"""
import tkinter as tk
 
 
def main():
    app = tk.Tk()  # 实例化一个Tk 用于容纳整个GUI程序
    app.title('shemingli')  # 设置窗体的标题栏
 
    # 设置label主键，显示文本，图标与图片
    the_label = tk.Label(app, text="这是一个窗口程序................................\n......................\n............................\n......................\n......................................................")
 
    the_label.pack()  # 自动调节 主键的尺寸与位置
 
    # 窗口的主事件循环。由tkinter接管
    app.mainloop()
 
 
if __name__ == '__main__':
    main()