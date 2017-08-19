import time
import re
from pymysql import *
import urllib.parse


g_templates_root = './templates'
g_url_handle = dict()


def route(url):
    def set_func(func):
        g_url_handle[url] = func
        def call_func(filename):
            return func(filename, url)
        return call_func
    return set_func


@route(r'/index\.html')
def index(filename, url):
    '''股票主页'''  
    try:
        fd = open(g_templates_root + filename)
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()

        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cs = db.cursor()
        sql = '''select * from info;
        '''
        cs.execute(sql)
        t_stock_info = cs.fetchall()
        cs.close()
        db.close()

        html = ''''''
        html_template = '''
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
            </tr>'''

        for info in t_stock_info:
            html +=  html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])
        content = re.sub(r'\{%content%\}', html, content)
        return content


@route(r'/center\.html')
def center(filename, url):
    '''个人信息中心'''
    try:
        fd = open(g_templates_root + filename)
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()

        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cs = db.cursor()
        sql = '''select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f where i.id=f.info_id;
        '''
        cs.execute(sql)
        t_note_info = cs.fetchall()        
        cs.close()
        db.close()

        replace_data = ''''''
        html = '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>''' 

        for info in t_note_info:
            replace_data +=  html % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])
 
        content = re.sub(r'\{%content%\}', replace_data, content)
        return content


@route(r'/update/(\d+)\.html')
def update(filename, url):
    '''个人信息中心'''
    try:
        fd = open(g_templates_root + '/update.html')
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()

        ret = re.match(url, filename)
        if ret:
            stock_code = ret.group(1)
        else:
            stock_code = 0

        db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cs = db.cursor()
        sql = ''' select f.note_info from focus as f inner join info as i on f.info_id=i.id where i.code='%s';
        ''' % stock_code
        cs.execute(sql)
        note_info = cs.fetchone()[0]        
        cs.close()
        db.close()

        content = re.sub(r'\{%code%\}', stock_code, content)
        content = re.sub(r'\{%note_info%\}', note_info, content)
        return content


@route(r'/update/(\d+)/(.*)\.html')
def update(filename, url):
    '''备注修改'''
    ret = re.match(url, filename)
    if ret:
        stock_code = ret.group(1)
        stock_note_info = ret.group(2)
        stock_note_info = urllib.parse.unquote(stock_note_info) 
    else:
        stock_code = 0
        stock_note_info = ''

    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cs = db.cursor()
    sql = ''' update focus as f inner join info as i on f.info_id=i.id set f.note_info='%s' where i.code='%s';
    ''' % (stock_note_info, stock_code)
    cs.execute(sql)
    db.commit()        
    cs.close()
    db.close()

    return '修改成功'


@route(r'/add/(\d+).html')
def add(filename, url):
    '''添加关注'''
    ret = re.match(url, filename)
    if ret:
        stock_code = ret.group(1)
    else:
        stock_code = 0

    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cs = db.cursor()


    sql = ''' select * from focus as f inner join info as i on f.info_id=i.id where i.code='%s';
    ''' % stock_code
    cs.execute(sql)
    ret = cs.fetchone()
    if ret:
        return '已经关注，无需加入'

    else:
        sql = ''' insert into focus(info_id) select id from info where code='%s';
        ''' % stock_code
        cs.execute(sql)
        db.commit()        
        cs.close()
        db.close()

        return '关注成功'


@route(r'/del/(\d+).html')
def delete(filename, url):
    '''取消关注'''
    ret = re.match(url, filename)
    if ret:
        stock_code = ret.group(1)
    else:
        stock_code = 0

    db = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
    cs = db.cursor()

    sql = ''' delete from focus where info_id=(select id from info where code='%s');
    ''' % stock_code
    cs.execute(sql)
    db.commit()        
    cs.close()
    db.close()

    return '取消关注成功'

def app(environ, start_handle):
    status = '200 OK'
    start_handle(status, [('Content-Type', 'text/html')])
    filename = environ['PATH_INFO']
    try:
        for url, call_func in g_url_handle.items():
            print(url)
            ret = re.match(url, filename)
            if ret:
                return call_func(filename, url)
                break
        else:
            print('no website found.')

    except Exception as e:
        print('Exception %s exists.' % e)

    else:
        return str(environ) + 'send to...>>%s' % time.ctime()
