from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, NumberRange
from wtforms import ValidationError
from ..models import User


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
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                          message='Username must have only letters, numbers, dots or underscores')])
    mobile_phone = IntegerField('Mobile Phone', validators=[DataRequired(), NumberRange(10000000000, 19999999999,
                                                                                   message="Mobile phone numbers format error")])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password_again', message="passwords unmatch")])
    password_again = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password_again', message="passwords must match")
    ])
    password_again = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')

class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1,64),
                                                 Email()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password_agaim', message="passwords must match")
    ])
    password_again = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update Password')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')




