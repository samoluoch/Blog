from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .. import db
from ..models import User
from app import login_manager
from .forms import PostForm
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
    Post = Post.query.filter_by(id)

    return render_template('index.html',title = 'new_post')

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
    title = ' comment'
    return render_template('new_comment.html',title = title, comment_form=form, pitchs=pitch)
