# coding=utf-8
from flask import Blueprint

# 第一步：创建蓝图对象
api = Blueprint('api', __name__)

from E9_AuthBook import Author, Book, db, redirect, url_for


# 第二步：使用蓝图对象
# 删除作者信息
@api.route('/delete_author/<int:id>')
def del_author(id):
    # 根据id查询数据，然后删除
    author = Author.query.get(id)
    # 删除数据
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('get_auth_book'))


# 删除书籍信息
@api.route("/delete_book/<int:id>")
def del_book(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('get_auth_book'))