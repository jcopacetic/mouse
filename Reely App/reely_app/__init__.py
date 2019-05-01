from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from reely_app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.signin'

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(Config)

  with app.app_context():
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

  from reely_app.main.routes import main 
  from reely_app.users.routes import users
  from reely_app.blog.routes import blog
  from reely_app.errors.handlers import errors 
  app.register_blueprint(main)
  app.register_blueprint(users)
  app.register_blueprint(blog)
  app.register_blueprint(errors)

  return app