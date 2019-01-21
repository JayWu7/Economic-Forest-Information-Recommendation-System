from flask import render_template
from . import auth
from .forms import LoginForm


@auth.route('/')
def index():
    return render_template('base.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['GET'])
def logout():
    pass

@auth.route('/password_reset_request')
def password_reset_request():
    pass

@auth.route('/register')
def register():
    pass