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
    View page function that creates and returns the post titles on the index page
    '''
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(actual_post=form.post.data,category=form.category.data, user_id=current_user.id)
        new_post.save_post()
        flash('Post has been created successfully')
        return redirect(url_for('.index'))
    post = Post.query.all()

    General = Post.query.filter_by(category='General')
    Cars = Post.query.filter_by(category='Cars')
    Technology = Post.query.filter_by(category='Technology')
    return render_template('index.html',title = 'new_post',form=form, General=General, post=post, Cars=Cars, Technology=Technology)

@main.route('/post/comments/new/<int:id>', methods = ['GET','POST'])
# @login_required
def new_comment(id):
    '''
    Function for creating new comments on the new_comments.html template
    '''
    form = CommentsForm()
    post = Comment.query.filter_by(post_id=id).all()
    if form.validate_on_submit():

        # Updated review instance
        new_comment = Comment(post_id=id, comments=form.comments.data)

        # save review method
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.new_comment',id=new_comment.post_id))
    title = 'comment'
    return render_template('new_comment.html',title = title, comment_form=form, post=post)


@main.route('/comments/<int:id>', methods = ['GET','POST'])
# @login_required
def comment(id):
    '''
    Function that displays the comments created to the comments.html template
    '''
    post = Comment.query.filter_by(post_id=id).order_by(Comment.timestamp.desc()).all()
    return render_template('comments.html',title = 'Comments', post=post)




# @main.route('/delete_comment/<int:id>', methods = ['POST'])
# @login_required
# def delete_comment(id):
#     '''
#     Function that deletes comments from posts
#     '''
#     post = Comment.query.filter_by(post_id=id).order_by(Comment.timestamp.desc()).all()
    
#     db.session.delete(new_comment)
#     db.session.commit()
#     return render_template('comments.html',title = 'Comments', post=post)


# @main.route('/delete_post/<int:id>', methods = ['POST'])
# @login_required
# def delete_comment(id):
#   '''
#   Function that deletes posts
#   '''
#   post = Post.query.filter_by(id=id).first()

#   db.session.delete(post)
#   db.session.commit()
#   return render_template('comments.html',title = 'Comments', post=post)


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




@main.route('/delete/<int:id>', methods=['POST','GET'])
def delete(id):
    try:
        if current_user.is_authenticated:
            posts = Post.query.all()
            post_form = PostForm()
            fetched_comment = Post.query.filter_by(id=id).first()
            db.session.delete(fetched_comment)
            db.session.commit()
            posts = Post.query.all()
            return redirect(url_for('main.index',posts=posts,form=post_form))

        return 

    except Exception as e:
        return (str(e))

# @main.route('/deletecomment/<int:>', methods=['POST','GET'])

@main.route('/deletecomment/<int:id>', methods=['POST','GET'])
def delete_commen(id):
    try:
        if current_user.is_authenticated:
            form = CommentsForm()
            fetched_comment = Comment.query.filter_by(id=id).first()
            db.session.delete(fetched_comment)
            db.session.commit()
            # post_id = Comment.query.filter_by()
            return redirect(url_for('main.index'))
        return ''

    except Exception as e:
        return (str(e))

