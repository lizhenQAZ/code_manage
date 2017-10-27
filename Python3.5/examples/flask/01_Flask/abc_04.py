from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/guess')
def guess():
    # url_for用法：url_for('函数名')
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
