import requests
url = 'http://127.0.0.1:66/user_chk'
data = {'username': '1', 'password': '123'}
# url = 'http://127.0.0.1:66/test'
print(url, data)
a = requests.post(url, data)
print(a)
print(a.text)