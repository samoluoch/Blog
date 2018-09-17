import os

class Config:
    '''
    This is the general configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'

    SECRET_KEY = os.environ.get('SECRET_KEY')


    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    This is the production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_ROSE_URL")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}