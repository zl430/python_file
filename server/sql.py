#coding:utf-8
#---------------------登陆用户sql------------------------
#检查登陆用户是否存在
check_user_sql = "select username from user where username = \"%s\""
#检查登陆用户可用性
check_user_pass_sql = "select * from user where username = \"%s\" AND password = %s AND available = \"Y\""
#登陆用户可用性校验
check_user_available_sql = "select available from user where username = \"%s\""
#注册登陆用户
registered_user = '''INSERT INTO user (username, password) VALUES (\"%s\", \"%s\")'''
#--------------------服务器信息sql------------------------
#查询主机
check_host_sql = "select * from host_table where host = \"%s\""
#添加主机
inster_host_sql = '''INSERT INTO host_table (host, system, host_user, host_pass) VALUES (\"%s\", \"%s\", \"%s\", \"%s\")'''
#删除主机
delete_host_sql = "DELETE FROM host_table wherer host = \"%s\""
