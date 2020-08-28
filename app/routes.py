from app import app  # 从app包导入其成员app变量
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)
