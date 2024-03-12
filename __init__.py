from flask import Flask
from .config import Config
from .docent.views import docenten_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
app.register_blueprint(docenten_blueprint, url_prefix='/docenten')

