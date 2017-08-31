from flask import Flask
from flask import render_template  # jinja2模板引擎
from flask_bootstrap import Bootstrap  # bootstrap前端js框架


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/<name>')
def index(name):
    return render_template('base.html', name=name)


# 自定义错误界面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
