from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from .decorators import admin_required
from ..models import User, Talen, Lessen
from .. import db
from .forms import SetRole, SetEmail, SetUsername, AddTaal, DeleteTaal, CreateCursus
import pathlib
import os

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
        return render_template('viewuser.html', user=user, emailform=emailform, usernameform=usernameform,
                               roleform=roleform)
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
        id = request.args.get('id')
        print(id)
        flash(f'Taal met ID {id} is verwijderd ')
        taal = Talen.query.get(id)
        db.session.delete(taal)
        db.session.commit()
        return redirect(url_for('admin.taal'))
    if form.validate_on_submit() and request.method == 'POST':
        print(form.taal.data)
        adding = Talen(name=form.taal.data)
        db.session.add(adding)
        db.session.commit()
        return redirect(url_for('admin.taal'))
    talen = Talen.query.all()
    return render_template('addtaal.html', form=form, talen=talen, delete=delete)


@admin_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
@admin_required
def add():
    form = CreateCursus()
    if request.method == 'POST' and form.validate_on_submit():
        print(form.datum.data)
        cursus = Lessen(docentID=int(form.docenten.data), talenID=int(form.talen.data), locatie=form.locatie.data, startDatum=form.datum.data, prijs=float(form.prijs.data))
        db.session.add(cursus)
        db.session.commit()
        lesid = db.session.query(Lessen.lesID).order_by(Lessen.lesID.desc()).first()
        talen = db.session.query(Talen.id, Talen.name).all()
        form.talen.choices = [(f'{talen[0]}', talen[1]) for talen in talen]
        talendict = {}
        for talen in form.talen.choices:
            talendict[int(talen[0])] = talen[1]
        mapnaam = f"{talendict[int(form.talen.data)]}_{lesid[0]}"
        basedir = pathlib.Path().resolve()
        path = os.path.join(basedir,'lessen', "cursussen", mapnaam)
        os.mkdir(path)
        with open(os.path.join(path, "les1.md"), "x") as file:
            file.write("Dit is je eerste les!")
        flash("Cursus toegevoegd!")
        return redirect(url_for('admin.add'))
    namen = db.session.query(User.id, User.username).filter(User.role == 'admin').all()
    talen = db.session.query(Talen.id, Talen.name).all()
    cursussen = Lessen.query.all()
    form.docenten.choices = [(f'{naam[0]}', naam[1]) for naam in namen]
    form.talen.choices = [(f'{talen[0]}', talen[1]) for talen in talen]
    talendict = {}
    docentendict = {}
    for talen in form.talen.choices:
        talendict[int(talen[0])] = talen[1]
    for docent in form.docenten.choices:
        docentendict[int(docent[0])] = docent[1]
    print(form.docenten.choices)
    return render_template('addcourse.html', form=form, cursussen=cursussen, talendict=talendict,
                           docentendict=docentendict)
