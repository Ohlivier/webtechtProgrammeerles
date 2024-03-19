from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField


class InschrijvenForm(FlaskForm):
    submit = SubmitField('Inschrijven')