from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mongo = PyMongo()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'auth.login'
app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mongo.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # register blueprint

    return app
