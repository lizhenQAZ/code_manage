from flask import Flask
from flask_script import Manager, Shell


def print_shell():
    return dict(name='haha', content='hello')

app = Flask(__name__)
manager = Manager(app)
manager.add_command("shell", Shell(make_context=print_shell))


@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    manager.run()
