import mysql.connector

mydb = mysql.connector.connect(
  host="10.113.4.189",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="123456",  # 数据库密码
  port="66"
)
mycursor = mydb.cursor()    #创建游标
# mycursor.execute("create database bbb")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
mycursor.execute("use py_test")
mycursor.execute("create table py_table (name VARCHAR (255),password VARCHAR (255))")
# sql = "INSERT INTO py_table (name, password) VALUES (%s, %s)"
# val = [
#   ('11', '123456')
# ]
# mycursor.execute(sql,val) #执行一条sql
# mycursor.executemany(sql, val) #批量执行多条sql
mydb.commit()   #更新数据表
print(mycursor.rowcount, "记录插入成功。")