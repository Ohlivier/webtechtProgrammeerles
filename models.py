from datetime import datetime
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    role = db.Column(db.String(), nullable=False, default='user')
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f'User: {self.username} \n Email: {self.email} \n password: {self.password_hash}'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Talen(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False, unique=True)


class Lessen(db.Model):
    lesID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    docentID = db.Column(db.Integer, db.ForeignKey('users.id'))
    talenID = db.Column(db.Integer, db.ForeignKey('talen.id'), nullable=False)
    startDatum = db.Column(db.DateTime, default=datetime.now)
    locatie = db.Column(db.String(), nullable=False)

    def __init__(self, lesID, userID, talenID):
        self.lesID = lesID
        self.userID = userID
        self.talenID = talenID

    # Get username by docentID
    # db.session.query(User).join(Lessen, User.id == Lessen.docentID).filter(User.role == 'admin').filter(Lessen.lesID == 1).first().username
