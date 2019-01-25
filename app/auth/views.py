from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user,logout_user
from . import auth
from .. import db
from .forms import LoginForm, RegisterForm, PasswordResetRequestForm, ChangePasswordForm
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))  #return current page or index page
        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/change_password', methods=['GET','POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/change_password.html', form=form)

@auth.route('/password_reset_request', methods=['GET', 'POST'])
def password_reset_request():
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/reset_password.html', form=form)

@auth.route('/change_email_request', methods=['GET', 'POST'])
def change_email_request():
    return ''


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
