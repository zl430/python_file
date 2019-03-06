# coding:utf-8
import mysql_connection_pool
#申请资源
class connection():
    mysql = mysql_connection_pool.MySQL()
    def __init__(self, username, password, mail):
        self.name = username
        self.password = password
        self.mail = mail
    def login(self):
        sql = "select * from py_table where name = %s AND password = %s" % (self.name, self.password)
        result = self.mysql.getAll(sql)
        if result == False:
            return False
        elif result:
            return True
        self.mysql.dispose()
    def create(self):
        user_select = {}
        sql = "select name from py_table where name = %s" % self.name
        result = self.mysql.getOne(sql)
        if result is None:
            sql = '''INSERT INTO py_table (name, password, mail) VALUES (%s, %s, "%s")''' % (self.name, self.password, self.mail)
            result = self.mysql.insertOne(sql)
            if result == 1:
                return True
        else:
            return False
        self.mysql.dispose()