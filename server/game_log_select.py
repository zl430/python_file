# coding:utf-8
import mysql_connection_pool
#申请资源
class connection():
    mysql = mysql_connection_pool.MySQL("game_log")
    def __init__(self, date1, date2, open_date):
        self.date1 = date1
        self.date2 = date2
        self.open_date = open_date
    #存值总额
    def cz(self):
        sql = "select SUM(pay_amt) FROM recharge_log WHERE gameServerId=201"
        result = self.mysql.getAll(sql)
        if result == False:
            return False
        elif result:
            return result
        self.mysql.dispose()
    #留存
    def huoyue(self):
        sql = "SELECT COUNT(distinct(a.userId)), a.channelId from login_log a,register_log b  where a.logtype =1 and a.creattime >='%s' and a.creattime<'%s' and a.playerId=b.playerId and b.creattime< '%s' GROUP BY a.channelId ;" % (self.date1, self.date2, self.open_date)
        result = self.mysql.insertOne(sql)
        if result is None:
            return result
        else:
            return False
        self.mysql.dispose()