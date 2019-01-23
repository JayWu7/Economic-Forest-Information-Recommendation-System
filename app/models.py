from . import db

class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    mobile_phone = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(20))