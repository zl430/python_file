import re
import mysql.connector
class select_sql():
    def ljzc(self, mydb):
        ##累计注册人数
        mycursor = mydb.cursor()
        mycursor.execute()
        sql1 = "select COUNT(userId),channelId  from register_log GROUP BY channelId;"
    def xzsb(self, mydb):
        ##累计新增设备
        mycursor = mydb.cursor()
        mycursor.execute()
        sql = "select COUNT(distinct(imei)),channelId from register_log GROUP BY channelId;"
    file = open('E:/Git/file/python_file/db_mysql.conf', 'r')
    f = file.readlines()
    l = " ".join(f)
    ip = re.findall(r"host=(.\S+)", l)
    us = re.findall(r"user=(.\S+)", l)
    pd = re.findall(r"passwd=(.\S+)", l)
    pt = re.findall(r"port=(.\S+)", l)
    db = re.findall(r"database=(.\S+)", l)
#--------------------------登陆数据库验证用户-----------------------------------
    mydb = mysql.connector.connect(
        host=str(ip[0]),   # 数据库主机地址a
        user=str(us[0]),    # 数据库用户名
        passwd=str(pd[0]),  # 数据库密码
        port=str(pt[0]),
        database="game_test"
    )
a=select_sql.ljzc()
print(a)
