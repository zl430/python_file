from flask import Flask
from flask import request
app = Flask(__name__)
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
@app.route('/signin', methods=['POST'])
def signin():
    # print(request.query_string)
    if request.form['username']=='admin' and request.form['password']=='password':
        from API import dnspod_class
        add = dnspod_class.dnspod_api_chk('71244700', 'www', '1.1.1.1')
        add.dns_add()
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'
@app.route('/test', methods=['POST'])
def dnspod():
    if request.form['user'] == 'test':
        return '<h3>aaaaaaaaaaaa</h3>'
@app.route('/user_chk', methods=['POST'])
def user_chk():
    name = request.form['username']
    password = request.form['password']
    from requrst import mysql_select
    over = mysql_select.mysql_select(name, password)
    overa = over.user_select()
    if overa == True:
        return 'you name ' + name + 'and password' + password
    return '用户名密码错误'
if __name__ == '__main__':
    app.run(port=66)