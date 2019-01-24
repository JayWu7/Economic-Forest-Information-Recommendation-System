from flask import render_template, url_for, redirect
from . import auth
from .. import db
from .forms import LoginForm, RegisterForm, ResetPasswordForm
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET'])
def logout():
    pass


@auth.route('/password_reset_request', methods=['GET', 'POST'])
def password_reset_request():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/reset_password.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        #'''email certification'''
        return redirect(url_for('.login'))
    return render_template('auth/register.html', form=form)
