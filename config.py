import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you will never guess this'
    SQLALCHEMY_DATABASE_URI = os.path.join(f"sqlite:///{os.path.join(basedir, 'database.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
