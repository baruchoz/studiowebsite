
from app import app, db
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import  login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegisterForm, PostForm
from app.models import User, Post


@app.route('/')
def index():
    return render_template("index.html", title="Home - BE Studios")


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():   
        email = register_form.email.data
        username = register_form.username.data
        password = register_form.password.data
        
        existing_user = User.query.filter_by(username=username).all()
        if existing_user:
            # Flash a warning message 
            flash(f'The username {username} is already registered. Please try again.', 'danger')
            # Redirect back to the register page
            return redirect(url_for('register'))

        new_user = User(username, email, password)

        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username}, you have successfully registered!', 'success')
        
        return redirect(url_for('login'))

    return render_template("register.html", title="Register - BE Studios", form=register_form)



@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():

        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash('Your username or password is incorrect', 'danger')
            return redirect(url_for('login'))

        login_user(user)

        flash(f'Welcome {user.username}. You have successfully logged in.', 'success')
        
        return redirect(url_for('index'))

    return render_template("login.html", title="Sign In - BE Studios", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account') 
@login_required 
def my_account():     
    return render_template('account.html', title="Account - BE Studios")


@app.route('/createpost', methods=['GET', 'POST'])
# @login_required
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        # print('Hello')
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, user_id=1)
        db.session.add(new_post)
        db.session.commit()

        # flash(f'The post {title} has been created.', 'primary')
        # return redirect(url_for('index'))
        
    return render_template('createpost.html', form=form)



@app.route('/services')
def services():
    title = "Services - BE Studios"
    return render_template("services.html", title=title)



@app.route('/booking')
def booking():
    title = "Booking - BE Studios"
    return render_template("booking.html", title=title)