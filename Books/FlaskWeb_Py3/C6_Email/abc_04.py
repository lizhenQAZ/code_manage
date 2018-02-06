from flask import Flask
from flask_mail import Mail, Message
from threading import Thread


# 配置sina邮箱
# TLS加密
# smtp：25  pop3:110
# 需要验证码
# 配置qq邮箱
# TLS加密
# smtp：465或587  pop3:995
# 需要授权码
# 查看调试信息
app = Flask(__name__)
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['FLASKY_MAIL_SENDER'] = '516960831@qq.com'
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587  # IMAP/SMTP
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
print(type(app.config['MAIL_USERNAME']), app.config['MAIL_USERNAME'], type(app.config['MAIL_PASSWORD']), app.config['MAIL_PASSWORD'])
mail = Mail(app)
# 设置环境变量
# set MAIL_USERNAME=用户名
# set MAIL_PASSWORD=密码，使用授权码


# 发送异步邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(user):
    msg = Message(user + ' test subject',  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[app.config['FLASKY_MAIL_SENDER']])
    msg.body = 'text body'
    msg.html = '<b>HTML</b>body'
    t = Thread(target=send_async_email, args=[app, msg])
    t.start()
    return t


if __name__ == '__main__':
    send_email('haha')
    app.run()
