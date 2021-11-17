from app import app
from flask import render_template, redirect, url_for, flash, session, request
from app.forms import LoginForm, RegisterForm, AccountInfoForm


@app.route('/')
def index():
    title = "Home - BE Studios"
    return render_template("index.html", title=title)

@app.route('/login')
def login():
    title = "Sign In - BE Studios"
    login_form = LoginForm()

    return render_template("login.html", title=title, form=login_form)


@app.route('/register', methods=["GET", "POST"])
def register():
    title = "Register - BE Studios"
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        print("This form has been submitted correctly")
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)
    return render_template("register.html", title=title, form=register_form)


@app.route('/services')
def services():
    title = "Services - BE Studios"
    return render_template("services.html", title=title)

@app.route('/booking')
def booking():
    title = "Booking - BE Studios"
    return render_template("booking.html", title=title)