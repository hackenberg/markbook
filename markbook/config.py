import os

_basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class BaseConfig:

    API = True
    DEBUG = False
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):
    _datadir = os.path.join(_basedir, "database")

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_datadir, "dev.db")


class ProductionConfig(BaseConfig):
    _homedir = os.path.expanduser("~")
    _maindir = os.path.join(_homedir, ".markbook")

    API = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_maindir, "prod.db")


class TestingConfig(BaseConfig):

    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
