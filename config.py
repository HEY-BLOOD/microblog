import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    WIN = sys.platform.startswith('win')
    prefix = 'sqlite:////'
    if WIN:  # Windows 环境下，三个斜杠
        prefix = 'sqlite:///'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        prefix + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 邮件服务器
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Blood Hwang', os.getenv('MAIL_USERNAME'))
