from . import db, migrate


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'User: {self.username} \n Email: {self.email} \n password: {self.password}'
