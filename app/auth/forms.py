from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    '''
    This is a user login form that allows users to enter their login details and validates the details
    '''
    email = StringField('Enter Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Your Password',validators =[Required()])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Login In')


class RegistrationForm(FlaskForm):
    '''
    This is user registration form that allows new users to register on the app
    '''
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password2',message = 'Passwords must match')])
    password2 = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')



