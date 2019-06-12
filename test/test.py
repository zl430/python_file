# # -*- coding: utf-8 -*-
# import paramiko
# import json
# # 服务器相关信息,下面输入你个人的用户名、密码、ip等信息
# ip = "140.143.19.168"
# port = 22
# user = "root"
# password = "Bq!DaMyU&UCHDFka"
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 建立连接
# ssh.connect(ip, port, user, password, timeout=10)
# #输入linux命令
# stdin,stdout,stderr = ssh.exec_command("cat   /data/python/gameNotice_backup/gameNotice.json")
# # 输出命令执行结果
# result = stdout.read()
# print(result)
# result = str(result, encoding='utf-8')
# result = json.loads(result)
# print(result)
# result['1000']['desc'] = '你地方离开你的fog你立刻飞到南方你离开你的联发科梦罗克除非你怕李开复内控规范党内村民的法律'
# stdin,stdout,stderr = ssh.exec_command("echo result  > /home/test.txt")
# print(result)
# #关闭连接
# ssh.close()

import requests
data = {'username': 'test3463', 'password': '123456'}
r = requests.post('http://127.0.0.1:66/login', data)
print('http://127.0.0.1:66/login', data)
print(r.text)