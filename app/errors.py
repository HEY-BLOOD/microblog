from flask import render_template
from app import app, db
from werkzeug.exceptions import HTTPException


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def all_exception_handler(e):
    """ 处理所有的 HTTP 错误 """
    # 对于 HTTP 异常，返回自带的错误描述和状态码
    # 这些异常类在 Werkzeug 中定义，均继承 HTTPException 类
    # 500 未知异常
    # result = render_template('error.html', description='Sorry, internal error.'), 500
    result = None
    if isinstance(e, HTTPException):
        result = render_template('error.html',
                                 description=e.description), e.code
    return result  # 返回响应和 状态码
