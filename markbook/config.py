import os

_basedir = os.getcwd()

DEBUG = True

JSON_AS_ASCII = False

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_basedir, "app.db")
