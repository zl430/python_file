# -*- coding:utf-8 -*-
from subprocess import Popen,PIPE
import re
import os,sys
import mysql.connector
import json
import paramiko
import psutil
# class MySql():
#     def conn(self):
#         mydb = mysql.connector.connect(
#         host="117.50.64.186",       # 数据库主机地址
#         user="admin",    # 数据库用户名
#         passwd="123456",  # 数据库密码
#         port="3306"
#         )
# mycursor = mydb.cursor()    #创建游标
# mycursor.execute("create database py_test")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
# mycursor.execute("use py_test")
# mycursor.execute("create table py_table (hostip VARCHAR (20),hostname VARCHAR (50), cpu VARCHAR (10))")
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
# mydb.commit()   #更新数据表
# print(mycursor.rowcount, "记录插入成功。")
class GetLinuxMessage():
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
    def session(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, int(self.port), self.username, self.password)
            print("Login %s is successful" % self.host)
            # stdin, stdout, stderr = ssh.exec_command('hostname')
            result = psutil.cpu_times(percpu=True)
            # print(hostname)
            # result = stdout.read()
            # result = str(result, encoding='utf-8')
            ssh.close()
            return result
            # return ssh
        except Exception as e:
            print(e.message)
    # def get_hostname(self):
    #     cmd_hostname = "hostname"
    #     client = self.session(self.host, int(self.port), self.username, self.password)
    #     stdin, stdout, stderr = client.exec_command(cmd_hostname)
    #     hostname = stdout.read()
    #     return hostname
    # def get_ifconfig(self):
    #     client = self.session(self.host, int(self.port), self.username, self.password)
    #     stdin, stdout, stderr = client.exec_command("ifconfig")
    #     data = stdout.read()
    #     ret = re.compile('(?:19[0-9]\.)((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){2}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
    #     match = ret.search(data).group()
    #     return match
ssh_client = GetLinuxMessage('117.50.64.186', '22', 'root', '`1234qwer')
over = ssh_client.session()
print(over)
# if over == str('login_successful'):
# ssh_client.get_hostname()

