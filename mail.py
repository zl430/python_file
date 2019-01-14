import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
 
from_addr='xxxx@163.com'
password='xxx'
to_addr=['1906869123@qq.com']
 
msg=MIMEMultipart()
msg['from']=from_addr
msg['to']=','.join(to_addr)
msg['subject']='又一封'
content='给你发2个附件'
txt=MIMEText(content)
msg.attach(txt)
with open('D:/tmp/1125/1.doc','rb') as f:
	att=MIMEApplication(f.read())
	att.add_header('Content-Disposition','attachment',filename=('gb2312','','中文.doc'))
	msg.attach(att)
with open('D:/tmp/1125/2.txt','rb') as f:
	att=MIMEApplication(f.read())
	att.add_header('Content-Disposition','attachment',filename='2.txt')
	msg.attach(att)
server=smtplib.SMTP('smtp.163.com',25)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,str(msg))
server.quit()
print('OK')
