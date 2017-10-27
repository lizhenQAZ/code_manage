from flask import Blueprint


message = Blueprint('msg', __name__)


@message.route('/')
def message1():
    return '/message/root'


@message.route('/test')
def message2():
    return '/message/test'
