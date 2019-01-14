import os
'''
#目录操作
t = os.getcwd()
print(t)
dir = os.path.join(t, "a.py")
print(os.listdir(t))
print(os.path.isdir(dir))
print(os.path.isfile(dir))

a = "E:/CRT"
print(a)
print(os.path.isdir(a))

#截屏
from PIL import ImageGrab
a = "E:\CRT"
im=ImageGrab.grab()
im.save(a,'a', 'jpeg')
'''
import  unittest
import  math
class TestMath(unittest.TestCase):
    def setUp(self):
        pass
    def test_add(self):
        result = math.add(5,7)
        self.assertEqual(result,11,"error")
    def tearDown(self):
        pass
w=TestMath()
print(w.test_add())