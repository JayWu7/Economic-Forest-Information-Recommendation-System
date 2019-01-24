from . import db,login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    mobile_phone = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(20))

    def verify_password(self, password):
        return self.password == password



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))