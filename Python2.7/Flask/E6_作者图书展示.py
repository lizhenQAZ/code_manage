# coding=utf-8
"""
作者书籍案例分析：
1.模板：表单wtf数据的定义/获取/验证/,使用语句遍历视图反悔的结果，删除指定数据的id
2.视图：数据库模型类的定义，wtf表单定义，数据创建
    视图函数：查询数据库，把查询结果规模版，添加或删除数据后，需要再次查询数据库
3.添加数据：db.session.add_all([auth, book])
    设置app.config['SECRET_KEY'] = 'abc'
    设置app.config['SQLALCHEMY_DATABASE_URI']
    设置app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
"""
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# 导入wtf表单扩展
from flask_wtf import FlaskForm
# 导入wtf扩展提供的字段类型
from wtforms import StringField, SubmitField
# 导入验证函数
from wtforms.validators import DataRequired

app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guest:guest@localhost/002test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 设置SECRET_KEY
app.config['SECRET_KEY'] = 'python27'

# 构造数据库实例
db = SQLAlchemy(app)


# 构造模型类：作者和小说
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return "author: %s" % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32))
    lead = db.Column(db.String(32))

    def __repr__(self):
        return "book:%s" % self.info


# 自定义表单类
class Form(FlaskForm):
    wtf_au = StringField(label=u'作者', validators=[DataRequired()])
    wtf_bk = StringField(label=u'书籍', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')


# 添加数据
@app.route('/', methods=['GET', 'POST'])
def get_auth_book():
    # 查询数据库
    auth = Author.query.all()
    book = Book.query.all()
    # 实例化表单对象
    form = Form()
    # 使用wtf表单对象的验证函数，会验证字段是数据，其次会验证表单中的csrf
    if form.validate_on_submit():
        # 接收表单中用户输入的数据
        auth = form.wtf_au.data
        book = form.wtf_bk.data
        # 把作者和书籍信息添加到模型类中
        au = Author(name=auth)
        bk = Book(info=book)
        # 提交数据、模型类对象
        db.session.add_all([au, bk])
        db.session.commit()
        auth = Author.query.all()
        book = Book.query.all()
    return render_template('002index.html', auth=auth, book=book, form=form)


# 删除作者信息
@app.route('/delete_author/<int:id>')
def del_author(id):
    # 根据id查询数据，然后删除
    author = Author.query.get(id)
    # 删除数据
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('get_auth_book'))


# 删除书籍信息
@app.route("/delete_book/<int:id>")
def del_book(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('get_auth_book'))


if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 构造数据库数据
    au_xi = Author(name='我吃西红柿', email='xihongshi@163.com')
    au_qian = Author(name='萧潜', email='xiaoqian@126.com')
    au_san = Author(name='唐家三少', email='sanshao@163.com')
    bk_xi = Book(info='吞噬星空', lead='罗峰')
    bk_xi2 = Book(info='寸芒', lead='李杨')
    bk_qian = Book(info='飘渺之旅', lead='李强')
    bk_san = Book(info='冰火魔厨', lead='融念冰')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()
    print app.url_map
    # 构造数据库数据
    app.run()
