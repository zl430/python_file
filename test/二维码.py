# _*_ coding:UTF-8 _*_
#二维码
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
# url = 'http://apis.juhe.cn/qrcode/api'
# key = 'key=31b87fdef2b197d7341fda94f06a2d7e'
# data = {"type": "1", "fgcolor": "00b7ee", "w": "90", "m": "5", "text": "123"}
# test = requests.post(url, key, data)
# print(test.text)
a = requests.post('http://apis.juhe.cn/qrcode/api?text=123&el=&bgcolor=ffffff&fgcolor=000000&logo=&w=300&m=10&lw=60&type=2&key=31b87fdef2b197d7341fda94f06a2d7e')
file = open('aaaaa.png', 'wb')
file.write(a.content)
print(file)
lena = mpimg.imread('aaaaa.png')
plt.imshow(lena)
plt.axis('off') # 不显示坐标轴
plt.show()
