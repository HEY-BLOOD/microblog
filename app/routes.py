from app import app  # 从app包导入其成员app变量


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
