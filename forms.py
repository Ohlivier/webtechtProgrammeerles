from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Verzend')


class TaalForm(FlaskForm):
    taal = StringField('Taal')
    submit = SubmitField('Verzend')


class CursusForm(FlaskForm):
    cursus = StringField('Cursus', validators=[DataRequired()])
    sumbit = SubmitField('Verzend')
