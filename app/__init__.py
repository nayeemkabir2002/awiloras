from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
 
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
bootstrap=Bootstrap()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])


    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    #Registering the blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    return app
