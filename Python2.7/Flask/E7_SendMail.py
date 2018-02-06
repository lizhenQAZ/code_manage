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
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='516960831@qq.com',
    MAIL_PASSWORD='pdqerqvsvsdlbgij',
)

mail = Mail(app)


@app.route('/')
def index():
    msg = Message("Hello test", html='Hello test mail', sender='516960831@qq.com', recipients=['516960831@qq.com'])
    mail.send(msg)
    print "Mail sent"
    return "Send successfully"


if __name__ == '__main__':
    app.run(debug=True)
