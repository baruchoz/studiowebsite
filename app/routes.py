from app import app
from flask import render_template


@app.route('/')
def index():
    title = "Home - BE Studios"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    title = "About - BE Studios"
    return render_template("about.html", title=title)

@app.route('/services')
def services():
    title = "Services - BE Studios"
    return render_template("services.html", title=title)

@app.route('/booking')
def booking():
    title = "Booking - BE Studios"
    return render_template("booking.html", title=title)

@app.route('/signin')
def signin():
    title = "Sign In - BE Studios"
    return render_template("signin.html", title=title)

@app.route('/signup')
def signup():
    title = "Sign Up - BE Studios"
    return render_template("signup.html", title=title)