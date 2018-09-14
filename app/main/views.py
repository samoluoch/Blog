from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .. import db
from ..models import User,Post,Comment
from app import login_manager
from .forms import PostForm,CommentsForm
@main.route('/',methods=['GET','POST'])
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(actual_post=form.post.data,category=form.category.data, user_id=current_user.id)
        new_post.save_post()
        flash('Post has been created successfully')
    post = Post.query.all()

    General = Post.query.filter_by(category='General')
    Cars = Post.query.filter_by(category='Cars')
    Technology = Post.query.filter_by(category='Technology')

    return render_template('index.html',title = 'new_post',form=form, General=General, post=post, Cars=Cars, Technology=Technology)

@main.route('/post/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    post = Comment.query.filter_by(post_id=id).all()
    if form.validate_on_submit():

        # Updated review instance
        new_comment = Comment(post_id=id, comments=form.comments.data)

        # save review method
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.comments'))
    title = 'comment'
    return render_template('comments.html',title = title, comment_form=form, post=post)

















@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



