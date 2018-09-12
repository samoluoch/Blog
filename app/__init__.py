from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initialaizing Flask extensions
bootstrap = Bootstrap()
# db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

# Creating app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)


    # Initializing bootstrap
    bootstrap.init_app(app)

    # Initializing sqlalchemy database
    # db.init_app(app)

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the authentication blueprint
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Initializing the login manager
    # login_manager.init_app(app)


    return app