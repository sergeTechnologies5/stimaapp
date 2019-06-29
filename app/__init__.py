from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from app.config import Config
from dotenv import load_dotenv
import threading

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
from app.camera import thread_function_startCam

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    x = threading.Thread(target=thread_function_startCam)
    return app

from app.models import User, Stima