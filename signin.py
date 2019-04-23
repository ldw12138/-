from flask import Flask
from flask import request
from check import check_user
from insert import insert_sinfo
from find_s import find_sinfo
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if check_user(request.form['username'], request.form['password']):
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/ins', methods=['GET'])
def insert_form():
    return '''<form action="/ins" method="post">
              <p><font size="2">学号:<front><input name="sno"></p>
              <p><font size="2">姓名:<front><input name="sname"></p>
              <p><font size="2">性别:<front><input name="ssex"></p>
              <p><font size="2">年龄:<front><input name="sage"></p>
              <p><font size="2">专业:<front><input name="sdept"></p>
              <p><button type="submit">insert</button></p>
              </form>'''


@app.route('/ins', methods=['POST'])
def inserts():
    insert_sinfo(request.form['sno'], request.form['sname'], request.form['ssex'], request.form['sage'], request.form['sdept'])
    return '<h3>insert successfully</h3>'


@app.route('/find', methods=['GET'])
def find_form():
    return '''<form action="/find" method="post">
              <p><font size="2">请输入要查询的学生的姓名<front><input name="s_name"></p>
              <p><button type="submit">find</button></p>
              </form>'''


# 查询功能还没实现
# @app.route('/find', methods=['POST'])
# def find_func():
#     s = find_sinfo(request.form['s_name'])
#     return '<h3>'+s+'</h3>'


if __name__ == '__main__':
    app.run()
