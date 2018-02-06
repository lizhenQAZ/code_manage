from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm
# from ..email import send_email
from ..models import User, db
from flask_login import login_user, login_required, logout_user, current_user


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     # 模板文件的路径是相对文件夹而言的
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data, username=form.username.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         token = User.generate_confirmation_token()
#         print(send_email(user.email))
#         flash('A confirmation email has been sent to you by email.')
#         return redirect(url_for("main.index"))
#     return render_template('auth/register.html', form=form)


# @auth.route('/confirm/<token>')
# @login_required
# def confirm(token):
#     if current_user.confirmed:
#         return redirect(url_for('main.index'))
#     if current_user.confirm(token):
#         flash('You have confirmed your account. Thanks!')
#     else:
#         flash('The confirmation is invalid or has expired.')
#     return redirect(url_for('main.index'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 模板文件的路径是相对文件夹而言的
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            print("==================>%s login %s<==========================" % (current_user, current_user.is_authenticated()))
            return redirect(request.args.get('next') or url_for("main.index"))
            flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print("==================>%s logout %s<==========================" % (current_user, current_user.is_authenticated()))
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
