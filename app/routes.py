from app import app
from flask import render_template


@app.route('/')
def index():
    title = "BE Studio's Homepage"
    return render_template("index.html", title=title)