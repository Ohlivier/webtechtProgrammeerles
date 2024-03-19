from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.role != 'admin':
            flash("You don't have permission to access this resource.", "warning")
            return redirect(url_for("index"))
        return func(*args, **kwargs)

    return decorated_view
