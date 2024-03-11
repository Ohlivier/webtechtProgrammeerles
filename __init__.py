from flask import Flask
from config import Config
from docent.views import docenten_blueprint




app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(docenten_blueprint, url_prefix='/docenten')