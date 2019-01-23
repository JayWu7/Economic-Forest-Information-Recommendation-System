from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length
    (1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z[A-Za-z0-9_.]*$]',
                                                          message='Username must have only letters, numbers, dots or underscores')])
    mobile_phone = IntegerField('Mobile Phone', validators=[DataRequired(), Length(11, 11,
                                                                                   message="Mobile phone numbers format error!")])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password_again', message="passwords unmatch")])
    password_again = PasswordField('Confirm password')
    submit = SubmitField('Register')


class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')
