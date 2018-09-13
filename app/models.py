# from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    '''
    This is a User class that defines the object User and it's database tables
    '''
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    blog = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    user_id = db.relationship('Comment',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('This password is inaccessible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'