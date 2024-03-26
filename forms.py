from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .models import User


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Doorgaan')


class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Bevestigd')])
    pass_confirm = PasswordField('Bevestig Wachtwoord', validators=[DataRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al vergeven, probeer een ander naam!')


class DeleteForm(FlaskForm):
    username = StringField('Gebruikersnaam')
