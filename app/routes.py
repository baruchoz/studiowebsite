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

@app.route('/ourteam')
def ourteam():
    title = "Our Team - BE Studios"
    return render_template("ourteam.html", title=title)

@app.route('/services')
def services():
    title = "Services - BE Studios"
    return render_template("services.html", title=title)

@app.route('/booking')
def booking():
    title = "Booking - BE Studios"
    return render_template("booking.html", title=title)