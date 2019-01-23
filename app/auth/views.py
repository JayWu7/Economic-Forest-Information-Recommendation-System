from flask import render_template
from . import auth
from .forms import LoginForm, RegisterForm, ResetPasswordForm


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
        pass
    return render_template('auth/register.html', form=form)