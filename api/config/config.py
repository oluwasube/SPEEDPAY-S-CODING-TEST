import os
from decouple import config
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    secret_key = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevelopementConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(BASE_DIR, "devdb.sqlite3")


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config_names = {
    "dev": DevelopementConfig,
    "test": TestConfig,
    "prod": ProductionConfig
}
