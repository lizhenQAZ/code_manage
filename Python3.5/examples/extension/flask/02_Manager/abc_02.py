from flask import Flask
from flask_script import Manager, Command


class Print(Command):
    def run(self):
        print("hello manager")


app = Flask(__name__)
manager = Manager(app)
manager.add_command("print", Print())


@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    manager.run()
