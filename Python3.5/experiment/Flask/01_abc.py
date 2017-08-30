from flask import Flask


app = Flask(__name__)


# 路由
@app.route('/')
def index():
    return 'hello world'


@app.route('/user', methods=['POST'])
def user():
    return 'hello user'


if __name__ == '__main__':
    app.run()
