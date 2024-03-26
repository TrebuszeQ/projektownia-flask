from dataclasses import dataclass
import os
basedir = os.path.abspath(os.path.dirname(__file__))


@dataclass(repr=True)
class Config:
    APP_NAME = os.environ.get('APP_NAME')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')
    TITLE = os.environ.get('TITLE')
    APP_ADMIN = os.environ.get('APP_ADMIN')
    APP_MAIL_SENDER = os.environ.get('APP_MAIL_SENDER')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQL_ALCHEMY_TRACK_NOTIFICATIONS = os.environ.get('SQL_ALCHEMY_TRACK_NOTIFICATIONS')

    class DevConfig(Config):
        DEBUG = True


