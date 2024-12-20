from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
import markdown
from markdown.extensions import codehilite, toc
import os
from pathlib import Path

lessen_blueprint = Blueprint('lessen', __name__, template_folder='templates')


@lessen_blueprint.route('/')
@login_required
def lessen():
    current_directory = os.path.dirname(__file__)
    naam = request.args.get('lesnaam')
    try:
        if len(naam) == 0:
            return "wottefok"
    except TypeError:
        flash("Deze les bestaat niet!")
        return redirect(url_for('dashboard.dashboard'))
    # les_naam = naam.split('_')[0]
    print(naam)
    cursus_dir = os.path.join(current_directory, 'cursussen', naam)
    lessen = {}
    try:
        for filename in os.listdir(cursus_dir):
            lessen[filename] = Path(filename).stem
    except FileNotFoundError:
        flash("Deze les bestaat niet!")
        return redirect(url_for('dashboard.dashboard'))
    print(lessen)
    if request.args.get('les') is not None:
        les_bestand = request.args.get('les')
        print(cursus_dir)
        try:
            with open(f'{cursus_dir}/{les_bestand}', 'r') as f:
                text = f.read()
                html = markdown.markdown(text, extensions=['extra', 'codehilite', 'nl2br', 'toc'])
        except FileNotFoundError:
            flash('dit bestand bestaat niet!')
            return redirect(url_for('dashboard.dashboard'))
        return render_template('renderles.html', html=html, naam=naam)
    return render_template('lesbase.html', lessen=lessen, naam=naam)
