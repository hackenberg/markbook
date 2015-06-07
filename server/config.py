import os

_basedir = os.getcwd()

DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_basedir, "app.db")
