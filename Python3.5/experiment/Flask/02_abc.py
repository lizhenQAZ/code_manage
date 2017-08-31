from flask import Flask
from flask.ext.script import Manager  # flask脚本
from flask import make_response


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>this is the index html</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s</h1>' % name


@app.route('/response')
def response():
    response = make_response('<h1>this request has a cookie</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == '__main__':
    manager.run()
