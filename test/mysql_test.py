import mysql.connector

mydb = mysql.connector.connect(
  host="10.113.4.189",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456",  # 数据库密码
  port="66"
)
mycursor = mydb.cursor()    #创建游标
# mycursor.execute("create database bbb")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
mycursor.execute("use py_test")
# mycursor.execute("create table py_table (name VARCHAR (255),password VARCHAR (255), mail VARCHAR (255))")
# sql = "INSERT INTO py_table (name, password, mail) VALUES (%s, %s, %s)"
# val = [
#     ('4', '123', '123@qq.com')
# ]
name = '5'
password = '123'
mail = '123@qq.com'
sql = '''INSERT INTO py_table (name, password, mail) VALUES (%s, %s, "%s")''' % (name, password, mail)
print(sql)
mycursor.execute(sql) #执行一条sql
# mycursor.executemany(sql, val) #批量执行多条sql
mydb.commit()   #更新数据表
print(mycursor.rowcount, "记录插入成功。")