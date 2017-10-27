import requests

# 抓取百度贴吧的网页
print('*'*100)
print('网页抓取开始...')
response = requests.get('http://tieba.baidu.com/index.html')
with open('03_保存百度贴吧网页.html', 'w') as f:
    f.write(response.content.decode())
print('网页抓取结束...')
