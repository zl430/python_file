# coding:utf-8
import mysql_connection_pool
#申请资源
class connection():
    mysql = mysql_connection_pool.MySQL()
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.check_user_sql = "select username from user where username = \"%s\"" % self.name
        self.check_user_pass_sql = "select * from user where username = \"%s\" AND password = %s AND available = \"Y\"" % (self.name, self.password)
        self.check_user_available_sql = "select available from user where username = \"%s\"" % self.name
        self.registered_user_sql = '''INSERT INTO user (username, password) VALUES (\"%s\", \"%s\")''' % (self.name, self.password)
    def login(self):
        check_user = self.mysql.getOne(self.check_user_sql)
        if check_user == False or check_user is None:
            return 'nouser'
        elif check_user != None or check_user != False:
            check_suer_pass = self.mysql.getAll(self.check_user_pass_sql)
            if check_suer_pass == False:
                check_suer_available = self.mysql.getOne(self.check_user_available_sql)
                result = check_suer_available['available']
                if result == b'N':
                    return 'N'
            elif check_suer_pass:
                return True
            self.mysql.dispose()
    def create(self):
        check_user = self.mysql.getOne(self.check_user_sql)
        if check_user == False or check_user is None:
            print(self.registered_user_sql)
            registered = self.mysql.insertOne(self.registered_user_sql)
            self.mysql.dispose()
            if registered == 1:
                return True
        else:
            self.mysql.dispose()
            return False
        self.mysql.dispose()