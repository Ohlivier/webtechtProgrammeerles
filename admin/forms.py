from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class SetEmail(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit1 = SubmitField('Submit')


class SetUsername(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required')])
    submit2 = SubmitField('Submit')


class SetRole(FlaskForm):
    role = SelectField('Role', validators=[DataRequired()], choices=[('User', 'user'), ('Admin', 'admin')])
    submit3 = SubmitField('Submit')
