# coding=utf-8
"""
功能：
1.服务器验证
2.文本消息回复
3.语音识别
"""
import time
import hashlib
from flask import Flask, request
import xmltodict

app = Flask(__name__)


@app.route('/wechat8910/', methods=['GET', 'POST'])
def wechat_validate():
    if request.method == 'GET':
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = "python"
        data = [token, timestamp, nonce]
        print data
        data.sort()
        data = ''.join(data)
        sha1 = hashlib.sha1()
        sha1.update(data)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr, 200
        else:
            return "error", 666
    elif request.method == 'POST':
        xml = request.data
        req = xmltodict.parse(xml)['xml']
        msg_type = req.get('MsgType')
        if 'text' == msg_type:
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': req.get('Content')
            }
            xml = xmltodict.unparse({'xml': resp})
            print req.get('Content')
            return xml, 200
        elif 'voice' == msg_type:
            print 11111
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': req.get('Recognition', u'无法识别')
            }
            xml = xmltodict.unparse({'xml': resp})
            print req.get('Content')
            return xml, 200
        else:
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': 'hehehe'
            }
            xml = xmltodict.unparse({'xml': resp})
            print req.get('Content')
            return xml, 666
if __name__ == '__main__':
    app.run(port=8910, debug=True)
