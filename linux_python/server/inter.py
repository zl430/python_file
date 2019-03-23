from flask import Flask
from flask import request
import mysql_operation
app = Flask(__name__)
@app.route('/login', methods=['POST'])
def login():
    # name = request.args.get("username")
    # password = request.args.get("password")
    name = request.form['username']
    password = request.form['password']
    mysql = mysql_operation.connection(username=name, password=password, mail=None)
    over = mysql.login()
    if over == True:
        return '1'
    elif over == False:
        return '2'
    else:
        return '0'
@app.route('/registered', methods=['POST'])
def registered():
    name = request.form['username']
    password = request.form['password']
    mail = request.form['mail']
    mysql = mysql_operation.connection(username=name, password=password, mail=mail)
    over = mysql.create()
    if over == True:
        return '1'
    else:
        return '0'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=66)