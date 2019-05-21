from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length



class SearchForm(FlaskForm):
    key_word = StringField('search',validators=[DataRequired(),Length(1, 32)])
    submit = SubmitField('Search')
