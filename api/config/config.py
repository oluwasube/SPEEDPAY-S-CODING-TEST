import os
from decouple import config


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    secret_key = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR, 'db.sqlite3')


class TestConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config_names = {
    "dev": DevelopmentConfig,
    "test": TestConfig,
    "prod": ProductionConfig
}
