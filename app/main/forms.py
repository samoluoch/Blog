from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo

class PostForm(FlaskForm): #create a class that inherits from FlaskForm class
    category = SelectField('Category', choices =[('General','General'),('Cars','Cars'),('Technology','Technology')],validators=[Required()])
    post = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')



class CommentsForm(FlaskForm):
    comments = TextAreaField('Comment on the Post', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR POST')
    submit = SubmitField('SUBMIT')


