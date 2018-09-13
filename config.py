import os

class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'

    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    This is the production configuration child class
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}