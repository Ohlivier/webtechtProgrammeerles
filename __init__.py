from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from .models import *


@login_manager.user_loader
def get_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None


migrate = Migrate(app, db, compare_type=True, render_as_batch=True)

from .dashboard import views

app.register_blueprint(views.dashboard_blueprint, url_prefix='/dashboard')

from .admin import views

app.register_blueprint(views.admin_blueprint, url_prefix='/admin')
