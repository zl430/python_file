import xlwt
a = []
f = open('E:/python/pycharm/PyCharm 4.0.4/file/test.txt', 'r' , 'gbk')
line = f.readline()
for i in line:
    a.append(line.strip())

'''
#只能写不能读
stus = [['姓名', '年龄', '性别', '分数'],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9]
        ]
'''
book = xlwt.Workbook()#新建一个excel
sheet = book.add_sheet('case1_sheet')#添加一个sheet页
row = 0#控制行
for stu in a:
    col = 0#控制列
    for s in stu:#再循环里面list的值，每一列
        sheet.write(row,col,s)
        col+=1
    row+=1
book.save('E:/python/pycharm/PyCharm 4.0.4/file/test.xls')#保存到当前目录下
