import mysql.connector

mydb = mysql.connector.connect(
  host="117.50.64.186",       # 数据库主机地址
  user="admin",    # 数据库用户名
  passwd="123456",  # 数据库密码
  port="3306"
)
mycursor = mydb.cursor()    #创建游标
# mycursor.execute("create database py_test")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
mycursor.execute("use py_test")
mycursor.execute("create table py_table (hostip VARCHAR (20),hostname VARCHAR (50), cpu VARCHAR (10))")
# sql = "INSERT INTO py_table (name, password, mail) VALUES (%s, %s, %s)"
# val = [
#     ('4', '123', '123@qq.com')
# ]
# name = '5'
# password = '123'
# mail = '123@qq.com'
# sql = '''INSERT INTO py_table (name, password, mail) VALUES (%s, %s, "%s")''' % (name, password, mail)
# print(sql)
# mycursor.execute(sql) #执行一条sql
# mycursor.executemany(sql, val) #批量执行多条sql
mydb.commit()   #更新数据表
print(mycursor.rowcount, "记录插入成功。")