from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


# Keep line below at bottom of page
from app import routes, models