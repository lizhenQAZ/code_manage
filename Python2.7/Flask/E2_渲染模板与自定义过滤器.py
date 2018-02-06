# coding=utf-8
"""
功能：
1.render_template响应参数传递
2.自定义过滤器两种方式：
    app.add_template_filter(FuncName, 'FilterName')
    @app.template_filter('FilterName')
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    temp = 'nihao'
    ls = [5, 7, 8]
    dic = {"name": 'hehe', "age": 24}
    return render_template('001index.html', temp=temp, ls=ls, dic=dic)


# 自定义过滤器实现一
# 添加过滤器给模板
def double_filter(ls):
    return ls[::-2]
app.add_template_filter(double_filter, 'db1')


# 自定义过滤器实现二
# 自定义过滤器，名称如果和内置过滤器重名，会重写过滤器
@app.template_filter('db2')
def num_filter(ls):
    return ls[::-3]


if __name__ == '__main__':
    app.run(debug=True)
