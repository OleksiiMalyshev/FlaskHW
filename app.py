from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

with app.app_context():
    from routes.main import *
    from routes.api.salons import *
    from routes.api.plants import *
    from routes.api.employees import *

app.run(host= '0.0.0.0', port =8080, debug=True)