# -*- coding: utf-8 -*-  
# import numpy as np
import matplotlib.pyplot as plt  
#X轴，Y轴数据  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.figure(figsize=(8, 8)) #创建绘图对象
plt.plot(x, y, "b--", linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Time(s)") #X轴标签  
plt.ylabel("Volt")  #Y轴标签  
plt.title("Line plot") #图标题  
plt.show()  #显示图  
plt.savefig("line.jpg") #保存图  
