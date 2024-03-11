from flask import Blueprint
from docent.forms import TaalForm
docenten_blueprint = Blueprint('docenten', __name__, template_folder='templates')


@docenten_blueprint.route('/')
def hello_world():
    form = TaalForm()
    return f'Hello World'
