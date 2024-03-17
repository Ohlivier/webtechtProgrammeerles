from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..decorators import admin_required
from ..models import User, Talen
from .. import db
from .forms import SetRole, SetEmail, SetUsername, AddTaal, DeleteTaal

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/')
@login_required
@admin_required
def admin_dashboard():
    return render_template('adminindex.html')


@admin_blueprint.route('/gebruikers', methods=['GET', 'POST'])
@login_required
@admin_required
def gebruikers():
    emailform = SetEmail()
    usernameform = SetUsername()
    roleform = SetRole()
    if request.args.get('id') is not None and request.method == 'POST':
        user = User.query.get(int(request.args.get('id')))
        if emailform.submit1.data and emailform.validate:
            user.email = emailform.email.data
            db.session.commit()
        if usernameform.submit2.data and usernameform.validate:
            user.username = usernameform.username.data
            db.session.commit()
            print(user.username)
        if roleform.submit3.data and roleform.validate:
            user.role = roleform.role.data
            db.session.commit()
    if request.args.get('id') is not None:
        user = User.query.get(int(request.args.get('id')))
        return render_template('viewuser.html', user=user, emailform=emailform, usernameform=usernameform, roleform=roleform)
    users = User.query.all()
    print(users)
    return render_template('users.html', users=users)


@admin_blueprint.route('/taal', methods=['GET', 'POST'])
@login_required
@admin_required
def taal():
    form = AddTaal()
    delete = DeleteTaal()
    if request.method == 'POST' and request.args.get('id') is not None and delete.delete:
        print(request.args.get('id'))
        flash(f'Taal met ID {request.args.get("id")} is verwijderd ')
        return redirect(url_for('admin.taal'))
    if form.validate_on_submit() and request.method == 'POST':
        print(form.taal.data)
        adding = Talen(name=form.taal.data)
        db.session.add(adding)
        db.session.commit()
        return redirect(url_for('admin.taal'))
    talen = Talen.query.all()
    return render_template('addtaal.html', form=form, talen=talen, delete=delete)