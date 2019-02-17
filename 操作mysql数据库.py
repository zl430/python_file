__author__ = 'Golden'
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
 
# 创建连接
conn = pymysql.connect(host='192.168.0.113',port=3306,user='root',passwd='123456',db='mysql')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回受影响行数
effect_row = cursor.execute("create database test2;")
'''
print(effect_row)
# 取出一条数据
print(cursor.fetchone())
# 取出前n条数据
print("*********************************************************")
print(cursor.fetchmany(5))
# 取出所有数据
print("*********************************************************")
print(cursor.fetchall())
'''
# 提交，不然无法保存新建或修改的数据
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()