from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button = SubmitField()

class BookForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places=2)
    author = StringField('author')
    genre = StringField('genre')
    publisher = StringField('publisher')
    edition = StringField('edition')
    language = StringField('language')
    cost_of_prod = DecimalField('cost of prod', places = 2)
    series = StringField('series')
    dad_joke = StringField('dad joke')
    submit_button = SubmitField()


    