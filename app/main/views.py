from flask import render_template, request, redirect, url_for, abort, flash
from . import main
# from .. import db
# from ..models import User

@main.route('/',methods=['GET','POST'])
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    # form = PitchForm()

    # if form.validate_on_submit():
    #     new_post = Blog(actual_post=form.pitch.data,category=form.category.data, user_id=current_user.id)
    #     new_post.save_post()
    #     flash('Post has been created successfully')
    # Post = Post.query.filter_by(id)

    return render_template('index.html',title = 'new_post')