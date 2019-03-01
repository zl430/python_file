import mysql.connector
class mysql_select():
    db = mysql.connector.connect(
        host='10.113.4.189',
        user='root',
        password='123456',
         port='66',
        database='py_test'
    )
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def user_select(self):
        db_sql = self.db.cursor()
        db_sql.execute('select * from py_table where name =' + self.name)
        results = db_sql.fetchall()
        self.db.close()
        if results != []:
            results = results[0]
            if results[0] == self.name and results[1] == self.password:
                return True
            else:
                return False
        else:
            return False
a = mysql_select('1', '123')
a.user_select()