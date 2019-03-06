 #coding:utf-8
from requrst import mysql_connection_pool
from _sqlite3 import Row
#申请资源
class connection():
    mysql = mysql_connection_pool.MySQL()
    def __init__(self, username, password, mail):
        self.name = username
        self.password = password
        self.mail = mail
    def login(self):
        sql = "select * from py_table where name = %s  AND password = %s" % (self.name, self.password)
        result = self.mysql.getAll(sql)
        if result:
            return True
    def create(self):
        sql = "INSERT INTO py_table (name, password, mail) VALUES (%s, %s, %s)"
        val = [
            "(%s, %s, %s)" % (self.name, self.password, self.mail)
        ]
        result = self.mysql.insertOne(sql=sql, value=val)
        print(result)
        if result:
            return True
    mysql.dispose()