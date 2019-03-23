# -*- coding:utf-8 -*-
# 导入模块
import paramiko
import json
def con_linux(hostname, username, password):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = s.exec_command('ls / |wc -l')
    print(stdin, stdout, stderr)
    result = stdout.read()
    result = json.loads(result)
    print(type(result))
    s.close()
    return result
print(con_linux(hostname='117.50.64.186', username='root',  password='`1234qwer'))