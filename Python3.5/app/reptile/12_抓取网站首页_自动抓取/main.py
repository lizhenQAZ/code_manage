import re
from lxml import etree  # html页面
import pymysql  # mysql数据库
import requests  # http协议


# 爬取数据
class Spider(object):
    def __init__(self, content):
        self.content = content
        print("正在爬取网页信息。。。。。。。。")

    def get_pic_url(self):
        # <img src="https://a1.jikexueyuan.com/home/201408/21/a650/53f54af62c068.jpg" class="lessonimg"
        # title="Python语言集成开发环境搭建" alt="Python语言集成开发环境搭建">
        # 排除JS的影响：<!--查看更多课程 <img src="/static/images/more.png"/>-->
        l_img_content = re.findall(r'<img[^>]*>[^-]', self.content, re.S)
        return l_img_content

    def handle_pic_url(self, pic_info):
        eh = etree.HTML(pic_info)
        # lessonname=Sector.xpath('//li/div[@class="lesson-infor"]/h2/a/text()')
        pic_url = eh.xpath('//img/@src')
        return pic_url

    def get_href_url(self):
        # < a href = "//www.jikexueyuan.com/course/201.html" target = "_blank"
        # jktag = "&posGP=103001&posArea=&posOper=&aCId=201&posColumn=201.1" >
        # 排除异常格式的影响,<dd><a href="#"><i class="xxzx-icon"></i>学习中心</a></dd>
        l_href_content = re.findall(r'<a[^>#]*>', self.content)
        return l_href_content

    def handle_href_url(self, href_info):
        eh = etree.HTML(href_info)
        # lessonname=Sector.xpath('//li/div[@class="lesson-infor"]/h2/a/text()')
        href_url = eh.xpath('//a/@href')
        # 排除JS的影响，<a href="javascript:;" id="diaochaid" class="diaocha"></a>
        if href_url[0].endswith(';'):
            return None
        else:
            return href_url


# mysql储存数据
class Container(object):
    def __init__(self):
        config = {
            'host': 'localhost',
            'user': 'guest',
            'password': 'guest',
            'database': 'websites',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**config)
        self.cs = self.conn.cursor()

    def insert_pic(self, l_url):
        sql = '''insert into picture values (0, %s)'''
        for url in l_url:
            # print(url)
            self.cs.execute(sql, [url])
            self.conn.commit()

    def insert_web(self, l_url):
        sql = '''insert into website values (0, %s)'''
        for url in l_url:
            self.cs.execute(sql, [url])
            self.conn.commit()

    def close(self):
        self.cs.close()
        self.conn.close()


def _main():
    l_img_content = list()
    l_img_url = list()
    l_href_content = list()
    l_href_url = list()

    # 1.打开网站：http://www.jikexueyuan.com/course/?pageNum=1
    default_url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    content = requests.get(default_url)
    # print(content)
    spider = Spider(content.text)

    # 2.爬取图片网页
    l_img_content = spider.get_pic_url()
    print('正在爬取图片链接。。。')
    for i, content in enumerate(l_img_content):
        url = spider.handle_pic_url(content)
        print('the %d line:%s' % (i+1, url[0]))
        l_img_url.append(url[0])
    # print(l_img_url)

    # 3.爬取首页链接
    l_href_content = spider.get_href_url()
    print('正在爬取网页链接。。。')
    escape_num = 0
    for i, content in enumerate(l_href_content):
        url = spider.handle_href_url(content)
        if url is None:
            escape_num += 1
        else:
            print('the %d line:%s' % (i+1-escape_num, url[0]))
            l_href_url.append(url[0])
    # print(l_href_url)

    # # 4.将数据存入数据库
    # container = Container()
    # container.insert_pic(l_img_url)
    # container.insert_web(l_href_url)
    # container.close()


if __name__ == '__main__':
    _main()
