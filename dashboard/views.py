from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Lessen, User, Talen, Inschrijvingen
from datetime import date
from .forms import InschrijvenForm
from ..cursusget import get_current_cursus

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates')


def has_korting():
    if current_user.is_authenticated:
        count = (
            db.session.query(Inschrijvingen)
            .filter(Inschrijvingen.userID == current_user.id).count())
        if count >= 1:
            return True
        else:
            return False


@dashboard_blueprint.route('/')
@login_required
def dashboard():
    current_user_cursus = get_current_cursus()
    lessen_namen = []
    for folder, naam in current_user_cursus.items():
        lessen_namen.append(folder)
    return render_template('dashboard.html', cursussen=current_user_cursus, lessen_namen=lessen_namen)


@dashboard_blueprint.route('/beschikbaar/', methods=['GET', 'POST'])
@login_required
def beschikbaar():
    current_user_cursus = get_current_cursus()
    lessen_namen = []
    for folder, naam in current_user_cursus.items():
        lessen_namen.append(folder)
    print(current_user_cursus)
    if request.method == 'POST' and request.args.get('id') is not None:
        lesid = request.args.get('id')
        current_user_id = current_user.id
        if db.session.query(Inschrijvingen).filter(Inschrijvingen.lessenID == lesid,
                                                   Inschrijvingen.userID == current_user_id).count() == 1:
            flash('U bent al ingeschreven voor deze cursus!')
            return redirect(url_for('dashboard.beschikbaar'))
        inschrijving = Inschrijvingen(userID=current_user_id, lessenID=lesid)
        db.session.add(inschrijving)
        db.session.commit()
        flash(f'U hebt zich ingeschreven voor de cursus {request.args.get("naam")}')
        return redirect(url_for('dashboard.beschikbaar'))
    current_time = date.today()
    beschikbare_cursussen = Lessen.query.filter(Lessen.startDatum > current_time).all()
    namen = db.session.query(User.id, User.username).filter(User.role == 'admin').all()
    talen = db.session.query(Talen.id, Talen.name).all()
    docent_naam = [(f'{naam[0]}', naam[1]) for naam in namen]
    taal_namen = [(f'{talen[0]}', talen[1]) for talen in talen]
    talendict = {}
    docentendict = {}
    for talen in taal_namen:
        talendict[int(talen[0])] = talen[1]
    for docent in docent_naam:
        docentendict[int(docent[0])] = docent[1]
    form = InschrijvenForm()
    korting = has_korting()
    print(korting)
    return render_template('available.html', form=form, beschikbaar=beschikbare_cursussen, talendict=talendict,
                           docentendict=docentendict, cursussen=current_user_cursus, lessen_namen=lessen_namen, korting=korting)
