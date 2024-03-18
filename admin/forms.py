from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from ..models import Talen


class SetEmail(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit1 = SubmitField('Submit')


class SetUsername(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required')])
    submit2 = SubmitField('Submit')


class SetRole(FlaskForm):
    role = SelectField('Role', validators=[DataRequired()], choices=[('user', 'User'), ('admin', 'Admin')])
    submit3 = SubmitField('Submit')


class AddTaal(FlaskForm):
    taal = StringField('Taal', validators=[DataRequired(message='Taal is required')])

    submit = SubmitField('Voeg toe')

    def validate_taal(self, field):
        if Talen.query.filter_by(name=field.data).first():
            raise ValidationError('Deze taal bestaat al!')


class DeleteTaal(FlaskForm):
    delete = SubmitField('DELETE')

class CreateCursus(FlaskForm):
    pass