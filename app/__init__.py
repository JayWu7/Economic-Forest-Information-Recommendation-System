from flask import Flask
from flask_bootstrap import Bootstrap

from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    #app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    app.config['SECRET_KEY'] = 'jaysinging'
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)  # register blueprint

    return app
