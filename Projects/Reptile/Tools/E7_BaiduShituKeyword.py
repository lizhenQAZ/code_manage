# coding: utf-8
import requests
import json

url = 'http://image.baidu.com/pcdutu/a_similar?queryImageUrl=http%3A%2F%2Fb.hiphotos.baidu.com%2Fimage%2F%2570%2569%2563%2Fitem%2F241f95cad1c8a78620abb9ab6c09c93d71cf5096.jpg&querySign=2909251985,2445959835&simid=0,0&word=&querytype=0&t=1511084998233&rn=60&sort=&fr=pc&pn=0'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response.content)
data = json.loads(response.content.decode())
print(data['result'])
