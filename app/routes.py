from app.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for
from app import app, db  # 从app包导入其成员app变量
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [{
        'author': {
            'username': 'John'
        },
        'body': 'Beautiful day in Portland!'
    }, {
        'author': {
            'username': 'Susan'
        },
        'body': 'The Avengers movie was so cool!'
    }]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 用户是否通过登录认证
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # 验证表单数据
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # 用户名或密码有误
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # 注册用户为已登录
        login_user(user, remember=form.remember_me.data)
        # 登录后页面重定向
        next_page = request.args.get('next')
        # 检查重定向与应用保持在同一站点，使用应用更安全
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    """ 登出用户 """
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 用户是否通过登录认证
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    # 验证表单数据
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
