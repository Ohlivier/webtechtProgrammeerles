from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..decorators import admin_required

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/')
@login_required
@admin_required
def admin_dashboard():
    return render_template('adminindex.html')
