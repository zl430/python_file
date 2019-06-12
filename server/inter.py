from flask import Flask
from flask import request
from flask_cors import *
import mysql_operation
app = Flask(__name__)
CORS(app, supports_credentials=True)
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
# @app.route('/signin', methods=['POST'])
# def signin():
#     # print(request.query_string)
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         from API import dnspod_class
#         add = dnspod_class.dnspod_api_chk('71244700', 'www', '1.1.1.1')
#         add.dns_add()
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
# @app.route('/login', methods=['GET'])
@app.route('/login', methods=['POST'])
def login():
    # name = request.args.get("username")
    # password = request.args.get("password")
    name = request.form['username']
    password = request.form['password']
    print(name, password)
    mysql = mysql_operation.connection(username=name, password=password)
    over = mysql.login()
    if over == True:
        return '1'
    elif over == 'N':
        return '2'
    elif over == 'nouser':
        return '0'
@app.route('/registered', methods=['POST'])
def registered():
    name = request.form['username']
    password = request.form['password']
    mysql = mysql_operation.connection(username=name, password=password)
    over = mysql.create()
    if over == True:
        return '1'
    else:
        return '0'
@app.route('/checkhost', methods=['POST'])
def check_host():
    hostip = request.form['hostip']
    print(hostip)
    mysql = mysql_operation.connection(hostip=hostip)
    over = mysql.host_information()
    return over
    # if over == True:
    #     return '1'
    # else:
    #     return '0'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=66)