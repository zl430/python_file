import mysql.connector

mydb = mysql.connector.connect(
  host="123.206.96.37",       # 数据库主机地址
  user="python",    # 数据库用户名
  passwd="zuolei@123.",  # 数据库密码
  port="3306"
)
mycursor = mydb.cursor()    #创建游标
mycursor.execute("create database py_user")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
mycursor.execute("use py_user")
mycursor.execute("create table py_user_table (name VARCHAR (255),password VARCHAR (255))")
# sql = "INSERT INTO py_table (name, password) VALUES (%s, %s)"
# val = [
#   ('11', '123456')
# ]
# mycursor.execute(sql,val) #执行一条sql
# mycursor.executemany(sql, val) #批量执行多条sql
mydb.commit()   #更新数据表
print(mycursor.rowcount, "记录插入成功。")