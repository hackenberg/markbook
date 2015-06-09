import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
homedir = os.path.expanduser("~")
maindir = os.path.join(homedir, ".markbook")


class BaseConfig:

    DEBUG = False
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev.db")


class ProductionConfig(BaseConfig):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(maindir, "prod.db")


class TestingConfig(BaseConfig):

    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
