import MySQLdb
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor


class MySQL():
    pool = None
    def __init__(self):
        self.conn = MySQL.getConn()
        self.cursor = self.conn.cursor()
    @staticmethod
    def getConn():
        if MySQL.pool is None:
            pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=1,
                            host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPWD,
                            db=Config.DBNAME, use_unicode=False, charset=Config.DBCHAR, cursorclass=DictCursor)

        return pool.connection()
    def getAll(self, sql, param=None):
        if param is None:
            count = self.cursor.execute(sql)
        else:
            count = self.cursor.execute(sql, param)
        if count > 0:
            result = self.cursor.fetchall()
        else:
            result = False
        return result
    def getOne(self, sql, param=None):
        if param is None:
            count = self.cursor.execute(sql)
        else:
            count = self.cursor.execute(sql, param)
        if count > 0:
            result = self.cursor.fetchone()
        else:
            result = False
        return result
    def getMany(self, sql, num, param=None):
        if param is None:
            count = self.cursor.execute(sql)
        else:
            count = self.cursor.execute(sql, param)
        if count > 0:
            result = self.cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertOne(self, sql, value):
        self.cursor.execute(sql, value)
        return self.__getInsertId()
    def insertMany(self, sql, values):
        count = self.cursor.executemany(sql, values)
        return count

    def __getInsertId(self):
        self.cursor.execute("SELECT @@IDENTITY AS id")
        result = self.cursor.fetchall()
        return result[0]['id']

    def __query(self, sql, param=None):
        if param is None:
            count = self.cursor.execute(sql)
        else:
            count = self.cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):
        return self.__query(sql,param)

    def delete(self, sql, param=None):
        return self.__query(sql, param)

    def begin(self):
        self.conn.autocommit(0)
    def end(self, option='commit'):
        if option == 'commit':
            self.conn.commit()
        else:
            self.conn.rollback()
    def dispose(self, isEnd=1):
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self.cursor.close()
        self.conn.close()
#
# pool = PooledDB(MySQLdb, 5, host='10.113.4.189', user='root', passwd='123456', db='py_test', port=66)
# def test():
#     try:
#         # 调用连接池
#         conn = pool.connection()
#         cur = conn.cursor()
#         sql = "select * from py_table"
#         cur.execute(sql)
#         result = cur.fetchall()
#         params = []
#         for row in result:
#             params.append((row[0], row[1], row[2]))
#         print(params)
#     except IOError:
#         conn.rollback() # 出现异常 回滚事件
#         print("Error: Function happen Error: test()")
#     finally:
#         print("释放资源，test，")
#         cur.close()
#         conn.close()
# test()