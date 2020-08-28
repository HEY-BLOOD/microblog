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
