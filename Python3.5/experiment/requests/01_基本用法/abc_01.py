import requests
import json


url = "https://api.github.com/user"
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print('---1---', r.status_code)
print('---2---', r.headers['content-type'])
print('---3---', r.encoding)
# {"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}
print('---4---', r.text)
# {'message': 'Bad credentials', 'documentation_url': 'https://developer.github.com/v3'}
print('---5---', r.json())
print('---6---', r.url)
print('---7---', r.content)
print('---8---', r.raw)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
r = requests.get('https://api.github.com/user', headers=headers)
print('---9---', r.status_code)

data = (('user', 'lizhen'), ('password', '123'))
r = requests.post('https://api.github.com/user', data=data)
print('---10---', r.status_code)

data = {'user': 'lizhen', 'password': '123'}
r = requests.post('https://api.github.com/user', json=data)
print('---11---', r.status_code)

data = {'user': 'lizhen', 'password': '123'}
r = requests.post('https://api.github.com/user', data=json.dumps(data))
print('---12---', r.status_code)

print('---13---', r.headers)
print('---14---', r.cookies)

cookies = dict(cookies_are='working')
r = requests.get('https://api.github.com/user', cookies=cookies)
print('---15---', r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
r = requests.get('https://api.github.com/user', cookies=jar)
# '{"cookies": {"tasty_cookie": "yum"}}'
print('---16---', r.text)

print('---17---', r.history)

r = requests.get('http://github.com', timeout=5)
print('---18---', r.text)

r = requests.get('http://github.com', allow_redirects=False)
print('---19---', r.text)
