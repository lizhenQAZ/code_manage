from flask import Flask
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@manager.command
def print_hello():
    print("hello manager")


@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    manager.run()
