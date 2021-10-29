from flask import Flask
from config import Config

app = Flask(__name__)


with app.app_context():
    from routes.lecture1 import *
    from routes.weather import *

app.run(debug=True)
