from werkzeug.routing import ValidationError

from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.hashed_password = generate_password_hash(password)

    def __repr__(self):
        return f'User: {self.username} \n Email: {self.email} \n password: {self.password}'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


