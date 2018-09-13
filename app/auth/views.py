from . import auth
from .forms import LoginForm
from flask_login import login_manager,login_required,logout_user,login_user,current_user
from flask import render_template,redirect,url_for,flash,request

@auth.route('/login',methods=['GET','POST'])

def login():
    '''
    This is a user login route that allows users to login
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/logout')

@login_required
def logout():
    '''
    This is a User logout route that redirects the users to the logout page after they logout
    '''
    logout_user()
    flash('You have successfully logged out')
    return redirect(url_for("main.index"))



