from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
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
    post = db.relationship('Post',backref = 'user',lazy = "dynamic")
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


class Post(db.Model):
    '''
    This is Post class that defines the tables in the post database
    '''

    post_list = []
    __tablename__ = 'post'

    id = db.Column(db.Integer,primary_key = True)
    actual_post = db.Column(db.String(255))
    vote_count = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post = db.relationship('Comment',backref = 'post',lazy = "dynamic")


    def save_post(self):
        '''
        Function that saves the posts created by the bloggers
        '''
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    '''
    Class Comments for the Comments column
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime,index= True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    
    
    def delete_comment(self):
        '''
        Function that delete the comments on a post
        '''
        db.session.delete(self)
        db.session.commit()

