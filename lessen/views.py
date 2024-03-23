from flask import Blueprint, render_template, request, flash
from flask_login import login_required
import markdown
import os
from pathlib import Path

lessen_blueprint = Blueprint('lessen', __name__, template_folder='templates')



@lessen_blueprint.route('/')
@login_required
def lessen():
    current_directory = os.path.dirname(__file__)
    naam = request.args.get('lesnaam')
    if len(naam) == 0:
        return "wottefok"
    les_naam = naam.split('_')[0]
    print(naam)
    cursus_dir = os.path.join(current_directory, 'cursussen', naam)
    lessen = {}
    for filename in os.listdir(cursus_dir):
        lessen[filename] = Path(filename).stem
    print(lessen)
    if request.args.get('les') is not None:
        les_bestand = request.args.get('les')
        print(cursus_dir)
        try:
            with open(f'{cursus_dir}/{les_bestand}', 'r') as f:
                text = f.read()
                html = markdown.markdown(text)
        except FileNotFoundError as e:
            html = 'x'
            flash('dit bestand bestaat niet!')
        return render_template('renderles.html', html=html, naam=naam)
    return render_template('lesbase.html', lessen=lessen, naam=naam)
