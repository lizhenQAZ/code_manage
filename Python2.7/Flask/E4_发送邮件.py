# coding=utf-8
"""
功能：
1.发送邮件
    配置邮箱服务器、端口、TLS加密、登录用户名与应用授权码
    配置邮件发件人、收件人、标题与邮件内容
"""
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='lz15251847740@163.com',
    MAIL_PASSWORD='qazwsx741852',
)

mail = Mail(app)


@app.route('/')
def index():
    msg = Message("Hello test", html='Hello test mail', sender='lz15251847740@163.com', recipients=['lz15251847740@163.com'])
    mail.send(msg)
    print "Mail sent"
    return "Send successfully"


if __name__ == '__main__':
    app.run(debug=True)
