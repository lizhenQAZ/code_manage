from . import mail
from flask_mail import Mail, Message
from threading import Thread
from config import config
from manage import app
import os


sender = config[os.getenv("FLASK_CONFIG") or 'default'].FLASKY_MAIL_SENDER
recipients = config[os.getenv("FLASK_CONFIG") or 'default'].FLASKY_MAIL_SENDER
print("==================>%s<========================" % sender)


# 发送异步邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(user):
    msg = Message(user + ' test subject',  sender=sender, recipients=[recipients])
    msg.body = 'text body'
    msg.html = '<b>HTML</b>body'
    t = Thread(target=send_async_email, args=[app, msg])
    t.start()
    return t


if __name__ == '__main__':
    send_email('haha')
    app.run()
