# coding=utf-8
"""
功能：
1.获取AccessToken
    参数：WECHAT_APPID、WECHAT_SECRET
    return：access_token
2.生成QRCode
    1.access_token获取ticket
    2.ticket换取二维码
"""
import datetime
import urllib
import urllib2
import json
from flask import Flask

app = Flask(__name__)

WECHAT_APPID = 'wx3194d1ff342ec4cd'
WECHAT_SECRET = '7d69e191479dba12bb1e22abf535fb3f'


class AccessToken(object):
    _access_token = {
        'token': '',
        'expires_in': '',
        'updatetime': datetime.datetime.now()
    }

    @classmethod
    def get_access_token(cls):
        if not cls._access_token['token'] or (datetime.datetime.now() - cls._access_token['updatetime']).seconds > 6800:
            return cls.__update_access_token()
        else:
            return cls._access_token['token']

    @classmethod
    def __update_access_token(cls):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APPID, WECHAT_SECRET)
        resp = urllib.urlopen(url).read()
        resp_data = json.loads(resp)
        cls._access_token['token'] = resp_data.get('access_token')
        return cls._access_token['token']


@app.route("/scene_id=<sid>")
def get_ticket(sid):
    access_token = AccessToken.get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s' % access_token
    req_body = {
        'expire_seconds': 7200,
        'action_name': 'QR_SCENE',
        'action_info': {'scene': {'scene_id': sid}}
    }
    data = json.dumps(req_body)
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req).read()
    print resp
    if 'errcode' in resp:
        return 'error'
    else:
        resp_data = json.loads(resp)
        ticket = resp_data['ticket']
        return '<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket


if __name__ == '__main__':
    print AccessToken.get_access_token()
    app.run(host='0.0.0.0', port=8910, debug=True)
