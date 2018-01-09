# coding: utf-8
from flask import request, Flask


app = Flask(__name__)


@app.route("/")
def index():
    print(request.method)
    print(request.url)
    return "hhehea"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
