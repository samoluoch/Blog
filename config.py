import os

class Config:

    SECRET_KEY = os.environ.get('blogger')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}