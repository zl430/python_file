# -*- coding=utf-8 -*-
from PIL import Image
im = Image.open('aa.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w*2, h*2))
print('Original image size: %sx%s' % (w*2, h*2))
im.save('thumbnail.jpg', 'jpeg')

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def rndChar():
    return chr(random.randint(65,90))
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (0, 0, 205))
font = ImageFont.truetype('aa.ttf', 35)
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')