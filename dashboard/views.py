from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard_blueprint.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')
