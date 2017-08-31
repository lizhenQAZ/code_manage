from flask import Flask


# 跨站请求伪造保护
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'


if __name__ == '__main__':
    app.run()
