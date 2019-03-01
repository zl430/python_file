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
def test():
    if request.form['user'] == 'test':
        return '<h3>aaaaaaaaaaaa</h3>'
if __name__ == '__main__':
    app.run(port=66)