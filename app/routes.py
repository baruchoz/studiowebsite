
from app import app, db
from flask import render_template, redirect, url_for, flash, session, request
from flask_login import  login_user, logout_user, current_user, login_required
from app.forms import LoginForm, RegisterForm, PostForm, UpdateAccountForm, EditProfileForm
from app.models import Product, User, Post
from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html", title="Home - BE Studios")

@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():   
        firstname = register_form.firstname.data
        lastname = register_form.lastname.data
        email = register_form.email.data
        username = register_form.username.data
        password = register_form.password.data
        existing_user = User.query.filter_by(username=username).all()
        if existing_user:    
            flash(f'The username {username} is already registered. Please try again.', 'danger')
            return redirect(url_for('register'))

        new_user = User(firstname, lastname, username, email, password)

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


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        print('Hello')
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, current_user.id)
        db.session.add(new_post)
        db.session.commit()

        flash(f'The post {title} has been created.', 'primary')
        return redirect(url_for('index'))
        
    return render_template('createpost.html', form=form)




@app.route('/my-posts')
@login_required
def my_posts():
    posts = current_user.posts
    return render_template('my_posts.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)


@app.route('/posts/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author.id != current_user.id:
        flash('That is not your post. You may only edit posts you have created.', 'danger')
        return redirect(url_for('blog.my_posts'))
    form = PostForm()
    if form.validate_on_submit():
        new_title = form.title.data
        new_content = form.content.data
        print(new_title, new_content)
        post.title = new_title
        post.content = new_content
        db.session.commit()

        flash(f'{post.title} has been saved', 'success')
        return redirect(url_for('blog.post_detail', post_id=post.id))

    return render_template('post_update.html', post=post, form=form)


@app.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You can only delete your own posts', 'danger')
        return redirect(url_for('blog.my_posts'))

    db.session.delete(post)
    db.session.commit()

    flash(f'{post.title} has been deleted', 'success')
    return redirect(url_for('blog.my_posts'))



@app.route('/services')
def services():
    title = "Services - BE Studios"
    return render_template("services.html", title=title)

@app.route('/shop')
def shop():
    
    return render_template("shop.html", title='Shop - BE Studios')



@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)


@app.route('/products/<prod_id>')
def product_detail(prod_id):
    print(prod_id)
    product = Product.query.get_or_404(prod_id)
    return render_template('product_detail.html', product=product)

@app.route('/cart')
@login_required
def cart():
    my_products = current_user.products
    return render_template('products.html', products=my_products)

@app.route('/add-to-cart/<prod_id>')
@login_required
def add_to_cart(prod_id):
    product = Product.query.get_or_404(prod_id)
    current_user.products.append(product)
    db.session.commit()
    return redirect(url_for('my_cart'))